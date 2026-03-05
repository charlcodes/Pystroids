import pygame
from circleshape import CircleShape
from constants import *
from shot import Explosion, Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.missile_cooldown = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
         pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH) # type: ignore[unused]
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):

        was_missile_ready = self.missile_cooldown <= 0
        

        self.shot_cooldown -= dt
        self.missile_cooldown -= dt

        if not was_missile_ready and self.missile_cooldown <= 0:
            print("KA-CHUNK")    

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]: 
            self.shoot()
        if keys[pygame.K_f]: 
            self.fire_missile()

    def move(self,dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self):

        if self.shot_cooldown > 0:
            return

        shot = Shot(self.position.x, self.position.y, #type: ignore[unused]
                    SHOT_RADIUS,
                    SHOT_EXPLOTION_MAX_SIZE,
                    SHOT_EXPLOTION_START_SIZE,
                    SHOT_EXPLOTION_PROPIGATION_SPEED ) 
        shot_vector = pygame.Vector2(0, 1)
        rotated_shot = shot_vector.rotate(self.rotation)
        shot.velocity = rotated_shot * PLAYER_SHOT_SPEED
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
    
    def fire_missile(self):
        
        if self.missile_cooldown > 0:
            return #audible click would be great, and when cool down ends border flash
        
        missile = Shot(self.position.x, self.position.y, #type: ignore
                       MISSILE_RADIUS, 
                       MISSILE_EXPLOTION_MAX_SIZE,
                       MISSILE_EXPLOTION_START_SIZE,
                       MISSILE_EXPLOTION_PROPIGATION_SPEED) 
        shot_vector = pygame.Vector2(0, 1)
        rotated_shot = shot_vector.rotate(self.rotation)
        missile.velocity = rotated_shot * MISSILE_SPEED
        self.missile_cooldown = MISSILE_COOLDOWN_SECONDS
