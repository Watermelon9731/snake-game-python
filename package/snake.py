import pygame
from pygame.math import Vector2
from utils import cell_size, cell_number, screen

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_right = pygame.image.load('graphics/snake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('graphics/snake/head_left.png').convert_alpha()
        self.head_up = pygame.image.load('graphics/snake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('graphics/snake/head_down.png').convert_alpha()

        self.tail_up = pygame.image.load('graphics/snake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('graphics/snake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('graphics/snake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('graphics/snake/tail_left.png').convert_alpha()

        self.body_graphic = pygame.image.load('graphics/snake/body.jpg').convert_alpha()

        self.corner_top_left = pygame.image.load('graphics/snake/corner_top_left.png').convert_alpha()
        self.corner_top_right = pygame.image.load('graphics/snake/corner_top_right.png').convert_alpha()
        self.corner_bottom_left = pygame.image.load('graphics/snake/corner_bottom_left.png').convert_alpha()
        self.corner_bottom_right = pygame.image.load('graphics/snake/corner_bottom_right.png').convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                # previous_block = self.body[index + 1] - block
                # next_block = self.body[index - 1] - block
                # if previous_block.x == next_block.x:
                #     screen.blit(self.body_vertical, block_rect)
                # elif previous_block.y == next_block.y:
                #     screen.blit(self.body_horizontal, block_rect)
                # else:
                    # if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                    #     screen.blit(self.corner_top_left, block_rect)
                    # elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                    #     screen.blit(self.corner_bottom_left, block_rect)
                    # elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                    #     screen.blit(self.corner_top_right, block_rect)
                    # elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                    #     screen.blit(self.corner_bottom_right, block_rect)
                # pygame.draw.rect(screen, (252, 242, 113), block_rect)
                screen.blit(self.body_graphic, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0):
            self.head = self.head_left
        elif head_relation == Vector2(-1,0):
            self.head = self.head_right
        elif head_relation == Vector2(0,1):
            self.head = self.head_up
        elif head_relation == Vector2(0,-1):
            self.head = self.head_down

    def update_tail_graphics(self):
        last_index = len(self.body) - 1
        tail_relation = self.body[last_index] - self.body[last_index - 1]
        if tail_relation == Vector2(0,1):
            self.tail = self.tail_down
        if tail_relation == Vector2(0,-1):
            self.tail = self.tail_up
        if tail_relation == Vector2(1,0):
            self.tail = self.tail_right
        if tail_relation == Vector2(-1,0):
            self.tail = self.tail_left
        
    def move_snake(self):
        if self.new_block == True:
            body_cloned = self.body[:]
            body_cloned.insert(0, body_cloned[0] + self.direction)
            self.body = body_cloned[:]
            self.new_block = False
        elif self.direction != Vector2(0,0):
            body_cloned = self.body[:-1]
            body_cloned.insert(0, body_cloned[0] + self.direction)
            self.body = body_cloned[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0,0)

    def on_hold(self):
        self.direction = Vector2(0,0)