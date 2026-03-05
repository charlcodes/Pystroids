

import pygame

class CircleShape(pygame.sprite.Sprite):
   
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers) # type: ignore[unused]
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
    
    def collides_with(self, other):
        radi_added = self.radius + other.radius
        distance_between_centers = self.position.distance_to(other.position)
        if distance_between_centers <= radi_added:
            return True
        else:
            return False