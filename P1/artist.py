from cs1graphics import *
from time import sleep

# Paint the Canvas
x = 512
y = 480
bg = Canvas(x, y, bgColor=(92, 148, 252), title='SUPER MARIO BROS. 1-1', autoRefresh=True)

# Function to add Block Patterns to Ground Blocks
def addBlockPatterns(layer):
    # Pattern 1
    blockPattern1Shadow = Path(
        Point(2, 2),
        Point(14, 2),
        Point(14, -3),
        Point(8, -3),
        Point(8, -5),
        Point(4, -5),
        Point(4, -7),
        Point(0, -7)
    )
    blockPattern1Shadow.setBorderColor((234, 187, 181))
    blockPattern1Shadow.setBorderWidth(1.5)
    layer.add(blockPattern1Shadow)

    blockPattern1 = Path(
        Point(2, 2),
        Point(14, 2),
        Point(14, -3),
        Point(8, -3),
        Point(8, -5),
        Point(4, -5),
        Point(4, -7),
        Point(0, -7)
    )
    blockPattern1.setBorderColor('black')
    blockPattern1.setBorderWidth(1)
    layer.add(blockPattern1)

    # Pattern 2
    blockPattern2Shadow = Path(
        Point(14, 0),
        Point(16, 0),
        Point(16, -2),
        Point(17, -2),
        Point(17, -5),
        Point(18, -5),
        Point(18, -24)
    )
    blockPattern2Shadow.setBorderColor((234, 187, 181))
    blockPattern2Shadow.setBorderWidth(1.5)
    layer.add(blockPattern2Shadow)

    blockPattern2 = Path(
        Point(14, 0),
        Point(16, 0),
        Point(16, -2),
        Point(17, -2),
        Point(17, -5),
        Point(18, -5),
        Point(18, -24)
    )
    blockPattern2.setBorderColor('black')
    blockPattern2.setBorderWidth(1)
    layer.add(blockPattern2)

    # Pattern 3
    blockPattern3Shadow = Path(
        Point(30, -22),
        Point(30, -13),
        Point(22, -13),
        Point(22, -16)
    )
    blockPattern3Shadow.setBorderColor((234, 187, 181))
    blockPattern3Shadow.setBorderWidth(1.5)
    layer.add(blockPattern3Shadow)

    blockPattern3 = Path(
        Point(30, -22),
        Point(30, -13),
        Point(22, -13),
        Point(22, -16)
    )
    blockPattern3.setBorderColor('black')
    blockPattern3.setBorderWidth(1)
    layer.add(blockPattern3)

    # Pattern 4
    blockPattern4Shadow = Path(
        Point(30, -12),
        Point(30, 4),
        Point(29, 4),
        Point(29, 6),
        Point(18, 6),
        Point(18, 8)
    )
    blockPattern4Shadow.setBorderColor((234, 187, 181))
    blockPattern4Shadow.setBorderWidth(1.5)
    layer.add(blockPattern4Shadow)

    blockPattern4 = Path(
        Point(30, -12),
        Point(30, 4),
        Point(29, 4),
        Point(29, 6),
        Point(18, 6),
        Point(18, 8)
    )
    blockPattern4.setBorderColor('black')
    blockPattern4.setBorderWidth(1)
    layer.add(blockPattern4)

# Create the Opening Screen Layer
openingScreen = Layer()

# Create the Board
Board = Polygon(
    Point(82, 67),
    Point(82, 237),
    Point(429, 236),
    Point(429, 67)
)
Board.setFillColor((153, 78, 0))
Board.setBorderColor((242, 191, 182))
Board.setBorderWidth(1.5)
openingScreen.add(Board)

# Clone Transparent Fill Circle Rings
ring = Circle(5, Point(92,78))
ring.setBorderWidth(.5)
ring2 = ring.clone()
ring3 = ring.clone()
ring4 = ring.clone()
ring2.moveTo(92, 226)
ring3.moveTo(419, 226)
ring4.moveTo(419, 78)
openingScreen.add(ring)
openingScreen.add(ring2)
openingScreen.add(ring3)
openingScreen.add(ring4)

# Create the "SUPER MARIO BROS. 1-1" text
gameStart = Text('SUPER MARIO BROS. 1-1', 13, Point(255.5, 180))
gameStart.setDepth(30)
gameStart.setFontColor('white')
openingScreen.add(gameStart)

# The Golden Goomba's Appearance (character 1)! Use Layer class for easier manipulation
goldenGoomba = Layer()

# Gold Goomba Upper Body
goomba2Face = Polygon(
    Point(255.5, 152),
    Point(255.5, 154),
    Point(249.5, 154),
    Point(246.5, 153),
    Point(246.5, 146),
    Point(249.5, 142),
    Point(252.5, 139),
    Point(255.5, 136),
    Point(257.5, 133),
    Point(259.5, 131),
    Point(264.5, 131),
    Point(266.5, 133),
    Point(268.5, 136),
    Point(271.5, 139),
    Point(274.5, 142),
    Point(277.5, 146),
    Point(277.5, 153),
    Point(274.5, 154),
    Point(268.5, 154),
    Point(268.5, 152)
)
goomba2Face.setFillColor((243, 196, 19))
goomba2Face.setBorderColor((243, 196, 1))
goldenGoomba.add(goomba2Face)

# Gold Goomba Left Sclera
goomba2LeftSclera = Polygon(
    Point(255.5, 143),
    Point(254.5, 143),
    Point(254.5, 150),
    Point(259.5, 150),
    Point(259.5, 147),
    Point(258.5, 147),
    Point(258.5, 149),
    Point(255.5, 149)
)
goomba2LeftSclera.setFillColor((255, 255, 255))  
goomba2LeftSclera.setBorderColor((255, 255, 255))
goldenGoomba.add(goomba2LeftSclera)

# Gold Goomba Right Sclera
goomba2RightSclera = Polygon(
    Point(269.5, 143),
    Point(268.5, 143),
    Point(268.5, 149),
    Point(265.5, 149),
    Point(265.5, 147),
    Point(264.5, 147),
    Point(264.5, 150),
    Point(269.5, 150)
)
goomba2RightSclera.setFillColor((255, 255, 255))  
goomba2RightSclera.setBorderColor((255, 255, 255))
goldenGoomba.add(goomba2RightSclera)

# Gold Goomba Eyebrow
goomba2Eyebrow = Polygon(
    Point(272.5, 141),
    Point(272.5, 142),
    Point(268.5, 142),
    Point(267.5, 143),
    Point(267.5, 148),
    Point(266.5, 148),
    Point(266.5, 146),
    Point(257.5, 146),
    Point(257.5, 148),
    Point(256.5, 148),
    Point(256.5, 143),
    Point(255.5, 142),
    Point(251.5, 142),
    Point(251.5, 141),
    Point(254.5, 140),
    Point(258.5, 144),
    Point(265.5, 144),
    Point(268.5, 140)
)
goomba2Eyebrow.setFillColor((170, 131, 2))
goomba2Eyebrow.setBorderColor((170, 131, 2))
goldenGoomba.add(goomba2Eyebrow)

# Gold Goomba Lower Body
goomba2Body = Polygon(
    Point(256.5, 152),
    Point(254.5, 154),
    Point(254.5, 157),
    Point(258.5, 161),
    Point(260.5, 161),
    Point(260.5, 163),
    Point(263.5, 163),
    Point(263.5, 161),
    Point(266.5, 158),
    Point(269.5, 157),
    Point(269.5, 154),
    Point(267.5, 152)
)
goomba2Body.setFillColor((234, 208, 2))
goomba2Body.setBorderColor((234, 208, 2))
goldenGoomba.add(goomba2Body)

# Gold Goomba Left Shoe
goomba2LeftShoe = Polygon(
    Point(254.5, 157),
    Point(252.5, 157),
    Point(251.5, 158),
    Point(251.5, 160),
    Point(252.5, 161),
    Point(254.5, 163),
    Point(259.5, 163),
    Point(259.5, 162),
    Point(258.5, 161)
)
goomba2LeftShoe.setFillColor((145, 109, 3))
goomba2LeftShoe.setBorderColor((145, 109, 3))
goldenGoomba.add(goomba2LeftShoe)

# Gold Goomba Right Shoe
goomba2RightShoe = Polygon(
    Point(269.5, 157),
    Point(266.5, 158),
    Point(264.5, 160),
    Point(264.5, 163),
    Point(272.5, 163),
    Point(274.5, 161),
    Point(275.5, 161),
    Point(275.5, 159),
    Point(275.5, 158),
    Point(272.5, 156),
    Point(270.5, 156)
)
goomba2RightShoe.setFillColor((145, 109, 3))
goomba2RightShoe.setBorderColor((145, 109, 3))
goldenGoomba.add(goomba2RightShoe)

# The Walking Goomba's Appearance (character 2)! Use Layer class for easier manipulation (except the shoes)
walkingGoomba = Layer()

# Goomba Upper Body
goombaFace = Polygon(
    Point(303, 404),
    Point(303, 406),
    Point(297, 406),
    Point(294, 405),
    Point(294, 398),
    Point(297, 394),
    Point(300, 391),
    Point(303, 388),
    Point(305, 385),
    Point(307, 383),
    Point(312, 383),
    Point(314, 385),
    Point(316, 388),
    Point(319, 391),
    Point(322, 394),
    Point(325, 398),
    Point(325, 405),
    Point(322, 406),
    Point(316, 406),
    Point(316, 404)
)
goombaFace.setFillColor((200, 76, 12))
goombaFace.setBorderColor((200, 76, 12))
walkingGoomba.add(goombaFace)

# Goomba Left Sclera
goombaLeftSclera = Polygon(
    Point(303, 395),
    Point(302, 395),
    Point(302, 402),
    Point(307, 402),
    Point(307, 399),
    Point(306, 399),
    Point(306, 401),
    Point(303, 401)
)
goombaLeftSclera.setFillColor((244, 180, 165))  
goombaLeftSclera.setBorderColor((244, 180, 165))  
walkingGoomba.add(goombaLeftSclera)

# Goomba Right Sclera
goombaRightSclera = Polygon(
    Point(317, 395),
    Point(316, 395),
    Point(316, 401),
    Point(313, 401),
    Point(313, 399),
    Point(312, 399),
    Point(312, 402),
    Point(317, 402)
)
goombaRightSclera.setFillColor((244, 180, 165))  
goombaRightSclera.setBorderColor((244, 180, 165))
walkingGoomba.add(goombaRightSclera)

# Goomba Eyebrow
goombaEyebrow = Polygon(
    Point(320, 393),
    Point(320, 394),
    Point(316, 394),
    Point(315, 395),
    Point(315, 400),
    Point(314, 400),
    Point(314, 398),
    Point(305, 398),
    Point(305, 400),
    Point(304, 400),
    Point(304, 395),
    Point(303, 394),
    Point(299, 394),
    Point(299, 393),
    Point(302, 392),
    Point(306, 396),
    Point(313, 396),
    Point(316, 392)
)
goombaEyebrow.setFillColor((0, 0, 0))
walkingGoomba.add(goombaEyebrow)

# Goomba Lower Body
goombaBody = Polygon(
    Point(304, 405),
    Point(302, 407),
    Point(302, 410),
    Point(306, 414),
    Point(308, 414),
    Point(308, 416),
    Point(311, 416),
    Point(311, 414),
    Point(314, 411),
    Point(317, 410),
    Point(317, 407),
    Point(315, 405)
)
goombaBody.setFillColor((228, 168, 154))
goombaBody.setBorderColor((228, 168, 154))
walkingGoomba.add(goombaBody)

# Goomba Left Shoe (not part of the walking Goomba layer)
goombaLeftShoe = Polygon(
    Point(302, 410),
    Point(300, 410),
    Point(299, 411),
    Point(299, 413),
    Point(300, 414),
    Point(302, 416),
    Point(307, 416),
    Point(307, 415),
    Point(306, 414)
)
goombaLeftShoe.setFillColor((0, 0, 0))  
goombaLeftShoe.setBorderColor((0, 0, 0))

# Goomba Right Shoe (not part of the walking Goomba layer)
goombaRightShoe = Polygon(
    Point(317, 410),
    Point(314, 411),
    Point(312, 413),
    Point(312, 416),
    Point(320, 416),
    Point(322, 414),
    Point(323, 414),
    Point(323, 412),
    Point(323, 411),
    Point(320, 409),
    Point(318, 409)
)
goombaRightShoe.setFillColor((0, 0, 0))  
goombaRightShoe.setBorderColor((0, 0, 0))
                  
# Set Walking Frame 2 (to switch left and right shoes for walking animation)
center_x = 309.5

# Goomba Walking Animation Setup
goombaLeftShoeWalking = Polygon(
    Point(center_x - (317 - center_x), 410),
    Point(center_x - (314 - center_x), 411),
    Point(center_x - (312 - center_x), 413),
    Point(center_x - (312 - center_x), 416),
    Point(center_x - (320 - center_x), 416),
    Point(center_x - (322 - center_x), 414),
    Point(center_x - (323 - center_x), 414),
    Point(center_x - (323 - center_x), 412),
    Point(center_x - (323 - center_x), 411),
    Point(center_x - (320 - center_x), 409),
    Point(center_x - (318 - center_x), 409)
)
goombaLeftShoeWalking.setFillColor((0, 0, 0))  
goombaLeftShoeWalking.setBorderColor((0, 0, 0))

goombaRightShoeWalking = Polygon(
    Point(center_x - (302 - center_x), 410),
    Point(center_x - (300 - center_x), 410),
    Point(center_x - (299 - center_x), 411),
    Point(center_x - (299 - center_x), 413),
    Point(center_x - (300 - center_x), 414),
    Point(center_x - (302 - center_x), 416),
    Point(center_x - (307 - center_x), 416),
    Point(center_x - (307 - center_x), 415),
    Point(center_x - (306 - center_x), 414)
)
goombaRightShoeWalking.setFillColor((0, 0, 0))  
goombaRightShoeWalking.setBorderColor((0, 0, 0))

# Paint Background Elements (Pipe, Tree, Hill, Ground Blocks)

# Create the Pipe Layer
pipe = Layer()

# Pipe Top
pipeTop = Rectangle(62, 27, Point(256, 366))
pipeTop.setFillColor((128, 209, 2))  
pipeTop.setBorderWidth(2)
pipeTop.setDepth(50)
pipe.add(pipeTop)

# Pipe Body
pipeBody = Rectangle(55, 35, Point(256, 398))
pipeBody.setFillColor((128, 209, 2))  
pipeBody.setBorderWidth(2)
pipeBody.setDepth(100)
pipe.add(pipeBody)

# Create the Tree Layer
tree = Layer()

# Tree Trunk
treeTrunk = Rectangle(20, 40, Point(413.5, 394.5))
treeTrunk.setFillColor((254, 228, 155)) 
treeTrunk.setBorderWidth(2)
pipeTop.setDepth(100)
tree.add(treeTrunk)

# Tree Top
treeTop = Polygon(
    Point(271, 213),
    Point(271, 211),
    Point(266, 211),
    Point(266, 209),
    Point(264, 209),
    Point(264, 207),
    Point(262, 207),
    Point(262, 201),
    Point(260, 201),
    Point(260, 167),
    Point(262, 167),
    Point(262, 163),
    Point(264, 163),
    Point(264, 161),
    Point(266, 161),
    Point(266, 159),
    Point(271, 159),
    Point(271, 156),
    Point(278, 156),
    Point(278, 159),
    Point(282, 159),
    Point(282, 161),
    Point(285, 161),
    Point(285, 163),
    Point(287, 163),
    Point(287, 167),
    Point(289, 167),
    Point(289, 201),
    Point(287, 201),
    Point(287, 207),
    Point(285, 207),
    Point(285, 209),
    Point(282, 209),
    Point(282, 211),
    Point(278, 211),
    Point(278, 213)
    )
treeTop.setFillColor((114, 186, 51))
treeTop.setBorderWidth(2)
treeTop.moveTo(410, 379)
pipeTop.setDepth(50)
tree.add(treeTop)

# Final Elements and Layers Additions to Canvas

# Add Hill and Ground Path (Visual Aesthetic)
hill = Path(
    Point(0,415),
    Point(64, 351),
    Point(67, 351),
    Point(67, 349),
    Point(73, 349),
    Point(73, 347),
    Point(86, 347),
    Point(86, 349),
    Point(92, 349),
    Point(92, 351),
    Point(95, 351),
    Point(159,415),
    Point(0,415),
    Point(512,415)
)
hill.setBorderWidth(2)
hill.setDepth(50)

# Add Tree Layer 
bg.add(tree)

# Add Game Start Assets
bg.refresh()
bg.add(openingScreen)

# Add Golden Goomba (character 1)
bg.setAutoRefresh(False)
bg.add(goldenGoomba)

bg.refresh()
bg.setAutoRefresh(True)

# Add Block Patterns and Ground Blocks (animated)
for row in range(2):
    # Create 16 horizontal ground blocks (32x32 pixels each)
    for i in range(16):
        blockLayer = Layer()
        groundBlock = Square(32)

        # Set color palette/border-width of ground block to match original Super Mario Bros. 1-1
        groundBlock.setFillColor((153, 78, 0))
        groundBlock.setBorderWidth(1.5)
        # Interestingly, the row variable determines the y-coordinate of the ground block to "stack" them into a 2x16 grid
        # 15.5 is the most visually appealing
        groundBlock.moveTo(15.5 + 32 * i, 464 - 32 * row)
        groundBlock.setBorderColor((153, 78, 0))
        groundBlock.setBorderWidth(3)

         # Add the ground block to the layer
        blockLayer.add(groundBlock)

        # Add block patterns to the layer
        addBlockPatterns(blockLayer)

         # Add the layer to the canvas
        blockLayer.moveTo(1 + 32 * i, 473 - 32 * row)

        # Add the ground block to the layer
        bg.add(groundBlock)
        bg.add(blockLayer)
        sleep(0.05)

# Add Hill to the background
bg.add(hill)

# Add Pipe to the background
bg.setAutoRefresh(False)
bg.add(pipe)
bg.refresh()
sleep(0.5)

# Add Brown (Walking) Goomba (character 2) Layer to the background
walkingGoomba.setDepth(45)
bg.add(walkingGoomba)

# Add Goomba Shoes to the background for use in the walking animation
bg.add(goombaLeftShoe)
bg.add(goombaRightShoe)
bg.refresh()
sleep(1)
bg.setAutoRefresh(True)

# Walking Animation for Brown Goomba (character 2) - Partially Obstructing Tree
while True:
    # Move the Goomba to the right
    walkingGoomba.move(0.5, 0)
    goombaLeftShoe.move(0.5, 0)
    goombaRightShoe.move(0.5, 0)
    goombaLeftShoeWalking.move(0.5, 0)
    goombaRightShoeWalking.move(0.5, 0)
    
    # Alternate between the two walking frames
    bg.remove(goombaLeftShoe)
    bg.remove(goombaRightShoe)
    bg.add(goombaLeftShoeWalking)
    bg.add(goombaRightShoeWalking)
    bg.remove(goombaLeftShoeWalking)
    bg.remove(goombaRightShoeWalking)
    bg.add(goombaLeftShoe)
    bg.add(goombaRightShoe)

    # Use getX() to break the loop when the Goomba reaches the end of the screen (x-coordinate of 512)
    if walkingGoomba.getReferencePoint().getX() == x:
        break

sleep(1)
bg.setAutoRefresh(False)

# Remove Golden Goomba (character 1)
bg.remove(goldenGoomba)

# Remove Opening Screen Layer 
bg.remove(openingScreen)

# Reset Canvas Before End Screen (last frame)
bg.refresh()
bg.setAutoRefresh(True)
sleep(1)
bg.clear()

# End Screen (last frame)
bg.setBackgroundColor('black')
end = Text('GAME OVER', 18, Point(x/2, y/2))
end.setFontColor('white')
bg.refresh()
bg.add(end)