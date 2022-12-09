from turtle import *
from aliens import Aliens
from threading import Thread

player = Turtle()
player.hideturtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0,-300)
player.showturtle()
player.left(90)
x = -150
x_second_row = -150

aliens = []
aliens_second_row = []

# alien1 = Aliens()
# print(alien1.aliens_second_row)

def go_left():
    x = player.xcor()
    if x >= -300:
        player.goto(x-40,-300)

def go_right():
    x = player.xcor()
    if x <= 300:
        player.goto(x+40,-300)




screen = Screen()
screen.onkey(go_left,"Left")
screen.onkey(go_right,"Right")

for i in range(0,6):
    alien = Turtle()
    alien.speed("fast")
    aliens.append(alien)
    alien.shape("turtle")
    alien.color('red')
    alien.penup()
    alien.right(90)
    x += 40
    alien.goto(x, 300)


for i in range(0,6):
    alien = Turtle()
    alien.speed("fast")
    aliens_second_row.append(alien)
    alien.shape("turtle")
    alien.color('red')
    alien.penup()
    alien.right(90)
    x_second_row += 40
    alien.goto(x_second_row, 250)



def alien_go_right():
    alien_automove = True
    while alien_automove == True:
        for i in aliens:
            if aliens[5].xcor() <= 280:
                i.goto(i.xcor() + 20 ,300)
            else:
                alien_go_left()
        for i in aliens_second_row:
            if aliens_second_row[5].xcor() <= 280:
                i.goto(i.xcor() + 20 ,250)
            else:
                alien_go_left()
    # alien_go_left()
def alien_go_left():
    alien_automove = True
    while alien_automove == True:
        for i in aliens:
            if i.xcor() >= -280:
                i.goto(i.xcor() - 20 ,300)
            else:
                alien_go_right()
        for i in aliens_second_row:
            if i.xcor() >= -280:
                i.goto(i.xcor() - 20 ,250)
            else:
                alien_go_right()
score = 0
def fire():
    fire = Turtle()
    fire.hideturtle()
    fire.speed("fast")
    fire.shape("turtle")
    fire.color('black')
    fire.penup()
    fire.left(90)
    fire.goto(player.xcor(), -300)
    fire.showturtle()
    x = fire.xcor()
    y = fire.ycor()
    global score
    while fire.ycor() < 380:
        fire.goto(x,fire.ycor() + 20)
        for i in aliens_second_row:
            if i.distance(fire) < 15:
                score+=1
                # print(aliens_second_row.index(i))
                fire.hideturtle()
                i.hideturtle()
                if score == 4:
                    print("win")

t1 = Thread(target=alien_go_left)
t2 = Thread(target=fire)

screen.ontimer(alien_go_left,10)
# t1.start()
# t2.start()


# def on_fire():
#     t2.start()
screen.onkey(fire,"space")

screen.listen()

screen.update()
screen.exitonclick()
