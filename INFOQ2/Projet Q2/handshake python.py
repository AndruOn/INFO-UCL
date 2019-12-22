import turtle as turtle
import time
import numpy as np
from serial import Serial
from color import palette_de_couleurs
import matplotlib.pyplot as plt


############## Setting the variables ############################################################################################################################################

maxcount= 1000
nb_of_captors= 1
total_squares= 9
port = Serial('COM3', 115200, timeout=10)
nb_dif_colors= 10
colors= palette_de_couleurs(nb_dif_colors)

############## Set up the screen ############################################################################################################################################

wn = turtle.Screen()
wn.bgcolor("white")
wn.colormode(255)
wn.screensize()
wn.setup(width = 1.0, height = 1.0)

############## Grading scale visual ################################################################################################################################################

## Grading scale size
legend_start=(-550,310)
legend_length=1100

## Creating the turtles for grading
for i in range(nb_dif_colors):
    t=turtle.Turtle()
    t.penup()
    t.speed(0)
    t.shape("square")
    t.shapesize(3,3)
    t.color(colors[i])
    t.setposition(legend_start[0]+30 + (legend_length/len(colors))*(i) ,legend_start[1]+57)
    
## Write the values of grading
volt_values=["0 V","1 V","2 V","3 V","4 V","5 V"]
mypen=turtle.Turtle()
mypen.speed(0)
mypen.penup()
mypen.setposition(legend_start)
for i in range(6):
    mypen.write(volt_values[i],False,align="center",font=("Arial black",12,"normal"))
    mypen.forward((legend_length+40)/5)
mypen.hideturtle()

############## Functions ##########################################################################################################################################################

## Defining the color changing function
def color_turtle(nb,t):
    """ Input: Takes in a number that corresponds to a color and a turtle
        Function: Changes the color of that turtle
        """

    if nb == None:
        print("Incorrect value for voltage" )
    elif 0<=nb<=5000:
        t.color(colors[nb * len(colors)//5000])   
    
## Function that reads values from port
def get_reading(port):
    """Reads value on port. Each space(" ") means a new value begins.
        """
    number=""
    while(port.inWaiting() != 0):
        byte=port.read() #on lit un caractère
        car=str(byte)[2:-1]
        if car!= " ":
            number+= car
        else:
            return int(number)

############## Setting up the changing color squares ##############################################################################################################################
        
## Creating the turtles that will change colors
t1=turtle.Turtle()
t1.penup()
t1.shape("square")
t1.shapesize(15,15)
t1.color("red")
t1.setposition(-250,0)

t2=turtle.Turtle()
t2.penup()
t2.shape("square")
t2.shapesize(15,15)
t2.color("red")
t2.setposition(250,0)

## Writing theirs names
mypen.setposition(-250,-190)
mypen.write("A0",False,align="center",font=("Arial black",16,"bold"))
mypen.setposition(255,-190)
mypen.write("A1",False,align="center",font=("Arial black",16,"bold"))

############## MAIN LOOP ##########################################################################################################################################################

## Loop that changes the colors of the turtle
start=time.time()

l0=np.zeros(maxcount)
l1=np.zeros(maxcount)
count=0
while count < maxcount:
    port.write(b'K')
    voltage1= get_reading(port)
    color_turtle(voltage1,t1)
    voltage2= get_reading(port)
    color_turtle(voltage2,t2)
    
    """
    print("A1= ",voltage2,"  A0= ",voltage1,"  count= ",count)
    """
    l0[count]=voltage1
    l1[count]=voltage2
    
    count+=1


end=time.time()

############## Print messages ##########################################################################################################################################################

## Print perfomance
print("-"*35,"Program performance","-"*35)
total_time= end-start
print("Time for program: %ss" % (total_time)," for %s refreshes" % maxcount)
time_per_refresh= (total_time)/maxcount
print("Time per refresh: %ss" % (time_per_refresh) )
print("-"*91)

############## Plotting ##########################################################################################################################################################

x=np.arange(0,maxcount,1)
plt.plot(x,l0,'red',label="A0 voltage")
plt.plot(x,l1,'blue',label="A1 voltage")
plt.ylabel("milliVolt (mV)")
plt.legend()

plt.show()



#wn.mainloop()