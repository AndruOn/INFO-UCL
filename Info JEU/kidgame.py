import turtle as turtle
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("green")
#wn.bgpic("IMAGEEE")
wn.tracer(3)

#Initiate score
score=0

#Draw border
mypen= turtle.Turtle()
mypen.penup()
mypen.speed(0)
mypen.setposition(-300,-300)
mypen.fillcolor("black")
mypen.begin_fill()
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.end_fill()
mypen.hideturtle()

#Create player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0) #vitesse d'animation (0 c le max)

#Create multiple goals
maxgoals=6
goals=[]
for count in range(maxgoals):       
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300),random.randint(-300,300))



#Initiate

#Set speed
speed = 1

#Define functions

def turnleft():
    player.left(30)

def turnright():
    player.right(30)
    
def increasespeed():
    global speed
    speed+=1

def decreasespeed():
    global speed
    speed-=1
    
def inCollision(a,b):
    d= math.sqrt( math.pow(a.xcor()-b.xcor(),2) + math.pow(a.ycor()-b.ycor(),2))
    if d< 15:
        return True
    return False
def closewn():
    global wn
    wn.bye()
    
#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
turtle.onkey(decreasespeed,"Down")
turtle.onkey(closewn,"space")

while score < 7:
    player.forward(speed)
    
    #Boundary Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        
    for count in range(len(goals)):
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
        
    #Collision checking
        if inCollision(player,goals[count]):
            goals[count].setposition(random.randint(-300,300),random.randint(-300,300))
            goals[count].right(random.randint(0,360))
            score += 1
            #Draw the score
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290,310)
            scorestring = "Score: %s" %score
            mypen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
            
    #Move the goal around:
        goals[count].forward(3)

mypen.undo()
mypen.write("CONGRATULATION ! You've won. Press Space to quit",False,align="left",font=("Arial",14,"bold"))
wn.mainloop()


