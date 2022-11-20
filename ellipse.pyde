x =10
y =10
def setup():
    size(800,800)
def draw():
    global x,y
    background(100)
    ellipse(400,400,x,y)
    x += 5 # это тоже самое,что и x = x - 5 
    y += 5
