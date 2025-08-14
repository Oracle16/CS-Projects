# ===================================================================================
# file: backgammon.py
# author: Oracle16
# date: 02/22/2025
# ===================================================================================

from cs1graphics import *

# ask the user for the value of the number of pixels per grid-cell
pixelsPerGrid = int(input("Enter value of the number of pixels per grid-cell (e.g., 30): "))

# scale canvas
x = 15 * pixelsPerGrid
y = 13 * pixelsPerGrid

# use "size" variables to determine the width of each grid-cell
xBlockOffset = x/15
yBlockOffset = y/13

# account for systematic error due to divider
originalX = xBlockOffset

# create appropriate sized canvas
frame = Canvas(x, y)
frame.setBackgroundColor('burlywood4')

# set alternating color for triangles
colors = ['tan', 'darkorange3']

# create left pane
backgammonBoard = Rectangle(6*xBlockOffset, 11*yBlockOffset)
backgammonBoard.moveTo(xBlockOffset*4, yBlockOffset*6.5)
backgammonBoard.setFillColor('navajowhite')

# create right pane
rightPane = backgammonBoard.clone()
rightPane.moveTo(xBlockOffset*11, yBlockOffset*6.5)

# add elements to canvas
frame.add(backgammonBoard)
frame.add(rightPane)

# create upper layer of triangles (i.e., doritos)
dorito = Layer()
for i in range(12):
    triangle = Polygon(
    # left base point
    Point(xBlockOffset, yBlockOffset),
    # right base point
    Point(xBlockOffset*2, yBlockOffset),
    # tip point
    Point(xBlockOffset*1.5, yBlockOffset*6)
    )

    # alternate colors
    color = colors[i % len(colors)]
    triangle.setFillColor(color)
    
    # shift triangle one unit each time
    dorito.add(triangle)
    shiftX = xBlockOffset*i

    # account for divider gap
    if i >= 6:
        shiftX += originalX
    triangle.move(shiftX, 0)

frame.add(dorito)

# create lower layer of doritos
doritoLow = dorito.clone()
doritoLow.moveTo(xBlockOffset*15, yBlockOffset*13)
doritoLow.rotate(180)

frame.add(doritoLow)

# create divider (vertically splits left/right boards)
divider = Path(Point(x/2, 0), Point(x/2, y))
divider.setBorderWidth(pixelsPerGrid/15)
frame.add(divider)

numberSystem = Layer()

# create labels for numbers 24-13
for i in range(6):
   # Labels 24 to 19 on the left side
   label = Text(str(24 - i))  # Numbers from 24 down to
   label.moveTo(xBlockOffset * (i + 1) + xBlockOffset * 4 - xBlockOffset * 3.5, yBlockOffset * 0.5)
   label.scale(pixelsPerGrid/30)
   frame.add(label)

   # Labels 18 to 13 on the right side
   label = Text(str(18 - i))  # Numbers from 18 down to 13
   label.moveTo(xBlockOffset * (i + 1) + xBlockOffset * 7.5, yBlockOffset * 0.5)
   label.scale(pixelsPerGrid/30)
   frame.add(label)

# add labels for numbers 1-12
for i in range(12):
    # Labels 1 to 12
    label = Text(str(i + 1))
    shiftX = xBlockOffset * (i + 1) + xBlockOffset * 4 - xBlockOffset * 3.5

    if i >= 6:
        shiftX += originalX
    label.move(shiftX, yBlockOffset * 12.5)

    label.scale(pixelsPerGrid/30)
    frame.add(label)

# init checkers
for num,pt,whiteOnTop in [(2,1,True), (5,6,False), (3,8,False), (5,12,True)]:

    # set diameter and create checker
    diameter = (xBlockOffset/2)*0.9
    checker = Circle(diameter)
    
    # use num to create 'n' number of rows of circles (i.e., 2 rows, 5, 3, 8...)
    # create baseYOffset (readability)
    baseYOffset = yBlockOffset + diameter

    # for additional (top) layer
    for rows in range(num):
        checker = Circle(diameter)
        bottomChecker = checker.clone()
        frame.add(checker)
        frame.add(bottomChecker)

        # account for systematic error due to divider
        shiftX = pt*xBlockOffset
        if pt > 6:
            shiftX += originalX

        # set location of checkers on top/bottom 
        checker.move(shiftX + pixelsPerGrid/2, baseYOffset + yBlockOffset*rows*0.9)
        bottomChecker.move(shiftX + pixelsPerGrid/2, -yBlockOffset*rows*0.9)
        bottomChecker.move(0, y - 3.25*diameter)

        # set color of checkers on top/bottom
        if whiteOnTop:
            checker.setFillColor('white')
            # invert for bottom
            bottomChecker.setFillColor('black')
        else:
            checker.setFillColor('black')
            # invert for bottom
            bottomChecker.setFillColor('white')