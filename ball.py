import curt0061Library as a
import click
import time

ball =  [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]

x1 = int(input('Enter in x start: '))
y1 = int(input('Enter in y start: '))

vx=5
vy=5
obj = ball
a.displayObject(obj,x1,y1)
hi=1

 #Having trouble determining why it doesn't erase after 1st loop, 
 #I think it's reading as if there are 
 #2 different objects in memory
while hi > 0:   
    a.eraseObject(obj,x1,y1)               
    a.moveObject(obj,x1,y1,vx,vy)
    a.checkCollision(obj,x1,y1,vx,vy,Sx=128,Sy=64)
    time.sleep(2)
    
    


a.bg()

a.displayObject(ball,x1,y1)
a.clearScreen

