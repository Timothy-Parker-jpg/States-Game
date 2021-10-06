import turtle
import pandas as pd
import random
def write_state():
    write_object.color("Black")
    write_object.hideturtle()
    write_object.penup()
    write_object.goto(int(data.x[data.state == ans]), int(data.y[data.state == ans]))
    write_object.pendown()
    write_object.write(f"{ans.capitalize()}")

data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.bgpic("blank_states_img.gif")

write_object = turtle.Turtle()
correct = []
game_is_on = True
while game_is_on:
    ans = screen.textinput(f"{len(correct)}/50", "Name a state: ").title()
    if ans in correct:
        continue
    else:
        try:
            for i in data.state:
                if ans == i:
                    write_state()
                    correct.append(ans)
        except:
            continue


screen.exitonclick()
