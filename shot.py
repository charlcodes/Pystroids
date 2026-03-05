
from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, color = "white"):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

'''
    def kill(self):
        # spawn explosion here before the shot is removed
        Explosion(self.position.x, self.position.y)
        super().kill()  # then actually destroy the shot
        
class Explosion(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 5)  # start small
    
    def update(self, dt):
        self.radius += 50 * dt  # grow outward
        if self.radius > 40:    # max size reached
            self.kill()
    
    def draw(self, screen):
        pygame.draw.circle(screen, "orange", self.position, int(self.radius), 2)
'''