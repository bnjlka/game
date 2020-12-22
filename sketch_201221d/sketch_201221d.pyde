width=640
height=400
x=width/2
y=height/2
rectSize=100
speedX=random(3,5)
speedY=random(3,5)
diam=10
rectsize=200
def setup():
    
              size(width, height)
              fill (0,255,0)

def draw():
    global x,y,speedX,speedY
    background(0)
    ellipse(x, y, diam, diam)
    rect(0,0,20,height)
    rect(width-30, mouseY-rectSize/2, 10, rectSize)
    x=x+speedX
    y=y+speedY
    
    if(x>width-30 and x<width-20 and y>mouseY-rectsize/2 and y<mouseY+rectsize/2):
            speedX=speedX*(-1)
    if(x<25):
            speedX=speedX*(-1.1)
            speedY=speedY*(-1.1)
            x=x+speedX
    if(y>height or y<0):
        speedY=speedY*(-1)
    if(x>width):
        background(255,0,0)
        fill(0,255,0)
        textSize(70)
        text("Try again!", width/4, height/2)
def mousePressed():
    global x,y,speedX,speedY
    x=width/2
    y=height/2

    speedX=random(3,5)
    speedY=random(3,5)
            
        
