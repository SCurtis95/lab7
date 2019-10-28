##Curt0061 Library
##Student ID 040862744
import time
from gfxhat import lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

def clearScreen():
    lcd.clear()
    lcd.show

def clearBacklight():
    lcd.clear()
    backlight.set_all(255,255, 255)
    time.sleep (2) 

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 38)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

def getVertical():
    x=20
    
    for y in range(0,127,1):
        lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(3)
    lcd.clear()


def getHorizontal(y):
    y=34
    for x in range(0,63,1):
        lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(3)
    lcd.clear()
 

def getStaircase(width, height):
    x = 45
    y = 34
    lcd.set_pixel(x,y,1)
    for x in range (0,63):
        width = x + 1
        lcd.set_pixel(x,y,1)
        height = y + 1
        lcd.set_pixel(x,y,1)
    lcd.show() 

def getDisplay(random):
    x = random.randint(1,127)
    y = random.randint(1,63)
    lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(4)
    lcd.clear()
    

def bg():
    r=15
    g=167
    b=194
    backlight.set_all(r,g,b)
    backlight.show()

def displayObject(obj,x1,y1):
    
    if (y1 + len(obj)) > 63:
        y1 = 63 - len(obj[0])

    if (x1 + len(obj)) > 127:
        x1 = 127 - len(obj[0])
    

    for i in range(0,len(obj)):
        for j in range(0,len(obj[i])):
            lcd.set_pixel(x1+i, y1+j,obj[i][j])        
            lcd.show()
        time.sleep(0.5)

##Lab 7

def eraseObject(obj,x1,y1):

    if (y1 + len(obj)) > 63:
        y1 = 63 - len(obj[0])

    if (x1 + len(obj)) > 127:
        x1 = 127 - len(obj[0])

    for i in range(0,len(obj)):
        for j in range(0,len(obj[i])):
            lcd.set_pixel(x1+i, y1+j,0)    
        lcd.show()     
    time.sleep(0.5)


def moveObject(obj,x1,y1,vx,vy):
    
    x1 = (x1+vx)
    y1 = (y1+vy)
    displayObject(obj,x1,y1)
    


def checkCollision(obj,x1,y1,vx,vy,Sx=128,Sy=64):
    w=8
    h=8
    if y1<0:
        y1=0
    if y1+h>Sy:
        y1=Sy-h
    if x1<0:
        x1=0
    if x1+w>Sx:
        x1=Sx-w
    else:
        pass

