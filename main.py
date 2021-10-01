import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen = turtle.Screen()
screen.tracer(0)

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
x = data["x"].to_list()
y = data["y"].to_list()
# print(states)

answer_lst = []
while len(answer_lst) < 50:
    answer_state = screen.textinput(title=f"{len(answer_lst)}/50 Guess the state",
                                    prompt="what's another state name?").title()
    for _ in states:
        if answer_state == "Exit":
            missing_states = [missing for missing in states if missing not in answer_lst]
            missed_states_dict = {
                "Missed States": missing_states
            }
            missed_states_data = pd.DataFrame(missed_states_dict)
            missed_states_data.to_csv("states_to_learn.csv")
            exit()
        elif _ == answer_state:
            answer_lst.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            index_of_state = states.index(_)
            x_cor, y_cor = x[index_of_state], y[index_of_state]
            turtle.setposition(x_cor, y_cor)
            turtle.write(f"{answer_state}", align="right", font=('Arial', 12, 'bold'))
            # print(x_cor, y_cor)
screen.exitonclick()
