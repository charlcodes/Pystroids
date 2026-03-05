
from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius = 1,
                expl_max_size = 1,
                expl_start_size = 1,
                expl_propigation_speed = 1):
        super().__init__(x, y, radius)
        self.explotion_size = expl_max_size
        self.expl_start_size = expl_start_size
        self.expl_propigation_speed = expl_propigation_speed

    def draw(self, screen, color = "white"):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)


    def kill(self):
        Explosion(self.position.x, self.position.y, self.radius, #type: ignore[unused]
                  self.explotion_size, self.expl_start_size,
                  self.expl_propigation_speed) 
        super().kill()  
        
class Explosion(CircleShape):
    def __init__(self, x, y, r, e_m_s, e_s_s, e_p_s):   
        super().__init__(x, y, r)
        self.e_m_s = e_m_s
        self.e_s_s = e_s_s
        self.e_p_s = e_p_s

    def update(self, dt):
        self.radius += self.e_p_s * dt  
        if self.radius > self.e_m_s  :    
            self.kill()
    
    def draw(self, screen, color="orange"):
        pygame.draw.circle(screen, color, self.position, int(self.radius), 2)
