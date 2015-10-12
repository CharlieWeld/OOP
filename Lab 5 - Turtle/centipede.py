__author__ = 'C06574343'

from turtle import *

def centipede(length, step, life):
    penup() #Stops the tail of the centipede
    theta = 1 #angle to turn in degrees
    dtheta = 1 #Amount in degrees to add to the angle of the centipede
    stamp() #Mark where the centipede starts
    speed(0) #Set the speed of the centipede
    theta = 0
    for i in range(life): #This is the number of times to draw body part
        forward(step) #Number of pixels to move forward in current direction
        stamp()

        
        #left(theta)
        #theta += dtheta
        stamp() #Draw another part on screen at the new forward location and direction
        print("x: ", xcor(), "y:", ycor())
        if(xcor() > 280):
            spd = 9
            speed(spd)
            if spd > 0:
                spd -= 1
        
        if(xcor() > 350):
       
            if theta < 13:
                theta += 1
                left(theta)
            
        
        
        if i > length: #When it gets to its predetermined length clear a part at the end
            clearstamps(1)
        #if theta > 10 or theta < -10: #When the angle becomes greater than 10 invert the angle (+ to -)
         #   dtheta = -dtheta
        #if ycor() > 350: #if the y coordinate becomes greater than 350 turn left 30 degrees
         #   left(30)


def main():
    setworldcoordinates(-100, -100, 500, 500) #Set the starting position of centipede and size of the world
    centipede(9, 5, 100)
    exitonclick()

main()

#Q2. length determines how many body parts will be drawn before first step is removed.
#once the length has been reached one new part will be drawn and one will be deleted

#(ii) step: how far forward it will move on each iteration
#(iii) life: how many iterations of the loop to go through
#(iv) dtheta: increments the angle each loop and inverts the angle when the angle reaches 10 (eg. +10 to -10
#(v) if the y coordinate reaches 350 (height reaches 350) the centipede will increase the angle to the left by 30 degrees
#(vi) when the angle turning gets to 10 or -10 invert it

#Q3. (i): centipede will keep growing
#(ii) the angle it turns will keep increasing
#(iii) when the y coordinate reaches 350 the centipede will not increase its turn and hit the boundary(assuming bound=400)
#
