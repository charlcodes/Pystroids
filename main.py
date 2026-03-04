import pygame
from pygame import display

from asteroid import * 
from constants import *
from logger import log_state
from player import Player
from asteroidfield import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    clock_ast = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #asteroidfields = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # type: ignore[unused]
    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore[unused]
    AsteroidField.containers = updatable # type: ignore[unused]


    player = Player(x,y)
    astrof = AsteroidField()
    

    while True:
        
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        
        screen.fill("black")

        for obj in updatable:
            obj.update(dt)
        
        for draws in drawable:
            draws.draw(screen)

        

        display.flip()
        dt = (clock_ast.tick(60)) / 1000
        print(dt)

if __name__ == "__main__":
    main()


