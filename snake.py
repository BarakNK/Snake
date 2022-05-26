import turtle
import random

turtle.bgcolor("black")
turtle.tracer(1, 0) #This helps the turtle move more smoothly
turtle.penup()
turtle.hideturtle()

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y)

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

SQUARE_SIZE = 20
START_LENGTH = 8
TIME_STEP = 100

# Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

# Creating the snake
snake = turtle.clone()
snake.shape("square")
snake.color("turquoise")
snake.direction = "Up"

turtle.register_shape("food.gif") #Add food picture
food = turtle.clone()
food.shape("food.gif")

#Locations of first food stamps
food_positions = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
#Stamping the first food stamps. #TODO: Make this a function later on
for this_food_pos in food_positions:
    food.goto(this_food_pos)
    f_s=food.stamp()
    food_stamps.append(f_s)
    food.hideturtle()

def make_food():
    """
    This function creates a new food stamp and places it on the screen
    """
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a random position that is multiple of SQUARE_SIZE (so that the food will fit in the grid)
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    food_position=food.pos()
    food_positions.append(food_position)
    new_food_stamp=food.stamp()
    food_stamps.append(new_food_stamp)


def new_stamp():
    """
    This function draws a part of the snake on the screen   
    """
    snake_pos = snake.pos() #Get snake’s position
    pos_list.append(snake_pos) 
    stamp_ID = snake.stamp() #Set a stamp at the snake’s position and store its ID
    stamp_list.append(stamp_ID)


def remove_tail():
    """
    This function removes the last part of the snake as it moves forward
    """
    old_stamp = stamp_list.pop(0) #Pop last piece of tail from the list
    snake.clearstamp(old_stamp) #Erase last piece of tail
    pos_list.pop(0) #Remove last piece of tail's position


def up():
    snake.direction = "Up"
    print("You pressed the up key!")


def down():
    snake.direction = "Down"
    print("You pressed the down key")


def left():
    snake.direction = "Left"
    print("You pressed the left key")


def right():
    snake.direction = "Right"
    print("You pressed the right key")


# Create listeners for keyboard input
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.listen()


def main():
    pass

if __name__ == '__main__':
    main()
