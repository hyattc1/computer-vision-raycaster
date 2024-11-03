from settings import *
import pygame
import math
from map import world_map  # Import world_map

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        speed = player_speed
        if keys[pygame.K_LSHIFT]:
            speed *= 1.5  # Sprint if shift is held down
        if keys[pygame.K_w]:
            dx += speed * cos_a
            dy += speed * sin_a
        if keys[pygame.K_s]:
            dx += -speed * cos_a
            dy += -speed * sin_a
        if keys[pygame.K_a]:
            dx += speed * sin_a
            dy += -speed * cos_a
        if keys[pygame.K_d]:
            dx += -speed * sin_a
            dy += speed * cos_a

        # Collision detection
        if not self.collide(dx, dy):
            self.x += dx
            self.y += dy

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    def collide(self, dx, dy):
        next_x = self.x + dx
        next_y = self.y + dy
        if (next_x // TILE * TILE, next_y // TILE * TILE) in world_map:
            return True
        return False
