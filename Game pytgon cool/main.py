import math
import pygame as pg
from genWorld import *
import random
from pygameZoom import PygameZoom

pg.init()

#creating window
WIDTH, HEIGHT = 1000, 600
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("gamer game")


#variables and images
FPS = 60

 
def worldGen():
    worldDict = {}
    map = gen(int(WIDTH/10), int(HEIGHT/10), random.randrange(0, 1000), 5)
    for i in range(0, int(HEIGHT/10)):
        for j in range(0, int(WIDTH/10)):
            if map[i][j] > -0.07:
                pg.draw.rect(WIN, (0, random.randrange(0, 25), 255 - abs(map[i][j])*200), [j*10, i*10, 10, 10], 0)
            else:
                pg.draw.rect(WIN, (17, random.randrange(95, 102), 0), [j*10, i*10, 10, 10], 0)

def zoomIn():
    pass


def highlight():
    posx, posy = pg.mouse.get_pos()
    posx, posy = math.floor(posx/10), math.floor(posy/10)
    pg.draw.rect(WIN, (250, 250, 250), [posx*10, posy*10, 10, 10], 0) 
    print(posx, posy)

def main():
    clock = pg.time.Clock()
    run = True

    worldGen()

    while run:

        #gets list of keys down
        keys = pg.key.get_pressed()
        
        #updates at rate of FPS
        clock.tick(FPS)
        

        #event listener
        for event in pg.event.get():
            if event.type==pg.QUIT:
                run=False


        #showing images on screen

        pg.display.update()     

    pg.quit()


if __name__ == "__main__":
    main()




    
