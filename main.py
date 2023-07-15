import turtle
import pandas

screen = turtle.Screen()
state_loc = turtle.Turtle()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# reading states list
states = pandas.read_csv("50_states.csv")
list_states = states["state"].tolist()
correct_guess_list = []

is_on = True
while is_on:

    def score_track():
        if len(correct_guess_list) == 0:
            return screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
        else:
            return screen.textinput(title=f"{len(correct_guess_list)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    answer_state = score_track()

    # guess states - x and y coordinates
    if answer_state in list_states and answer_state not in correct_guess_list:
        guess_state = states[states.state == answer_state]
        x_cor_state = int(guess_state.x)
        y_cor_state = int(guess_state.y)

        correct_guess_list.append(answer_state)
        state_loc.penup()
        state_loc.hideturtle()
        state_loc.goto(x_cor_state,y_cor_state)
        state_loc.write(arg=f"{answer_state}",align="center",font=("Arial", 10, "normal"))

    elif len(correct_guess_list) == 50:
        is_on = False

    elif answer_state == "Exit":
        break

    else:
        score_track()

