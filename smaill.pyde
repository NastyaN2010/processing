x = 10
z = 10
def setup():
    size(600,400)
def draw():
    global x,z
    ellipse(150,150,100,100)
    ellipse(135,140,15,15)
    ellipse(165,140,15,15)
    ellipse(150,166,10,10)
    x = x - 1
    z = z + 1
    
