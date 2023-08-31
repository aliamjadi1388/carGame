import pgzrun
import random

WIDTH = 1000
HEIGHT = 700

listCar = ["car1","car2","car3"]

car = Actor(random.choice(listCar) , (500 , 350))

speedCars = 2

def update():
    global speedCars

    car.x -= speedCars
    if car.x <= -50:
        speedCars += 1
        car.x = 1050
        car.image = random.choice(listCar)
        car.y = random.randint(100,900)

def draw():
    screen.fill("white")
    car.draw()


def on_mouse_down(pos):
    global speedCars
    if car.collidepoint(pos) and car.image == "car1":
        car.image = "car2"
        speedCars += 1

    elif car.collidepoint(pos) and car.image == "car2":
        car.image = "car3"  
        speedCars += 1

    elif car.collidepoint(pos) and car.image == "car3":
        car.image = "car1"
        speedCars += 1

pgzrun.go()