"""
The player of the game has to click the mouse where the donkey's
tail will go. The problem is, the picture keeps disappearing!
"""

def setup():
    size(800, 600)
    
    global donkey
    donkey = loadImage('donkey.jpg')
    donkey.resize(width, height)
    
    global tail
    tail = loadImage('tail.png')
    
    global x
    global y
    x = None
    y = None
    global hasclicked
    hasclicked = False
    
    noStroke()
    
def draw():
    global x
    global y
    global hasclicked
    # 1. Use the background() function to draw the donkey

    # 2. Use the rect() function to draw a box in the upper left
    # corner of the screen:
    rect(0, 0, 30, 30)
    
    # 3. Now find the x and y coordinates where the tail attaches
    # to the donkey and draw another box with a side of 50
    rect(700, 150, 50, 50)
    # 4. Change your code so the donkey is only shown when the
    # mouse is inside the corner bounding box. 
    #
    # Hint: check if mouseX is greater than 0 and less than 30
    # and y is greater than 0 and less than 30
    if mouseX > 0 and mouseX < 30 and mouseY > 0 and mouseY < 30:
        background(donkey)
    else:
        background(255,255,255)

    

    
    # 5. Check that when the mouse is outside the corner box,
    # you should show a solid color background.
    
    # 6. Use the image() method to draw the tail at the mouseX
    # and mouseY location. For example,
    if hasclicked == False:
        x = mouseX
        y = mouseY
    if mousePressed:
        hasclicked = True
    image(tail, x, y)
    
    # 7. Now, adjust your code so the tail sticks when you click the
    # mouse (this means it will no longer move when the mouse moves)
    #
    # Hint: you will need to use the mousePressed variable and set the
    # x and y variables declared in setup()
        
    # 8. When the tail has been pinned, write code to check if the
    # tail was pinned inside the target bounding box.
    if x > 700 and x < 650 and y > 150 and y < 200:
        pass
        
    # 9. Show the donkey so the user knows where they pinned the tail.
    if hasclicked == True:
        background(donkey)
        image(tail, x, y)
