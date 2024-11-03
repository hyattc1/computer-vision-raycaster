import pygame
from settings import *
from player import Player
from map import world_map
from drawing import Drawing
from sprites import load_weapon_sprites, load_monster_sprites
from enemies import Enemy  # Import Enemy class

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
weapons = load_weapon_sprites()
monsters_sprites = load_monster_sprites()

# Initialize enemies with death sprites
enemies = [
    Enemy(x=3 * TILE, y=3 * TILE, sprites=monsters_sprites['ghost'], speed=0.8, scale=0.7, death_sprites=monsters_sprites['ghost_die']),
    Enemy(x=5 * TILE, y=5 * TILE, sprites=monsters_sprites['bat'], speed=1.1, scale=0.3, death_sprites=monsters_sprites['bat_die']),
    Enemy(x=7 * TILE, y=7 * TILE, sprites=monsters_sprites['kos'], speed=0.5, scale=0.8, death_sprites=monsters_sprites['kos_die']),
]

current_weapon = 'wrench'
weapon_frame = 0
weapon_animation_speed = 0.2
weapon_keys = {
    'wrench': pygame.K_1,
    'plasma': pygame.K_2,
}
attack = False

def check_hit(enemy):
    # Check if crosshair is within enemy's hitbox
    crosshair_x, crosshair_y = HALF_WIDTH, HALF_HEIGHT
    enemy_rect = enemy.get_rect()
    enemy_rect.center = (enemy.x, enemy.y)
    return enemy_rect.collidepoint(crosshair_x, crosshair_y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # Handle weapon switching
        elif event.type == pygame.KEYDOWN:
            for weapon, key in weapon_keys.items():
                if event.key == key:
                    current_weapon = weapon
                    weapon_frame = 0
        # Handle attacks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                attack = True
                weapon_frame = 0

                # Register hit if crosshair overlaps with an enemy
                for enemy in enemies:
                    if enemy.alive and check_hit(enemy):
                        enemy.die()  # Trigger death animation

    player.movement()
    sc.fill(BLACK)

    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)

    # Update and draw enemies
    for enemy in enemies:
        enemy.update(player)
        if enemy.alive or enemy.dying:  # Draw only if alive or in death animation
            enemy.draw(sc, player)

    # Update weapon animation
    if attack:
        if current_weapon == 'plasma':
            weapon_animation_speed = 0.3  # Faster animation speed for plasma
        else:
            weapon_animation_speed = 0.4  # Default for other weapons like wrench

        weapon_frame += weapon_animation_speed
        if weapon_frame >= len(weapons[current_weapon]):
            weapon_frame = 0
            attack = False
    else:
        weapon_frame = 0

    # Draw the current weapon
    weapon_image = weapons[current_weapon][int(weapon_frame)]
    weapon_rect = weapon_image.get_rect()
    weapon_rect.center = (HALF_WIDTH, HEIGHT - weapon_rect.height // 2)
    sc.blit(weapon_image, weapon_rect)

    # Draw crosshair last to ensure it appears on top
    drawing.draw_crosshair()

    pygame.display.flip()
    clock.tick(FPS)