import pygame, random
from pygame.math import Vector2
from utils import cell_size, screen, watermelon, cell_number


class Fruit:
    def __init__(self):
        self.random_position()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(watermelon, fruit_rect)
        # pygame.draw.rect(screen, fruit_color, fruit_rect)

    def random_position(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)