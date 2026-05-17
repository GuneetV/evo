from config import *

from collections import deque
import numpy as np

world_map = np.zeros((MAP_DIM, MAP_DIM), dtype=float)

fertility_map = np.ones(world_map.shape, dtype=float)
fertility_spots = rng.integers(0, MAP_DIM, size=(FERTILITY_PATCHES, 2))


def spread_fertility(coords):
    v = {coords}
    q = deque([(coords, FERTILITY_BOOST)])
    
    while q:
        (x, y), boost = q.popleft()
        fertility_map[x, y] += boost
        
        next_boost = boost * FERTILITY_DECAY
        if next_boost < FERTILITY_MIN:
            continue
        
        for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < MAP_DIM and 0 <= ny < MAP_DIM and (nx, ny) not in v:
                v.add((nx, ny))
                q.append(((nx, ny), next_boost))


for c in fertility_spots:
    spread_fertility(tuple(c))


def tick():
    rng.random()