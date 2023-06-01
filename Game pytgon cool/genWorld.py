import math
import numpy as np
from perlin_noise import PerlinNoise

def gen(x, y, seed, octaves):
    noise = PerlinNoise(octaves=octaves, seed=seed)
    pic = [[noise([i/x, j/y]) for j in range(x)] for i in range(y)]
    return pic

