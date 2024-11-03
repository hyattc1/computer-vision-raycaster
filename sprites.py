import pygame
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

def load_weapon_sprites():
    weapons = {}

    # Load Wrench sprites
    wrench_sprites = []
    wrench_path = os.path.join(script_dir, 'Sprites', 'Wrench')
    if os.path.exists(wrench_path):
        for filename in sorted(os.listdir(wrench_path)):
            if filename.endswith('.png'):
                image = pygame.image.load(os.path.join(wrench_path, filename)).convert_alpha()
                wrench_sprites.append(image)
        weapons['wrench'] = wrench_sprites

    # Load Plasma Blaster sprites in exact order from plasma0.png to plasma28.png
    plasma_sprites = []
    plasma_path = os.path.join(script_dir, 'Sprites', 'PlasmaBlaster')
    if os.path.exists(plasma_path):
        for i in range(29):  # 29 images from plasma0.png to plasma28.png
            filename = f"plasma{i}.png"
            file_path = os.path.join(plasma_path, filename)
            if os.path.exists(file_path):
                image = pygame.image.load(file_path).convert_alpha()
                plasma_sprites.append(image)
        weapons['plasma'] = plasma_sprites

    return weapons

def load_monster_sprites():
    monsters = {}

    # Load Ghost move sprites
    ghost_move_sprites = []
    ghost_move_path = os.path.join(script_dir, 'Sprites', 'Ghost', 'GhostMove')
    if os.path.exists(ghost_move_path):
        for filename in sorted(os.listdir(ghost_move_path)):
            if filename.endswith('.png'):
                image = pygame.image.load(os.path.join(ghost_move_path, filename)).convert_alpha()
                ghost_move_sprites.append(image)
        monsters['ghost'] = ghost_move_sprites

    # Load Ghost death sprites
    ghost_die_sprites = []
    ghost_die_path = os.path.join(script_dir, 'Sprites', 'Ghost', 'GhostDie')
    if os.path.exists(ghost_die_path):
        for filename in sorted(os.listdir(ghost_die_path)):
            if filename.endswith('.png'):
                image = pygame.image.load(os.path.join(ghost_die_path, filename)).convert_alpha()
                ghost_die_sprites.append(image)
        monsters['ghost_die'] = ghost_die_sprites

    # Load Bat move sprites
    bat_move_sprites = []
    bat_move_path = os.path.join(script_dir, 'Sprites', 'Bat', 'BatMove')
    if os.path.exists(bat_move_path):
        for filename in sorted(os.listdir(bat_move_path)):
            if filename.endswith('.png'):
                image = pygame.image.load(os.path.join(bat_move_path, filename)).convert_alpha()
                bat_move_sprites.append(image)
        monsters['bat'] = bat_move_sprites

    # Load Bat death sprites
    bat_die_sprites = []
    bat_die_path = os.path.join(script_dir, 'Sprites', 'Bat', 'BatDie')
    if os.path.exists(bat_die_path):
        for filename in sorted(os.listdir(bat_die_path)):
            if filename.endswith('.png'):
                image = pygame.image.load(os.path.join(bat_die_path, filename)).convert_alpha()
                bat_die_sprites.append(image)
        monsters['bat_die'] = bat_die_sprites

    # Load Evil King Kos move sprites
    kos_walk_sprites = []
    kos_walk_path = os.path.join(script_dir, 'Sprites', 'Kos', 'KosWalk')
    if os.path.exists(kos_walk_path):
        for filename in sorted(os.listdir(kos_walk_path)):
            if filename.endswith('.png'):
                image = pygame.image.load(os.path.join(kos_walk_path, filename)).convert_alpha()
                kos_walk_sprites.append(image)
        monsters['kos'] = kos_walk_sprites

    # Load Evil King Kos death sprites
    kos_die_sprites = []
    kos_die_path = os.path.join(script_dir, 'Sprites', 'Kos', 'KosDie')
    if os.path.exists(kos_die_path):
        for filename in sorted(os.listdir(kos_die_path)):
            if filename.endswith('.png'):
                image = pygame.image.load(os.path.join(kos_die_path, filename)).convert_alpha()
                kos_die_sprites.append(image)
        monsters['kos_die'] = kos_die_sprites

    return monsters
