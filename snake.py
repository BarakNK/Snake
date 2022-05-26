import turtle
import random

turtle.bgcolor("black")
turtle.tracer(1,0) #This helps the turtle move more smoothly
turtle.penup()
turtle.hideturtle()

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

SQUARE_SIZE = 20
START_LENGTH = 8
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Creating the snake
snake = turtle.clone()
snake.shape("square")
snake.color("turquoise")
snake.direction = "Up"

def main():
    pass

if __name__ == '__main__':
    main()
