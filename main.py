from turtle import Turtle, Screen
import random


my_sc = Screen()
my_sc.setup(width=600,height=600)

user_bet = my_sc.textinput("Who will win the race","Your bet:")

blue_turtle=Turtle()
blue_turtle.color("blue")
blue_turtle.shape("turtle")

red_turtle=Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")

purple_turtle=Turtle()
purple_turtle.color("purple")
purple_turtle.shape("turtle")


green_turtle=Turtle()
green_turtle.color("green")
green_turtle.shape("turtle")


black_turtle=Turtle()
black_turtle.color("black")
black_turtle.shape("turtle")

finish_line = Turtle()
finish_line.penup()
finish_line.setx(250)
finish_line.sety(300)
finish_line.right(90)
finish_line.pendown()
finish_line.forward(600)

contestants = [red_turtle,green_turtle,black_turtle,blue_turtle,purple_turtle]

x = -250
y = 200
for contestant in contestants:
    contestant.penup()
    contestant.setx(x)
    contestant.sety(y)
    y-=100


game_on=True
while game_on:
    for contestant in contestants:
        contestant.forward(random.randint(1,50))
        if contestant.xcor() >= finish_line.xcor():
            winner = contestant.pencolor()
            print(f"{contestant.pencolor()} wins")
            game_on=False
            break

if user_bet.lower()==winner.lower():
    print(f"{winner} won the race! Congratulations")
else:
    print(f"You made a bet on {user_bet} but the winner is {winner}. You LOST! ")


my_sc.exitonclick()