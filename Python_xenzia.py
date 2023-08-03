from tkinter import *
import random

game_width = 700
game_height = 600
speed = 40
space = 20
body_part = 3
snake_color = "blue"
food_color = "red"
background_color = "black"


class Food:
    def __init__(self):
        x = random.randint(0, (game_width/space)-1)*space
        y = random.randint(0, (game_height/space)-1)*space

        self.coordinates = [x, y]

        can.create_oval(x, y, x+space, y+space, fill=food_color, tag="food")


class Snake:
    def __init__(self):
        self.body_size = body_part
        self.coordinates = []
        self.squares = []

        for snake in range(0, body_part):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = can.create_rectangle(
                x, y, x+space, y + space, fill=snake_color, tag="snake")
            self.squares.append(square)


def next_direction(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= space
    elif direction == "down":
        y += space
    elif direction == "left":
        x -= space
    elif direction == "right":
        x += space

    snake.coordinates.insert(0, (x, y))
    square = can.create_rectangle(x, y, x+space, y + space, fill=snake_color)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score: {score}")

        can.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        can.delete(snake.squares[-1])
        del snake.squares[-1]

    if touched(snake):
        game_over()
    else:
        window.after(speed, next_direction, snake, food)


def change_direction(new_direction):
    global direction
    if new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "left":
        if direction != "right":
            direction = new_direction


def touched(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= game_width:
        return True
    elif y < 0 or y >= game_height:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def game_over():
    can.create_text(can.winfo_width()/2, can.winfo_height()/2,
                    font=("Ink Free", 33), text="Game over", fill="red")
    frame.pack_forget()


window = Tk()
window.title("Python Xenzia --(Murad)--")
window.resizable(False, False)

direction = "down"
score = 0

label = Label(window,
              text=f"Score: {score}",
              font=("Ink Free", 33))
label.pack()

can = Canvas(window, bg=background_color, width=game_width, height=game_height)
can.pack()

frame = Frame(window)
frame.pack()

Button(frame, text="↑", command=lambda:  change_direction("up")).pack(side=TOP)
Button(frame, text="←", command=lambda:  change_direction("left")).pack(side=LEFT)
Button(frame, text="↓", command=lambda:  change_direction("down")).pack(side=LEFT)
Button(frame, text="→", command=lambda: change_direction("right")).pack(side=LEFT)

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_direction(snake, food)
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_width/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
