x = 200
z = 250
def setup():
    size(600,400)
def draw():
    global z,x
    background(135,206,235)
    line(1,250,600,250)
    fill(245,245,245)
    rect(1,250,600,250)
    fill(50,205,50)
    triangle(200,150,170,200,230,200)
    triangle(200,200,160,250,240,250)
    triangle(200,250,150,300,250,300)
    fill(162,82,45)
    rect(190,300,20,30)
    fill(255,255,255)
    ellipse(350,180,50,50)
    ellipse(350,235,60,60)
    ellipse(350,300,70,70)
    fill(255,140,0)
    triangle(350,190,300,180,350,180)
    fill(0,0,0)
    ellipse(345,170,5,5)
    ellipse(355,170,5,5)
    fill(255,255,255)
    ellipse(150,z,20,20)
    ellipse(100,z,20,20)
    ellipse(300,z,20,20)
    ellipse(400,z,20,20)
    ellipse(500,z,20,20)
    x = x - 2
    z = z + 2
    
    
    
    
    
    
    
