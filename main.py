#!usr/bin/env python3

# Space invaders

import turtle

turtle.fd(0)
turtle.speed(0) # maximize drawing speed
turtle.ht() # Hide turtle 
turtle.setundobuffer(1)
turtle.tracer(1)
import os

# Set up the main window
# Screen size
screenWidth = 600
screenHight = 600

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

playerspeed = 15
# Move player left and right

def moveLeft(player,screenWidth):
    player.setx(*[player.xcor()-playerspeed if player.xcor() >-screenWidth/2.0+player.width/2.0 else player.xcor()])

def moveRight(player,screenWidth):
    player.setx(*[player.xcor()+playerspeed if player.xcor() <screenWidth/2.0-player.width/2.0 else player.xcor()])

# Keyboard binding
turtle.listen()
turtle.onkey(lambda:moveLeft(player,screenWidth), 'a')
turtle.onkey(lambda:moveRight(player,screenWidth), 'd')


delay = input("Press enter key to finish")