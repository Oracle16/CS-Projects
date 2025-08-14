from oasis import Oasis
from random import choice

def getInt(prompt, low, high):
  ans = low-1
  while not low <= ans <= high:
    try:
      ans = int(input(prompt))
      if ans < low:
        print(f'The value must be at least {low}')
      if ans > high:
        print(f'The value must be at most {high}')
    except ValueError:
      print('Illegal response')
  return ans

def getYesNo(prompt):
  while True:
    response = input(prompt).strip().lower()
    if response in ('y','yes'):
      return True
    elif response in ('n','no'):
      return False
    else:
      print('Unrecognized response')

def addEgg(w,rows,cols):
  while True:
    r = getInt('In what row is the egg? ', 0, rows-1)
    c = getInt('In what column is the egg? ', 0, cols-1)
    if (r,c) == (0,0):
      print('The person starts at (0,0) so that cannot be an egg')
    else:
      w.addEgg(r,c)
      return

# Text based visualizer
class TextViz:

  def __init__(self, world):
    self._w = world

  def update(self):
    rows = w.numRows()
    cols = w.numColumns()
    eggs = set()
    try:
      eggs = set(w.eggLocations())
    except:
      pass

    for r in range(rows,-2,-1):
      for c in range(-1,1+cols):
        if 0 <= r < rows and 0 <= c < cols:
          if (r,c) == tuple(w.playerLocation()):
            symbol = '@'
          elif (r,c) in eggs:
            symbol = 'o'
          else:
            symbol = '.'
        else:
          symbol = '#'  # wall
        print(symbol,end='')
      print()  # end of row
    print(f'Current Score: {w.getScore()}, Eggs remaining: {len(eggs)}')
               

# cs1graphics based visualizer
class GraphicsViz:
  def __init__(self, world):
    self._w = world
   
    self._canvas = canvas = Canvas(self._w.numColumns()*50, self._w.numRows()*50+50)
    self._eggs = self.eggLayer()
    self._canvas.add(self._eggs)
    msg = f'Current Score: {w.getScore()}\nEggs remaining: {len(self._w.eggLocations())}'
    self._message = Text(msg, 12, Point(self._canvas.getWidth()/2,self._canvas.getHeight()-30))
    self._message.setJustification('left')
    self._canvas.add(self._message)

    # Grid graphics
    canvas.setAutoRefresh(False)
    for x in range(self._w.numColumns()):
      for y in range(self._w.numRows()):
        gridSquare = Rectangle(50,50)
        canvas.add(gridSquare)
        gridSquare.moveTo(x*50+25, y*50+25)
        gridSquare.setFillColor("white")
        gridSquare.setBorderColor("black")
    canvas.setAutoRefresh(True)

    # Person graphics
    personLocation = self._w.playerLocation()
    person = Layer()
    
    self._face = Circle(15, Point(personLocation[1]*50+25, self._w.numRows()*50 - personLocation[0]*50 - 25))
    self._face.setFillColor("white")
    self._face.setBorderColor("black")
    self._face.setDepth(2)
    person.add(self._face)

    self._eye1 = Circle(2, Point(personLocation[1]*50+20, self._w.numRows()*50 - personLocation[0]*50-25))
    self._eye1.setFillColor("black")
    self._eye1.setDepth(1)
    person.add(self._eye1)

    self._eye2 = Circle(2, Point(personLocation[1]*50+30, self._w.numRows()*50 - personLocation[0]*50-25))
    self._eye2.setFillColor("black")
    self._eye2.setDepth(1)
    person.add(self._eye2)

    canvas.add(person)
    person.setDepth(10)


  def eggLayer(self):
    lay = Layer()
    lay.setDepth(5)
    # Egg graphics
    for egg in self._w.eggLocations():
      color = 'gold'
      size = 0.3
      
      topcir = Circle(30*size,Point(85*size, -95*size))
      topcir.move(50*egg[1], 50*(self._w.numRows()-egg[0]))
      topcir.setFillColor(color)
      topcir.setBorderColor('transparent')
      
      botcir = Circle(40*size,Point(85*size, -65*size))
      botcir.move(50*egg[1], 50*(self._w.numRows()-egg[0]))
      botcir.setFillColor(color)
      botcir.setBorderColor('transparent')
      
      trap = Polygon(Point(52*size,-100*size),Point(115*size,-100*size),Point(125*size,-65*size),Point(45*size,-65*size))
      trap.move(50*egg[1], 50*(self._w.numRows()-egg[0]))
      trap.setFillColor(color)
      trap.setBorderColor('transparent')
      
      lay.add(topcir)
      lay.add(botcir)
      lay.add(trap)
    return lay

  def update(self):
    self._face.moveTo(self._w.playerLocation()[1]*50+25, self._w.numRows()*50 - self._w.playerLocation()[0]*50 - 25)
    self._eye1.moveTo(self._w.playerLocation()[1]*50+20, self._w.numRows()*50 - self._w.playerLocation()[0]*50-30)
    self._eye2.moveTo(self._w.playerLocation()[1]*50+30, self._w.numRows()*50 - self._w.playerLocation()[0]*50-30)

    self._canvas.remove(self._eggs)
    self._eggs = self.eggLayer()
    self._canvas.add(self._eggs)
    self._message.setMessage(f'Current Score: {w.getScore()}\nEggs remaining: {len(self._w.eggLocations())}')

 
# setup basic world
print("Welcome to our new game. Let's begin by setting up an oasis with Easter eggs.")
rows = getInt('How many rows does the world have? ', 1, float('inf'))
cols = getInt('How many columns does the world have? ', 1, float('inf'))
w = Oasis(rows,cols)

# consider extra credit
moreEggs = True
while moreEggs:
  moreEggs = getYesNo('Would you like to add an egg? ')
  if moreEggs:
    addEgg(w,rows,cols)

# consider visualizer
graphics = getYesNo('Would you like a cs1graphics visualization? ')
if graphics:
  from cs1graphics import *
  viz = GraphicsViz(w)
else:
  viz = TextViz(w) 

# start moving
print()
viz.update()
while True:
  raw = input('Enter one of (U)p, (D)own, (L)eft, (R)ight, (Q)uit: ').strip()
  response = raw.upper()[:1]
  if response in ('U','D','L','R'):
    if response == 'U':
      success = w.moveUp()
    elif response == 'D':
      success = w.moveDown()
    elif response == 'L':
      success = w.moveLeft()
    else:
      success = w.moveRight()

    if not success:
      print('The player was unable to move.')
    else:
      loc = w.playerLocation()
      print(f'The person moved to row {loc[0]}, column {loc[1]}')

    viz.update()

  elif response == 'Q':
    break

  else:
    print('Unrecognized command:',raw)

print('Thanks for playing.')
