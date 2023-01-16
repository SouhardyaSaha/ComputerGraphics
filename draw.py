import pygame
import sys
from pygame import gfxdraw
from pygame.locals import *

pygame.init()

screen_width, screen_height = 600, 600

screen_surface = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption("DDA Line Drawing Algorithm")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

screen_surface.fill(BLACK)


def draw_figure(points):
    for (x, y) in points:
        gfxdraw.pixel(screen_surface, round(x), round(y), WHITE)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
