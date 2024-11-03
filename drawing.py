from settings import *
import pygame
import math
from map import world_map, mini_map  # Import world_map and mini_map

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {
            'wall': pygame.image.load('textures/wall.png').convert()
        }

    def background(self):
        pygame.draw.rect(self.sc, SKYPURPLE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, DARKGREY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ox, oy = player_pos
        xm, ym = ox // TILE * TILE, oy // TILE * TILE
        cur_angle = player_angle - HALF_FOV
        for ray in range(NUM_RAYS):
            sin_a = math.sin(cur_angle)
            cos_a = math.cos(cur_angle)
            cos_cur_angle = math.cos(cur_angle - player_angle)
            depth = 0
            texture_vert = False  # Flag to check if hit was vertical or horizontal

            while True:
                depth += 1
                x = ox + depth * cos_a
                y = oy + depth * sin_a

                # Map positions
                map_x = int(x // TILE) * TILE
                map_y = int(y // TILE) * TILE

                if (map_x, map_y) in world_map:
                    # Determine if hit is on a vertical or horizontal wall
                    if int(ox) % TILE == int(x) % TILE:
                        texture_x = y % TILE
                        texture_vert = False
                    else:
                        texture_x = x % TILE
                        texture_vert = True

                    # Correct fish-eye effect
                    depth *= cos_cur_angle

                    # Calculate projected wall height
                    proj_height = PROJ_COEFF / (depth + 0.0001)

                    # Get texture column
                    texture = self.textures['wall']
                    texture_width = texture.get_width()
                    texture_height = texture.get_height()
                    texture_x = int(texture_width * texture_x / TILE)
                    wall_column = texture.subsurface(texture_x, 0, 1, texture_height)
                    wall_column = pygame.transform.scale(wall_column, (SCALE, int(proj_height)))

                    # Draw wall column
                    self.sc.blit(wall_column, (ray * SCALE, HALF_HEIGHT - proj_height // 2))
                    break

            cur_angle += DELTA_ANGLE

        # Ensure crosshair is drawn after all other elements in the world
        self.draw_crosshair()

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, WHITE, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)
    
    def draw_crosshair(self):
        # Draw a simple crosshair in the center of the screen
        pygame.draw.line(self.sc, WHITE, (HALF_WIDTH - 10, HALF_HEIGHT), (HALF_WIDTH + 10, HALF_HEIGHT), 2)
        pygame.draw.line(self.sc, WHITE, (HALF_WIDTH, HALF_HEIGHT - 10), (HALF_WIDTH, HALF_HEIGHT + 10), 2)
