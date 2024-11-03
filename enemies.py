import pygame
import math
from settings import *
from map import world_map

class Enemy:
    def __init__(self, x, y, sprites, speed=1, scale=1.0, death_sprites=None):
        self.x = x
        self.y = y
        self.sprites = sprites
        self.death_sprites = death_sprites or []  # Optional death animation sprites
        self.frame_index = 0
        self.speed = speed
        self.scale = scale
        self.distance = 0
        self.angle = 0
        self.alive = True
        self.dying = False
        self.death_frame_index = 0  # Track frame for death animation

    def update(self, player):
        if not self.alive and not self.dying:
            return

        dx = self.x - player.x
        dy = self.y - player.y
        self.distance = math.hypot(dx, dy)
        self.angle = math.atan2(dy, dx)

        if self.alive and self.distance > 0:
            move_step = self.speed
            dx_move = -move_step * math.cos(self.angle)
            dy_move = -move_step * math.sin(self.angle)
            if not self.collide(dx_move, 0):
                self.x += dx_move
            if not self.collide(0, dy_move):
                self.y += dy_move

        self.frame_index = (self.frame_index + 0.1) % len(self.sprites)

    def die(self):
        """Trigger the death animation for the enemy."""
        self.alive = False
        self.dying = True
        self.death_frame_index = 0

    def collide(self, dx, dy):
        next_x = self.x + dx
        next_y = self.y + dy
        return (int(next_x // TILE) * TILE, int(next_y // TILE) * TILE) in world_map

    def is_visible(self, player):
        ox, oy = player.x, player.y
        ex, ey = self.x, self.y
        dx = ex - ox
        dy = ey - oy
        distance = math.hypot(dx, dy)
        angle = math.atan2(dy, dx)
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        x, y = ox, oy
        for i in range(int(distance)):
            x += cos_a
            y += sin_a
            if (int(x // TILE) * TILE, int(y // TILE) * TILE) in world_map:
                return False
        return True

    def get_rect(self):
        """Returns the current bounding rectangle of the enemy for collision detection."""
        if self.sprites:
            sprite = self.sprites[int(self.frame_index)]
            rect = sprite.get_rect()
            rect.center = (self.x, self.y)
            return rect
        return pygame.Rect(self.x, self.y, TILE * self.scale, TILE * self.scale)

    def draw(self, sc, player):
        if not self.is_visible(player):
            return

        rel_angle = self.angle - player.angle
        if rel_angle > math.pi:
            rel_angle -= 2 * math.pi
        if rel_angle < -math.pi:
            rel_angle += 2 * math.pi

        if -HALF_FOV < rel_angle < HALF_FOV:
            proj_distance = self.distance * math.cos(rel_angle)
            proj_height = min(int(PROJ_COEFF / proj_distance), HEIGHT * 2)

            if self.dying and self.death_sprites:
                # Play death animation
                sprite = self.death_sprites[int(self.death_frame_index)]
                self.death_frame_index += 0.1
                if self.death_frame_index >= len(self.death_sprites):
                    self.dying = False  # End death animation
            else:
                sprite = self.sprites[int(self.frame_index)]

            sprite = pygame.transform.scale(sprite, (int(proj_height * self.scale), int(proj_height * self.scale)))

            sprite_x = HALF_WIDTH + (rel_angle * (WIDTH / FOV)) - sprite.get_width() // 2
            sprite_y = HALF_HEIGHT - sprite.get_height() // 2
            sc.blit(sprite, (sprite_x, sprite_y))
