#!usr/bin/env python3

# Space invaders

import turtle
import math
turtle.fd(0)
turtle.speed(0) # maximize drawing speed
turtle.ht() # Hide turtle 
turtle.setundobuffer(1)
turtle.tracer(1)
import os

# Set up the main window
# Screen size
screenWidth = 600
screenHeight = 600

wn = turtle.Screen()
wn.bgcolor('black')

wn.title('Space Invaders')

# Draw border around window
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

# Create player
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setheading(90) # rotate 90 degrees

player.setposition(0,-250)
player.width = 30

playerSpeed = 15

# Move player left and right

def moveLeft(player,screenWidth,playerSpeed):
    player.setx(*[player.xcor()-playerSpeed if player.xcor() >-screenWidth/2.0+player.width/2.0 else player.xcor()])

def moveRight(player,screenWidth,playerSpeed):
    player.setx(*[player.xcor()+playerSpeed if player.xcor() <screenWidth/2.0-player.width/2.0 else player.xcor()])

# Create player weapon

bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bullet.state = 'ready' # 'ready' to fire or 'fire'
bulletSpeed = -25

def fireBullet(player,bulletSpeed,bullet):
    if bullet.state == 'ready':
        bullet.setx(player.xcor())
        bullet.sety(player.ycor())
        bullet.state = 'fire'
        bullet.showturtle()
    


# Create enemy

enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, -250)

enemy.width = 15

enemySpeed = 2

# Keyboard binding
turtle.listen()
turtle.onkey(lambda:moveLeft(player,screenWidth,playerSpeed), 'a')
turtle.onkey(lambda:moveLeft(player,screenWidth,playerSpeed), 'Left')
turtle.onkey(lambda:moveRight(player,screenWidth,playerSpeed), 'd')
turtle.onkey(lambda:moveRight(player,screenWidth,playerSpeed), 'Right')
turtle.onkey(lambda:fireBullet(player,bulletSpeed,bullet), 'space')

def collission(obj1, obj2, minDistance = 1):
    vectorBetween = [obj1.xcor()-obj2.xcor(),obj1.ycor()-obj2.ycor()]
    distance = math.sqrt(vectorBetween[0]**2+vectorBetween[1]**2)
    return distance<minDistance

# main Game loop 

while True:
    #Move enemy 
    x = enemy.xcor()
    x += enemySpeed
    if x > screenWidth/2.0-player.width/2.0 or x <-screenWidth/2.0+enemy.width/2.0:
        enemySpeed*=-1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        if y<-screenHeight/2.0+enemy.width/2.0:
            print('Game OVER!')
            break
    enemy.setx(x)

    if bullet.state == 'fire':
        y = bullet.ycor()-bulletSpeed
        if y>screenHight/2.0:
            bullet.state = 'ready'
            bullet.hideturtle()
        bullet.sety(y)

        if collission(bullet,enemy,minDistance=15):
            bullet.state = 'ready'
            bullet.hideturtle()
            enemy.hideturtle()
        




delay = input("Press enter key to finish")