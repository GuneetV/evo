from config import *

import pygame


def draw_world(screen, world_map, fertility_map):
    for x in range(MAP_DIM):
        for y in range(MAP_DIM):
            if world_map[x, y] > 0:
                # Food on top — bright green
                pygame.draw.rect(screen, (0, 100, 0),
                                 (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))