z = 450
x = 200
def setup():
    size(600,600)
def draw():
    global z,x
    triangle(300,x,250,250,350,250)
    triangle(200,350,x,450,250,450)
    triangle(400,350,350,450,z,450)
    x = x - 1
    z = z + 1
    
    
    
 
    
       
          
             
                   
