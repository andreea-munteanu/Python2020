import pygame
from Constants import OPPONENT, ROWS, COLS, FIRST_PLAYER, WIDTH, HEIGHT


# Initialize the pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("4 In A Row")
icon = pygame.image.load('4-in-a-row.png')
pygame.display.set_icon(icon)


