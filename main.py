from config import *
from world import *
from renderer import *

import pygame


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

SIM_TICKS_PER_FRAME = 1  


running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                SIM_TICKS_PER_FRAME = min(SIM_TICKS_PER_FRAME * 2, 256)
            elif event.key == pygame.K_DOWN:
                SIM_TICKS_PER_FRAME = max(SIM_TICKS_PER_FRAME // 2, 1)
            elif event.key == pygame.K_SPACE:
                paused = not paused
    
    if not paused:
        for _ in range(SIM_TICKS_PER_FRAME):
            grow_plants()
    
    draw_world(screen, world_map, fertility_map)
    pygame.display.flip()
    clock.tick(60)

