import pygame

cell_size = 40
cell_number = 20
pygame.display.set_caption('Snakes Game by Python - UIT')
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

watermelon = pygame.image.load('graphics/watermelon.png').convert_alpha()
menu_bg = pygame.image.load('graphics/menu/menu_bg.jpg')

grass_land = (167, 209, 61)
grass_bush = (95,172,0)
fruit_color = (126, 166, 114)
snake_color = (183, 111, 122)
white = (255, 255, 255)
black = (0, 0, 0)
start_button = (0, 255, 0)
title = (248, 234, 81)
button_base_color = "#d7fcd4"

HS_FILE = "high_score.txt"