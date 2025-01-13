import pygame, sys
from pygame.math import Vector2
from utils import screen, menu_bg, cell_size, cell_number, clock, grass_land, title, white, button_base_color
from package.button import Button
from package.game import Game

pygame.init()
pygame.display.set_caption('Snakes Game by Python - UIT')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

game = Game()

def get_font(size):
    return pygame.font.Font("./graphics/font/menu.ttf", size)

def restart():
    running = True
    while running:
        MOUSE_POS = pygame.mouse.get_pos()

        SCORE_TEXT = get_font(cell_size * 2).render("SCORE", True, title)
        TEXT_RECT = SCORE_TEXT.get_rect(center=(cell_size * (cell_number / 2), cell_size * 2))

        SCORE_VALUE = get_font(cell_size * 2).render(game.score, True, (white))
        VALUE_RECT = SCORE_VALUE.get_rect(center=(cell_size * (cell_number / 2), 250))

        RESTART_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 400), text_input="RESTART", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))
        RETURN_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 550), text_input="RETURN", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))

        screen.blit(SCORE_TEXT, TEXT_RECT)
        screen.blit(SCORE_VALUE, VALUE_RECT)

        for button in [RESTART_BUTTON, RETURN_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(MOUSE_POS):
                    print("RESTART")
                    game.restart = True
                    running = False
                    play(game.level)
                if RETURN_BUTTON.checkForInput(MOUSE_POS):
                    game.restart = False
                    running = False


        # draw all elements
        pygame.display.update()
        # frame rate
        clock.tick(60)

def start():
    running = True
    while running:
        screen.blit(menu_bg, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        LEVEL_TEXT = get_font(cell_size * 2).render("LEVEL", True, title)
        LEVEL_RECT = LEVEL_TEXT.get_rect(center=(cell_size * (cell_number / 2), cell_size * 2))

        EASY_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 250), text_input="EASY", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))
        NORMAL_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 400), text_input="NORMAL", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))
        HARD_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 550), text_input="HARD", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))

        RETURN_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 700), text_input="RETURN", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))

        screen.blit(LEVEL_TEXT, LEVEL_RECT)

        for button in [EASY_BUTTON, NORMAL_BUTTON, HARD_BUTTON, RETURN_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(MOUSE_POS):
                    play(1)
                    running = False
                if NORMAL_BUTTON.checkForInput(MOUSE_POS):
                    play(2)
                    running = False
                if HARD_BUTTON.checkForInput(MOUSE_POS):
                    play(3)
                    running = False
                if RETURN_BUTTON.checkForInput(MOUSE_POS):
                    running = False

        # draw all elements
        pygame.display.update()
        # frame rate
        clock.tick(60)

def play(level):
    if level == 1:
        game.level = 1
        pygame.time.set_timer(SCREEN_UPDATE, 200)
    elif level == 2:
        game.level = 2
        pygame.time.set_timer(SCREEN_UPDATE, 150)
    elif level == 3:
        game.level = 3
        pygame.time.set_timer(SCREEN_UPDATE, 50)
        
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if game.snake.direction.y != 1:
                        game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if game.snake.direction.y != -1:
                        game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if game.snake.direction.x != 1:
                        game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if game.snake.direction.x != -1:
                        game.snake.direction = Vector2(1, 0)

        if game.start == True:
            screen.fill(grass_land)
            game.draw_element()
        else:
            screen.fill((0,0,0))
            game.start = True
            restart()
            if game.restart == False:
                running = False

        # draw all elements
        pygame.display.update()
        # frame rate
        clock.tick(60)

def high_score():
    running = True
    while running:
        screen.blit(menu_bg, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        HIGH_SCORE_TEXT = get_font(cell_size * 2).render("HIGH SCORE", True, title)
        HIGH_SCORE_RECT = HIGH_SCORE_TEXT.get_rect(center=(cell_size * (cell_number / 2), cell_size * 2))

        RETURN_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 550), text_input="RETURN", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))

        screen.blit(HIGH_SCORE_TEXT, HIGH_SCORE_RECT)

        RETURN_BUTTON.changeColor(MOUSE_POS)
        RETURN_BUTTON.update(screen)
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(MOUSE_POS):
                    print("RETURN")
                    running = False
                    main()

        pygame.display.update()
        clock.tick(60)

def main():
    while True:
        screen.blit(menu_bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(cell_size * 2).render("MAIN MENU", True, title)
        MENU_RECT = MENU_TEXT.get_rect(center=(cell_size * (cell_number / 2), cell_size * 2))

        START_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 250), text_input="START", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))
        HIGH_SCORE_BUTTON = Button(image=pygame.image.load("graphics/menu/option_rect.png"), pos=(cell_size * (cell_number / 2), 400), text_input="HIGH SCORE", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))
        QUIT_BUTTON = Button(image=pygame.image.load("graphics/menu/quit_rect.png"), pos=(cell_size * (cell_number / 2), 550), text_input="QUIT", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [START_BUTTON, HIGH_SCORE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("PLAY")
                    start()
                if HIGH_SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print('HIGH_SCORE')
                    high_score()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print('QUIT')
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

main()