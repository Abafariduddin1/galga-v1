import pgzrun

WIDTH=700
HEIGHT=700

bees = []

ship=Actor("plane.png")
ship.pos=350,600

point=75
ypoint=10
for b in range(4):
    for i in range(8):
        bee = Actor("bee.png")
        bees.append(bee)
        bees[i].x=60+60*i

    


def draw():
    screen.clear()
    screen.fill("blue")
    ship.draw()
    for i in bees:
        i.draw()
    
      

def update():
     if keyboard.a:
        ship.x -= 5 
     if keyboard.d:
        ship.x += 5 
     for i in bees:
         i.y=i.y+1
     if ship.x<=-40:
         ship.x=730
     if ship.x>=740:
         ship.x=-30    
        
               

    







pgzrun.go()