import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
exit = False
guessed_states = []

while len(guessed_states) < 50 and exit == False:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Insert a state name!").title()
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    
    if answer_state == "Exit":
        exit = True
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        
screen.exitonclick()