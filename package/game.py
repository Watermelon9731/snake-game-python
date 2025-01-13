from utils import cell_size, screen, watermelon, cell_number, grass_bush, HS_FILE
from os import path
import pygame
from package.snake import Snake
from package.fruit import Fruit

def get_font(size):
    return pygame.font.Font("./graphics/font/menu.ttf", size)

class Game:
    def __init__(self):
        self.level = 1
        self.snake = Snake()
        self.fruit = Fruit()
        self.start = True
        self.restart = False
        self.score = 0

    def update(self):
        self.game_restart = False
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_element(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.random_position()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.random_position()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
        self.start = False
        self.restart = False
        pygame.display.flip()

    def draw_grass(self):
        for row in range (cell_number):
            if row % 2 == 0:
                for column in range(cell_number):
                    if column % 2 == 0:
                        grass_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_bush, grass_rect)
            else:
                for column in range(cell_number):
                    if column % 2 != 0:
                        grass_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_bush, grass_rect)

    def draw_score(self):
        level_weight = 1

        if self.level == 2:
            level_weight = 2
        elif self.level == 3:
            level_weight = 4

        score_text = str((len(self.snake.body) - 3) * level_weight)
        self.score = int(score_text)
        score_font = pygame.font.Font(None, 25)
        score_surface = score_font.render(str(score_text), True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        watermelon_rect = watermelon.get_rect(midright = (score_rect.left - 20, score_rect.centery))
        bg_rect = pygame.Rect(watermelon_rect.left - 10, watermelon_rect.top, watermelon_rect.width + score_rect.width + cell_size, watermelon_rect.height)
        
        pygame.draw.rect(screen, (255, 255, 255), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(watermelon, watermelon_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)