import pygame, sys, random
from pygame.math import Vector2

# custom color
grass_land = (167, 209, 61)
grass_bush = (95,172,0)
fruit_color = (126, 166, 114)
snake_color = (183, 111, 122)
white = (0, 0, 0)
start_button = (0, 255, 0)

class SNAKE:
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
        # for block in self.body:
        #     x_pos = block.x * cell_size
        #     y_pos = block.y * cell_size
        #     block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        #     pygame.draw.rect(screen, snake_color, block_rect)
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
        else:
            body_cloned = self.body[:-1]
            body_cloned.insert(0, body_cloned[0] + self.direction)
            self.body = body_cloned[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0,0)

class FRUIT:
    def __init__(self):
        self.random_position()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        # pygame.draw.rect(screen, fruit_color, fruit_rect)

    def random_position(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
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
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number :
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

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
        score_text = str(len(self.snake.body) - 3)
        score_surface = font.render(str(score_text), True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left - 20, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left - 10, apple_rect.top, apple_rect.width + score_rect.width + cell_size, apple_rect.height)
        
        pygame.draw.rect(screen, (255, 255, 255), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

pygame.init()

cell_size = 40
cell_number = 20
pygame.display.set_caption('Snakes Game by Python - UIT')
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
font = pygame.font.Font(None, 25)
clock = pygame.time.Clock()
apple = pygame.image.load('graphics/apple.png').convert_alpha()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)


    screen.fill(grass_land)
    main_game.draw_element()
    # draw all elements
    pygame.display.update()

    # frame rate
    clock.tick(60)