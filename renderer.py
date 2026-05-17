from config import *

import pygame


def draw_world(screen, world_map, fertility_map):
    for x in range(MAP_DIM):
        for y in range(MAP_DIM):
            fert = fertility_map[x, y]
            # Background tint: darker for low fertility, lighter for high
            tint = min(int(fert * 20), 80)  # cap so it doesn't get too bright
            bg_color = (0, 0+ tint, 0)
            pygame.draw.rect(screen, bg_color, 
                             (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if world_map[x, y] > 0:
                # Food on top — bright green
                pygame.draw.rect(screen, (100, 0, 0),
                                 (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))