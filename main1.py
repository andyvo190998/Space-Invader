from turtle import *
import random

#set up screen
screen = Screen()
screen.title("SPACE INVADER")


score = 0

#Create the player
player = Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
player.left(90)
player.setposition(0,-300)
playerspeed = 15


#Add enemies to the list
num_of_enemies = 5
enemies = []
for i in range(num_of_enemies):
    enemies.append(Turtle())
for enemy in enemies:
    enemy.penup()
    enemy.shapesize(2,2)
    enemy.speed('fast')
    enemy.color("red")
    enemy.shape("turtle")
    x= random.randint(-200,200)
    y= random.randint(100,250)
    enemy.setposition(x,y)
    enemy.right(90)


#Create the player's bullet
bullet = Turtle()
bullet.penup()
bullet.shape("square")
bullet.shapesize(0.5,0.5)
bullet.speed("fast")
bullet.color("black")
bullet.hideturtle()




#Define bullet state
#ready- ready to fire
#fire- bullet is firing
bullet_state = "ready"



#Move the player left and right
def move_left():
    # x = player.xcor()
    # if x <-280:
    #     player
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x=-280
    player.setx(x)
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
        bullet_state = "fire"



#Create keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(fire_bullet, "space")



#Main game loop
enemy_speed = 5
game_is_on = True
while game_is_on == True:
    #Move the enemy
    for enemy in enemies:
        x = enemy.xcor()
        x+=enemy_speed
        enemy.setx(x)
    #Move the enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
                enemy_speed *= -1
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemy_speed *=-1

        if enemy.ycor() < -300 or score == num_of_enemies:
            game_is_on = False
            bullet_state = "ready"




        # check for a collision between bullet and enemy
        if enemy.distance(bullet) < 35:

            enemy.hideturtle()
            enemy.setposition(0,1000)
            score += 1
            print(score)



        #Move the bullet
        if bullet_state == "fire":
            x = bullet.xcor()
            y = bullet.ycor()
            y +=20
            bullet.sety(y)
            if y > 300:
                bullet_state = "ready"
                bullet.hideturtle()


screen.exitonclick()
while True:
    screen.update()
