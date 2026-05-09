import numpy as np
import pygame

from enums import Biome

# Create a 100x100 biome map
biome_map = np.zeros((100, 100), dtype=np.int8)
biome_map[:, :30] = Biome.OCEAN.value
biome_map[:, 30:70] = Biome.FOREST.value
biome_map[:, 70:] = Biome.PLAINS.value


# Color lookup keyed by biome ID
BIOME_COLORS = {
    Biome.OCEAN:   (30, 80, 180),
    Biome.FOREST:  (40, 120, 50),
    Biome.PLAINS:  (160, 200, 90),
}

CELL_SIZE = 6  # pixels per grid cell
WIDTH, HEIGHT = biome_map.shape[1] * CELL_SIZE, biome_map.shape[0] * CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

map_surface = pygame.Surface((biome_map.shape[1], biome_map.shape[0]))

for y in range(biome_map.shape[0]):
    for x in range(biome_map.shape[1]):
        map_surface.set_at((x, y), BIOME_COLORS[biome_map[y, x]])

# Scale up to the window size with nearest-neighbor (so pixels stay crisp)
map_surface = pygame.transform.scale(map_surface, (WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(map_surface, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()