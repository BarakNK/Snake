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
NUM_FOOD = 6

# Initialize lists for the snake and for the food
pos_list = []
stamp_list = []
food_positions = []
food_stamps = []

# Creating the snake
snake = turtle.clone()
snake.shape("square")
snake.color("turquoise")
snake.direction = "Up"

#Create food
turtle.register_shape("food.gif") #Add food picture
food = turtle.clone()
food.shape("food.gif")


def make_food():
    """
    This function creates a new food stamp and places it on the screen
    """
    min_x = -int(SIZE_X/2/SQUARE_SIZE)+1
    max_x = int(SIZE_X/2/SQUARE_SIZE)-1
    min_y = -int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y = int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a random position that is multiple of SQUARE_SIZE (so that the food will fit in the grid)
    food_x = random.randint(min_x, max_x)*SQUARE_SIZE
    food_y = random.randint(min_y, max_y)*SQUARE_SIZE

    food.goto(food_x, food_y)
    food_position = food.pos()
    food_positions.append(food_position)
    new_food_stamp = food.stamp()
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


def init_snake():
    """
    This function initializes the snake, drawing the snake
    """
    for i in range(START_LENGTH):
        snake_position = snake.pos()
        x_pos = snake_position[0] + SQUARE_SIZE #To move the snake forward
        y_pos = snake_position[1] 

        snake.goto(x_pos, y_pos)
        new_stamp()


def up():
    snake.direction = "Up"


def down():
    snake.direction = "Down"


def left():
    snake.direction = "Left"


def right():
    snake.direction = "Right"


# Create listeners for keyboard input
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.listen()


def move_snake():
    """
    This function moves the snake forward, and checks if it has eaten food or if it has hit the wall or itself
    """
    #Move the snake forward
    snake_pos = snake.pos()
    x_pos = snake_pos[0]
    y_pos = snake_pos[1]
    
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)

    elif snake.direction == "Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    elif snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)

    elif snake.direction == "Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)

    new_snake_pos = snake.pos()

    #If snake is on top of food item
    if new_snake_pos in food_positions:
        food_index = food_positions.index(new_snake_pos)
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_positions.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp from the list

    else:
        remove_tail()

    #Check if snake has hit itself
    if new_snake_pos in pos_list:
        print("Your snake ate itself! Game over!")
        quit()

    new_stamp()

    new_x_pos = new_snake_pos[0]
    new_y_pos = new_snake_pos[1]

    #Check if snake has hit the wall
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()

    if new_y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        quit()

    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()

    if new_y_pos >= UP_EDGE:
        print("You hit the top edge! Game over!")
        quit()

    if len(food_stamps) < NUM_FOOD:
        make_food()

    turtle.ontimer(move_snake, TIME_STEP)


def main():
    init_snake()
    move_snake()
    turtle.mainloop()

if __name__ == '__main__':
    main()
