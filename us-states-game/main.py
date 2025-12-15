import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.bgcolor("#f4f4f2")

map_image = "blank_states_img.gif"
screen.addshape(map_image)
turtle.shape(map_image)

states_df = pandas.read_csv("50_states.csv")
state_names = states_df["state"].to_list()
# x_coords = states_df["x"].to_list()
# y_coords = states_df["y"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Guess a state name:"
    ).title()

    if answer == "Exit":
        missing_states = [state for state in state_names if state not in guessed_states]
        missing_df = pandas.DataFrame(missing_states)
        missing_df.to_csv("states_to_learn.csv")
        break

    if (answer in state_names) and (answer not in guessed_states):
        guessed_states.append(answer)

        # index_no = state_names.index(answer)
        # x_pos = x_coords[index_no]
        # y_pos = y_coords[index_no]

        state_row = states_df[states_df.state == answer]
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.color("#37474f")
        # marker.goto(x_pos, y_pos)
        marker.goto(state_row.x.item(), state_row.y.item())
        marker.write(answer)


