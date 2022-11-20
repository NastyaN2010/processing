x =1
def setup():
    size(600,400)
def draw():
    global x,y
    background(100)
    line(300,100,300,200)
    line(200,200,400,200)
    line(300,200,250,300)
    line(300,200,350,300)
    strokeWeight(x)
    x += 5  
    
