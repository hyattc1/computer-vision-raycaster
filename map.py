from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W....W.....W',
    'W..W...W...W',
    'W....W..WW.W',
    'W.WW....W..W',
    'W.W..W.WWW.W',
    'W....W.....W',
    'WWWWWWWWWWWW'
]

world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map[(i * TILE, j * TILE)] = 'wall'
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
