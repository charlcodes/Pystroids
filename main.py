import pygame
from pygame import display

import sys
from asteroid import * 
from constants import *
from logger import log_state, log_event
from player import Player
from asteroidfield import *
from shot import Explosion, Shot
from score import *



def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    clock_ast = pygame.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    ###

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    scores = pygame.sprite.Group() #

    ###

    Player.containers = (updatable, drawable) # type: ignore[unused]
    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore[unused]
    AsteroidField.containers = updatable # type: ignore[unused]
    Shot.containers = (shots, updatable, drawable) # type: ignore[unused]
    Explosion.containers = (explosions, updatable, drawable) # type: ignore[unused]
    #Score.containers = drawable # type: ignore
    player = Player(x,y)
    astrof = AsteroidField() # # #
    scr = Score()
    

    while True:
        
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if obj.collides_with(bullet) == True: # :/ astroid collides with bullet
                    log_event("asteroid_shot")
                    bullet.kill()
                    obj.split(scr)
            for explotion in explosions:
                if obj.collides_with(explotion):
                    log_event("explosion_touched_astroid")
                    obj.split(scr)

        for draws in drawable:
            draws.draw(screen)

        scr.draw(screen)

        display.flip()
        dt = (clock_ast.tick(60)) / 1000
        #print(dt)

if __name__ == "__main__":
    main()


