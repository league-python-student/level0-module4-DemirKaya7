"""
You’re going to draw a face with eyes that will follow the mouse!
"""

# 1. Find an image on the internet and drop it into your sketch.
# It can be anything as long as it has large eyes!

def setup():
    # 2. Import your image using the following code:
    global face
    face = loadImage("big_eye_bird.png")

    
    # 3. Set the size of your sketch and the size of your image to be
    # the same by entering the following code in the setup method.
    size(800, 600)
    face.resize(width, height)

    global left_eye_x
    left_eye_x = 250
    global left_eye_y
    left_eye_y = 160
    global eye_radius
    eye_radius = 300
    global pupil_radius
    pupil_radius = 50
    
def draw():
    # 4. Draw your image using:
    global face
    global left_eye_x
    global left_eye_y
    global eye_radius
    global pupil_radius
    background(face)

    # 5. Place a white ellipse over the left eye of your image.
    fill(255, 255, 255)
    ellipse(250, 160, 300, 300)
    println(str(mouseX) + ' ' + str(mouseY))   
    
    # 6. Now add a pupil (the black part) to the left eye earlier.
    # Use the pupil x and y variables for the position.

    
    # 7. Run the program and check if the left eye is in the correct
    # position
    
    # 8. To make the pupil follow the mouse, the pupil's x and y positions
    # should be set to mouseX and mouseY when the mouse is inside the eye.
    # Use the is_mouse_inside_eye() function for this.
    
    if is_mouse_inside_eye(250, 160, eye_radius, pupil_radius):
        left_eye_x = mouseX
        left_eye_y = mouseY
        fill(0, 0, 0)
        ellipse(left_eye_x, left_eye_y, pupil_radius, pupil_radius)
    
    # If the mouse is not inside the eye, call the get_eye_position()
    # function:
    else:
        position = get_eye_position(250, 160, 300, 25)
        left_eye_x = position.x
        left_eye_y = position.y
        fill(0, 0, 0)
        ellipse(left_eye_x, left_eye_y, pupil_radius, pupil_radius)
    
    
    # 9. Repeat the steps above for the right eye and observe the googly eyes!

# ======================= DO NOT MODIFY THE CODE BELOW ==========================

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
