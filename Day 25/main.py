import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("USA States Game")
image = "100 days of python\\Day 25\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("100 days of python\\Day 25\\states.csv")
state_list = df.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guessed", prompt="What's another state's name? ").title()
    
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("100 days of python\\Day 25\\states_to_learn.csv")
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        pos_state = df[df.state == answer_state]
        t.goto(int(pos_state.x), int(pos_state.y))
        t.write(pos_state.state.item())     #or answer_state


screen.exitonclick()
