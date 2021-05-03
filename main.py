import turtle
import pandas


screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []
score = 0
wrong_guess = turtle.Turtle()
wrong_guess.hideturtle()
wrong_guess.penup()

while len(guessed_states) < 50:
    pen = turtle.Turtle()
    pen.up()
    pen.hideturtle()
    user_input = screen.textinput(title=f"{len(guessed_states)}/50 State_name", prompt="Type the state name")
    user_input = user_input.title()

    if user_input == "Exit":
        break

    if user_input in all_states:
        wrong_guess.clear()

        # If the state was already guessed
        if user_input in guessed_states:
            pass
        else:
            guessed_states.append(user_input)
            state_row = states_data[states_data.state == user_input]
            x = float(state_row.x)
            y = float(state_row.y)
            pen.goto(x, y)
            pen.down()
            pen.write(user_input)
    # If the guess is not among the list of states
    else:
        # Removing text written by a turtle -  https://stackoverflow.com/questions/34823206/turtle-delete-writing-on-screen-and-rewrite
        wrong_guess.goto(-40,0)
        wrong_guess.pendown()
        wrong_guess.write("Please try again",font=("Arial",16,"normal"))

for state in guessed_states:
    all_states.remove(state)

missed_states = all_states

# Converting list to a Series since only series and dataframe has to_csv attribute
Learn = pandas.Series(missed_states)
Learn.to_csv("States_to_learn.csv")

screen.exitonclick()
