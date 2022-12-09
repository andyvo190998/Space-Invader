from turtle import *

class Aliens:
    def __init__(self):
        self.aliens = []
        self.aliens_second_row = []
        self.create_aliens()
        self.x = 0
        self.x_second_row = 0

    def create_aliens(self):
        for i in range(0,6):
            alien = Turtle()
            alien.speed("fast")
            self.aliens.append(alien)
            alien.shape("turtle")
            alien.color('red')
            alien.penup()
            alien.right(90)
            self.x = self.x + 40
            alien.goto(self.x, 300)
        for i in range(0,6):
            alien = Turtle()
            alien.speed("fast")
            self.aliens_second_row.append(alien)
            alien.shape("turtle")
            alien.color('red')
            alien.penup()
            alien.right(90)
            self.x_second_row += 40
            alien.goto(self.x_second_row, 250)