"""
You’re going to draw a face with eyes that will follow the mouse!
"""

# 0. Make sure you complete the other assignments in this folder first!

# 1. Find an image on the internet or use the provided image (big_eye_bird.png)
# and drop it into your sketch. It can be anything as long as it has large eyes!

def setup():
    # 2. Import your image using the following code:
    #global face
    global face
    face = loadImage("big eyes.jpeg")

    
    # 3. Set the size of your sketch and the size of your image to be
    # the same by entering the following code in the setup method.
    size(600, 900)
    face.resize(width, height)

    
def draw():
    # 4. Draw your image using:
    background(face)

    # 5. Place a white circle over the left eye of your image.
    # *HINT* The current position of the mouse is printed to the
    # console. Use it to find the center of the left eye.
    # fill(<your color>)
    fill(255, 255, 255)
    circle(230, 200, 250)

    println(str(mouseX) + ' ' + str(mouseY))
    draw_googly_eye(230, 200, 250, 50)
    # 6. Call the draw_gooly_eye function with the correct input parameters to draw
    # the pupil insdie the eye. Does it stay inside the eye and follow the mouse?

    # 7. Repeat the steps above for the right eye and observe the googly eyes!
    fill(255, 255, 255)
    circle(420, 208, 170)
    draw_googly_eye(420, 208, 170, 50)
    

# ======================= DO NOT MODIFY THE CODE BELOW ==========================

def draw_googly_eye(eye_center_x, eye_center_y, eye_diameter, pupil_diameter):
    fill(0)
    if is_mouse_inside_eye(eye_center_x, eye_center_y, eye_diameter/2, pupil_diameter/2):
        circle(mouseX, mouseY, pupil_diameter)
    else:
        position = get_eye_position(eye_center_x, eye_center_y, eye_diameter/2, pupil_diameter/2)
        circle(position.x, position.y, pupil_diameter)

def is_mouse_inside_eye(eye_center_x, eye_center_y, eye_radius, pupil_radius):
    dist_x = mouseX - eye_center_x;
    dist_y = mouseY - eye_center_y;
    distance = sqrt( (dist_x * dist_x) + (dist_y * dist_y) )
    
    if distance <= eye_radius - pupil_radius:
        return True
    
    return False

def get_eye_position(eye_center_x, eye_center_y, eye_radius, pupil_radius):
    position = Position()
    
    if mouseX - eye_center_x != 0:
        angle = atan2( mouseY - eye_center_y, mouseX - eye_center_x )
        position.x = eye_center_x + ((eye_radius - pupil_radius) * cos(angle))
        position.y = eye_center_y + ((eye_radius - pupil_radius) * sin(angle))

    return position

class Position:
    x = float()
    y = float()
