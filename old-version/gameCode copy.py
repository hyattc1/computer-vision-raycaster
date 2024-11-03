import pygame
from pygame.locals import *
import math as m
import os
import sys

# Initialize Pygame
pygame.init()

# Game settings
win_width, win_height = 800, 600  # Window size
fps = 60
display = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Wean After Dark")
clock = pygame.time.Clock()

# Game map
game_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1],
    [1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1],
    [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
MAP_WIDTH = len(game_map[0])
MAP_HEIGHT = len(game_map)
TILE_SIZE = 1  # Map grid units

# Player settings
xpos, ypos = 2.5, 2.5  # Starting position
rot_r = 0  # Rotation angle in radians

# Movement settings
sensitivity = m.pi / 256
move_speed = 0.05

# Raycasting settings
fov = 60  # Field of view in degrees
num_rays = win_width  # One ray per horizontal pixel
max_depth = 20
precision = 0.01

# Controls
wk, sk, ak, dk = False, False, False, False

# Load weapon sprites
def load_weapon_sprites():
    wrench_sprites = []
    plasma_sprites = []

    # Load wrench sprites
    wrench_frames = 17  # Adjust according to your frames
    for i in range(1, wrench_frames + 1):
        image_path = f'Sprites/Wrench/wrench{i}-removebg-preview.png'
        if os.path.exists(image_path):
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (300, 300))
            wrench_sprites.append(image)
        else:
            print(f"Warning: {image_path} not found.")

    # Load plasma sprites
    plasma_frames = 4  # Adjust according to your frames
    for i in range(1, plasma_frames + 1):
        image_path = f'Sprites/PlasmaBlaster/plasma{i}-removebg-preview.png'
        if os.path.exists(image_path):
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (300, 300))
            plasma_sprites.append(image)
        else:
            print(f"Warning: {image_path} not found.")

    return wrench_sprites, plasma_sprites

wrench_sprites, plasma_sprites = load_weapon_sprites()

class Weapon:
    def __init__(self, name, sprites, damage, range):
        self.name = name
        self.sprites = sprites
        self.frame_index = 0
        self.is_animating = False
        self.damage = damage
        self.range = range

    def animate(self):
        if self.is_animating:
            self.frame_index += 0.5  # Adjust animation speed
            if self.frame_index >= len(self.sprites):
                self.frame_index = 0
                self.is_animating = False
        else:
            self.frame_index = 0

    def draw(self):
        sprite = self.sprites[int(self.frame_index)]
        sprite_rect = sprite.get_rect(center=(win_width // 2, win_height - sprite.get_height() // 2))
        display.blit(sprite, sprite_rect)

# Create weapon instances
wrench_weapon = Weapon('Wrench', wrench_sprites, damage=100, range=1.5)
plasma_weapon = Weapon('Plasma Blaster', plasma_sprites, damage=100, range=10)
current_weapon = wrench_weapon

# Load monster sprites
def load_monster_sprites():
    ghost_move_sprites = []
    ghost_die_sprites = []

    # Load ghost move sprites
    for i in range(1, 7):
        image_path = f'Sprites/Ghost/GhostMove/GSTFLY{chr(64 + i)}0-removebg-preview.png'
        if os.path.exists(image_path):
            image = pygame.image.load(image_path).convert_alpha()
            ghost_move_sprites.append(image)
        else:
            print(f"Warning: {image_path} not found.")

    # Load ghost die sprites
    for i in range(1, 7):
        image_path = f'Sprites/Ghost/GhostDie/GSTDIE{chr(64 + i)}0-removebg-preview.png'
        if os.path.exists(image_path):
            image = pygame.image.load(image_path).convert_alpha()
            ghost_die_sprites.append(image)
        else:
            print(f"Warning: {image_path} not found.")

    return ghost_move_sprites, ghost_die_sprites

ghost_move_sprites, ghost_die_sprites = load_monster_sprites()

class Monster:
    def __init__(self, x, y, move_sprites, die_sprites):
        self.x = x
        self.y = y
        self.move_sprites = move_sprites
        self.die_sprites = die_sprites
        self.alive = True
        self.frame_index = 0
        self.state = 'move'  # 'move' or 'die'
        self.distance = 0

    def update(self):
        if self.alive:
            # Simple AI: move towards player
            dx = xpos - self.x
            dy = ypos - self.y
            angle = m.atan2(dy, dx)
            self.x += 0.02 * m.cos(angle)
            self.y += 0.02 * m.sin(angle)
            self.distance = m.hypot(dx, dy)

            # Animation
            self.frame_index = (self.frame_index + 0.1) % len(self.move_sprites)
        else:
            # Death animation
            if self.frame_index < len(self.die_sprites) - 1:
                self.frame_index += 0.1
            self.distance = m.hypot(xpos - self.x, ypos - self.y)

    def draw(self):
        if self.alive:
            sprite = self.move_sprites[int(self.frame_index)]
        else:
            sprite = self.die_sprites[int(self.frame_index)]
        # Calculate angle between player and monster
        dx = self.x - xpos
        dy = self.y - ypos
        angle_to_monster = m.atan2(dy, dx) - rot_r
        # Normalize angle
        if angle_to_monster > m.pi:
            angle_to_monster -= 2 * m.pi
        if angle_to_monster < -m.pi:
            angle_to_monster += 2 * m.pi

        # Check if monster is within FOV
        if -m.radians(fov / 2) < angle_to_monster < m.radians(fov / 2):
            # Distance to monster
            dist = m.hypot(dx, dy)
            # Correct fisheye
            dist *= m.cos(angle_to_monster)
            # Calculate projection
            if dist == 0:
                dist = 0.0001  # Avoid division by zero
            projection_height = int(win_height / dist)
            # Calculate position
            sprite = pygame.transform.scale(sprite, (projection_height, projection_height))
            sprite_x = win_width // 2 + m.tan(angle_to_monster) * win_width // 2 - sprite.get_width() // 2
            sprite_y = win_height // 2 - sprite.get_height() // 2
            # Draw sprite
            display.blit(sprite, (sprite_x, sprite_y))

monsters = [
    Monster(5, 5, ghost_move_sprites, ghost_die_sprites),
    Monster(10, 10, ghost_move_sprites, ghost_die_sprites),
]

# Main game loop
run = True
while run:
    clock.tick(fps)
    pygame.display.set_caption("Wean After Dark - FPS: " + str(round(clock.get_fps())))

    # Event handling
    for e in pygame.event.get():
        if e.type == QUIT:
            run = False

        if e.type == KEYDOWN:
            if e.key == pygame.K_w:
                wk = True
            if e.key == pygame.K_s:
                sk = True
            if e.key == pygame.K_a:
                ak = True
            if e.key == pygame.K_d:
                dk = True
            if e.key == pygame.K_1:
                current_weapon = wrench_weapon
            if e.key == pygame.K_2:
                current_weapon = plasma_weapon
        if e.type == KEYUP:
            if e.key == pygame.K_w:
                wk = False
            if e.key == pygame.K_s:
                sk = False
            if e.key == pygame.K_a:
                ak = False
            if e.key == pygame.K_d:
                dk = False
        if e.type == MOUSEBUTTONDOWN:
            # Attack
            current_weapon.is_animating = True
            current_weapon.frame_index = 0
            # Check for monster hit
            for monster in monsters:
                if monster.alive and monster.distance <= current_weapon.range:
                    monster.alive = False
                    monster.frame_index = 0
                    monster.state = 'die'
                    break  # Only hit one monster

    # Player movement
    x, y = xpos, ypos
    if wk:
        x += move_speed * m.cos(rot_r)
        y += move_speed * m.sin(rot_r)
    if sk:
        x -= move_speed * m.cos(rot_r)
        y -= move_speed * m.sin(rot_r)
    if ak:
        rot_r -= sensitivity
    if dk:
        rot_r += sensitivity
    # Collision detection
    if 0 <= int(y) < MAP_HEIGHT and 0 <= int(x) < MAP_WIDTH:
        if game_map[int(y)][int(x)] == 0:
            xpos, ypos = x, y

    # Update monsters
    for monster in monsters:
        monster.update()

    # Rendering
    display.fill((30, 30, 30))  # Dark background color

    # Raycasting
    for i in range(num_rays):
        ray_angle = rot_r - m.radians(fov / 2) + m.radians(fov) * i / num_rays
        sin_a = m.sin(ray_angle)
        cos_a = m.cos(ray_angle)
        depth = 0
        hit = False

        while not hit and depth < max_depth:
            depth += precision
            x = xpos + cos_a * depth
            y = ypos + sin_a * depth

            if 0 <= int(y) < MAP_HEIGHT and 0 <= int(x) < MAP_WIDTH:
                if game_map[int(y)][int(x)] != 0:
                    # Wall hit
                    hit = True
                    # Correct fish-eye effect
                    depth *= m.cos(rot_r - ray_angle)
                    # Calculate wall height
                    if depth == 0:
                        depth = 0.0001  # Avoid division by zero
                    height = int(win_height / (depth))
                    # Limit wall height to screen height
                    if height > win_height:
                        height = win_height
                    # Calculate color shading
                    shade = 255 / (1 + depth ** 2 * 0.00002)
                    shade = int(max(0, min(255, shade)))
                    color = (shade, shade, shade)
                    # Draw wall slice
                    pygame.draw.rect(display, color, (i, win_height // 2 - height // 2, 1, height))
            else:
                # Ray is out of bounds
                hit = True

    # Draw monsters
    monsters_sorted = sorted(monsters, key=lambda m: m.distance, reverse=True)
    for monster in monsters_sorted:
        monster.draw()

    # Draw weapon
    current_weapon.animate()
    current_weapon.draw()

    pygame.display.flip()

pygame.quit()
sys.exit()
