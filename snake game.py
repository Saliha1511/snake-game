import turtle
import random

segment= []

grass=turtle.Screen()
grass.bgpic("grass.gif")
grass.addshape("headfront.gif")
grass.addshape("headdown.gif")
grass.addshape("headright.gif")
grass.addshape("headleft.gif")
grass.addshape("body.gif")

snake=turtle.Turtle()
snake.shape("headfront.gif")
snake.penup()

snake.goto(0,0)
snake.setheading(90)
snake.speed(0)
food=turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(1000)
food.goto(100,10)

pen=turtle.Turtle()
pen.penup()
pen.speed(500)
pen.goto(0,250)
pen.hideturtle()
pen.write("Score:0",font=("Courier",27,"bold"))

def move():
    snake.forward(5)

def up():
    if snake.heading() !=270:
       snake.shape("headfront.gif")
       snake.setheading(90)
def down():
    if snake.heading() != 90:
       snake.shape("headdown.gif")
       snake.setheading(270)
def right():
    if snake.heading() != 180:
       snake.shape("headright.gif")
       snake.setheading(0)
def left():
    if snake.heading() != 0:
       snake.shape("headleft.gif")
       snake.setheading(180)

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")

turtle.listen()
score=0

while True:
    grass.update()
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
       grass.bgpic("game over.gif")
       food.hideturtle()
    for i in segment:
       if i.distance(snake)<1:
           grass.bgpic("game over.gif")
           food.hideturtle()    

    if snake.distance(food)<20:
       x=random.randint(-285,285)
       y=random.randint(-285,285)
       food.setpos(x,y)
       pen.clear()
       score=score+1
       pen.write("Score:{}".format(score),font=("Courier",27,"bold"))
       body=turtle.Turtle()
       body.shape("body.gif")
       body.penup()
       body.speed(0)
       segment.append(body)
    
    for i in range(len(segment)-1,0,-1):
        x=segment[i-1].xcor()
        y=segment[i-1].ycor()
        segment[i].goto(x,y) 
        if  len(segment)>0:
            x=snake.xcor()
            y=snake.ycor()
            segment[0].goto(x-1,y+1)
       
    move()

turtle.done()