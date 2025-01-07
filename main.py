import pygame, sys, random
from pygame.math import Vector2

# custom color
grass = (55, 140, 10)
fruit_color = (126, 166, 114)
snake_color = (183, 111, 122)

# class BACKGROUND:
#     def __init__(self):
#         self.background = pygame.image.load('graphics/grass_texture_background.jpg').convert_alpha()
    
#     def draw_background(self):
#         bg_rect = pygame.Rect(0, 0, cell_size * cell_number, cell_size * cell_number)
#         screen.blit(self.background, bg_rect)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_right = pygame.image.load('graphics/snake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('graphics/snake/head_left.png').convert_alpha()
        self.head_up = pygame.image.load('graphics/snake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('graphics/snake/head_down.png').convert_alpha()

        self.tail_up = pygame.image.load('graphics/snake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('graphics/snake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('graphics/snake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('graphics/snake/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('graphics/snake/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('graphics/snake/body_horizontal.png').convert_alpha()

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
                pygame.draw.rect(screen, (189, 242, 113), block_rect)

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
        # self.background.draw_background()
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.random_position()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number :
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        pygame.quit()
        sys.exit()

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
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


    screen.fill(grass)
    main_game.draw_element()

    # draw all elements
    pygame.display.update()

    # frame rate
    clock.tick(60)