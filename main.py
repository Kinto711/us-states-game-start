import csv
from turtle import Turtle, Screen
import pandas

turtle = Turtle()
# turtle1 = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# turtle1.hideturtle()
# turtle1.penup()


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()



# data = pandas.read_csv("50_states.csv")
is_on = True
user_input_list = []
score = 0
while score < 50:
    user_input = screen.textinput(f"{len(user_input_list)}/50 States Correct", "Type a State name:").capitalize()

    if user_input not in user_input_list:
        if user_input in all_states:
            turtle1 = Turtle()
            turtle1.hideturtle()
            turtle1.penup()
            state_data = data[data.state == user_input]
            turtle1.goto(int(state_data.x), int(state_data.y))
            turtle1.write(user_input)
            user_input_list.append(user_input)
#     score = 0
#     user_input_list = []
#     user_input = screen.textinput(f"{str(score)}/50 States Correct", "Type a State name:").capitalize()
#     with open("50_states.csv") as data_file:
#         data = csv.reader(data_file)
#         for row in data:
#             if row[0] != "state":
#                 if row[0] == user_input:
#                     if row[0] in user_input_list:
#                         pass
#                     else:
#                         turtle1.goto(int(row[1]), int(row[2]))
#                         turtle1.write(user_input, False, align="center", font=('Arial', 25, 'normal'))
#                         user_input_list.append(row[0])
#         score += 1
#         print(score)


screen.exitonclick()
# dicta = csv.reader(data)
#
# states = data["state"]
#
#
#
# print(dicta)