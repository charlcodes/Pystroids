
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
from score import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen, color = "white"):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self, score): #score object for .add()
        self.kill()
        score.add(self.radius) 
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            ran_ang = random.uniform(20, 50)
            ast_one = self.velocity.rotate(ran_ang)
            ast_two = self.velocity.rotate(-ran_ang)
            new_small_size = self.radius - ASTEROID_MIN_RADIUS
            #ast_1_vel = ast_one * 1.2
            #ast_1 = astf.spawn(self, new_small_size, self.position,ast_1_vel)


            ast_1 = Asteroid(self.position.x, self.position.y, new_small_size) #type: ignore[unused]
            ast_2 = Asteroid(self.position.x, self.position.y, new_small_size) #type: ignore[unused]

            ast_1.velocity = 1.2 * ast_one
            ast_2.velocity = 1.2 * ast_two

