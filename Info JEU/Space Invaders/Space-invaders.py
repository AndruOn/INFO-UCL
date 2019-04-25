#---------------------------------------------------------------
# SPACE INVADERS
# Andru Onciul
# 10/03/2018
# Use the arrows to move and
# Press Space to fire
#---------------------------------------------------------------
import turtle as turtle
import math
import random
import winsound
import time


#Variables
playerspeed = 15
invaderspeed = 8
invaderdownspeed = 40
bulletspeed = 25
maxscore= 100
maxlives= 3
score= 0

#Ask to begin or not
wanttoplay=True
hasntlost=True
ingame=False

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Space Invaders")
wn.bgpic("background1.gif")
#wn.tracer(3)

#Register shapes for turtles
turtle.register_shape("invader (1).gif")
turtle.register_shape("player.gif")
turtle.register_shape("heart_noback.gif")
turtle.register_shape("minivaisseau.gif")
turtle.register_shape("insecte1.gif")

#Draw border
mypen= turtle.Turtle()
mypen.penup()
mypen.color("white")
mypen.speed(0)
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)

mypen.hideturtle()

#Draw title
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(0,310)
scorestr="SPACE INVADERS"
score_pen.write(scorestr,False,align="center",font=("Arial black",14,"bold"))
score_pen.hideturtle()

#Functions
import msvcrt as m
def wait():
    m.getch()
    
def move_left():
    if ingame==True:
        x = player.xcor()
        x-= playerspeed
        if x < -280:
            x=280
        player.setx(x)
    
def move_right():
    if ingame==True:
        x = player.xcor()
        x+= playerspeed
        if x > 280:
            x=280
        player.setx(x)
    
def closewn():
    global wn
    wn.bye()
    
def fire():
    global bulletstate
    for i in range(len(bullets)):
        if bulletstate[i]== "ready" and ingame==True:
            laser()
            bulletstate[i]= "fire"
            x= player.xcor()
            y= player.ycor() + 10
            bullets[i].setposition(x,y)
            bullets[i].showturtle()
            break

def inCollision(a,b):
    d= math.sqrt( math.pow(a.xcor()-b.xcor(),2) + math.pow(a.ycor()-b.ycor(),2))
    if d< 15:
        return True
    return False
    
def laser():
    winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
    
def explosion():
    winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)

def play():
    global wanttoplay
    global hasntlost
    wanttoplay=True
    hasntlost=True
    
def replay():
    global wanttoplay
    global hasntlost
    wanttoplay=True
    hasntlost=True
    
#Set keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire,"space")
turtle.onkey(closewn,"Escape")
turtle.onkey(replay,"r")
turtle.onkey(play,"p")

#Create score pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()

#Create player
player = turtle.Turtle()
player.color("blue")
player.shape("minivaisseau.gif")
player.penup()
player.speed(0) #vitesse d'animation (0 c le max)
player.setposition(0,-250)
player.setheading(90)
player.hideturtle()

#Create player bullets
bullets=[]
bulletstate=[]
for i in range(5):
    bullet=turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5,0.5)
    bullet.setposition(0,310) #hors de la carte pour pas quelle detruise un vaisseau sans que je tire
    bullet.hideturtle()
    bullets.append(bullet)
    bulletstate.append("ready")
        #Define bullet state
        #ready - ready to fire
        #fire - th bullet is firing


#Create multiple ennemies
maxinvaders= 6
invaders=[]
for count in range(maxinvaders):       
    invaders.append(turtle.Turtle())
    invaders[count].hideturtle()
for invader in invaders:
    invader.color("red")
    invader.shape("insecte1.gif")
    invader.penup()
    invader.speed(0)
    x= random.randint(-200,200)
    y= random.randint(100,250)
    invader.setposition(x,y)
    
#Create live turtle
hearts=[]
for i in range(maxlives):
    heart=turtle.Turtle()
    heart.hideturtle()
    heart.speed(3)
    heart.shape("heart_noback.gif")
    heart.penup()
    heart.setposition(200 + i*35,270)
    hearts.append(heart)


#----------------------------------------------------------------------------------------------------
#Now the main loop that will play the game
#----------------------------------------------------------------------------------------------------



#MAIN LOOP
while True:
    #Write Begining text
    score_pen.clear()
    score_pen.setposition(0,0)
    score_pen.write("ARE YOU READY ?",False,align="center",font=("Arial black",20,"bold"))
    score_pen.setposition(0,-30)
    score_pen.write("Press P to launch the game",False,align="center",font=("Arial",15,"normal"))
    score_pen.setposition(0,-50)
    score_pen.write("Use the arrows to move and fire with Space",False,align="center",font=("Arial",15,"normal"))
    score_pen.hideturtle()

    #Wait for player to press P
    wanttoplay=False
    while True:
        t=turtle.Turtle()
        y= t.ycor()+1     #il se passe qlqch en fond/background pour que ce soit pas un bouble instantannée et qu'il ait le temps de capter
        t.sety(y)         #qd utilisateur clique sur p
        if wanttoplay == True:
            break
        
    #Make all turtles visibles for begining of the match
    player.showturtle()
    for invader in invaders:
        invader.showturtle()
        x= random.randint(-200,200)
        y= random.randint(100,250)
        invader.setposition(x,y)
        
    #Draw score
    score_pen.clear()
    score_pen.setposition(-290,270)
    scorestr="Score: %s" %score
    score_pen.write(scorestr,False,align="left",font=("Arial",14,"normal"))
    score_pen.hideturtle()

    #Drawn number of lifes
    for heart in hearts:
        heart.showturtle()

    #The Game can now begin
    ingame = True
    print("begin game")
    score=0
    lives=maxlives
    
    #Now lets make everything move
    while score < maxscore and hasntlost==True:
        for i in range(len(bullets)):
            for invader in invaders:
                #move invaders
                x= invader.xcor()
                x+= invaderspeed
                invader.setx(x)
                #move invaders down
                if invader.xcor() > 280:
                    #Move all ennemies down
                    for inv in invaders:
                        y= inv.ycor()
                        y-= invaderdownspeed
                        inv.sety(y)
                    #Change all ennemies direction
                    invaderspeed *= -1

                if invader.xcor() < -280:
                    for inv in invaders:    
                        y= inv.ycor()
                        y-= invaderdownspeed
                        inv.sety(y)
                    invaderspeed *= -1
                    
                #Check collision bullet/invader
                if inCollision(bullets[i],invader):
                    explosion()
                    bullets[i].hideturtle()
                    bulletstate[i]= "ready"
                    bullets[i].setposition(0,-400)
                    #reset. ennemis
                    x= random.randint(-200,200)
                    y= random.randint(100,250)
                    invader.setposition(x,y)
                    #Change score
                    score+=100
                    score_pen.setposition(-290,270)
                    scorestr="Score: %s" %score
                    score_pen.clear()
                    score_pen.write(scorestr,False,align="left",font=("Arial",14,"normal"))
                    score_pen.hideturtle()
                #Lose a life
                if inCollision(player,invader):
                    explosion()
                    lives -=1
                    #Reset ennemi
                    x= random.randint(-200,200)
                    y= random.randint(100,250)
                    invader.setposition(x,y)
                    #Write remaining lives
                    hearts[lives].hideturtle()
                    if lives == 0:
                        hasntlost=False
                        break
                #Respawn ennemies if they go too low
                if invader.ycor() < -290:
                    x= random.randint(-200,200)
                    y= random.randint(100,250)
                    invader.setposition(x,y)
                
            #Move the bullet
            if bulletstate[i] == "fire":
                y= bullets[i].ycor()
                y+= bulletspeed
                bullets[i].sety(y)
            #Check bullet in borders
            if bullets[i].ycor() > 280:
                bullets[i].hideturtle()
                bulletstate[i]="ready"
        
    ingame=False
    
    #Hide the turtles
    player.hideturtle()
    for invader in invaders:
        invader.hideturtle()
    bullet.hideturtle()
    
    #Draw the appropriate finale message
    if score == maxscore:
        score_pen.setposition(0,0)
        score_pen.write("YOU WON",False,align="center",font=("Arial black",20,"bold"))
        score_pen.setposition(0,-30)
        score_pen.write("Press Escape to exit the game or Press R to retry",False,align="center",font=("Arial",14,"normal"))
        score_pen.hideturtle()
    elif lives == 0:
        score_pen.setposition(0,0)
        score_pen.write("GAME OVER",False,align="center",font=("Arial black",20,"bold"))
        score_pen.setposition(0,-30)
        score_pen.write("Press Escape to exit the game or Press R to retry",False,align="center",font=("Arial",14,"normal"))
        score_pen.hideturtle()
        
    #Wait for player answer
    wanttoplay= False
    while True:
        bullet.sety(310)
        y= bullet.ycor()+1     #il se passe qlqch en fond pour que ce soit pas un bouble instantannée et qu'il ait le temps de capter
        bullet.sety(y)         #qd utilisateur clique sur p
        if wanttoplay == True:
            break
    
        
wn.mainloop()
