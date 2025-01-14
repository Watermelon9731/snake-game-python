import pygame, sys
from os import path
from pygame.math import Vector2
from utils import screen, menu_bg, cell_size, cell_number, clock, grass_land, title, white, black, button_base_color
from package.button import Button
from package.game import Game

pygame.init()
pygame.display.set_caption('Snakes Game by Python - UIT')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

game = Game()

def save_high_score(score, file):
    # load high score
    dir = path.dirname(__file__)
    with open(path.join(dir, f"{file}.txt"), "w") as f:
        int(f.write(str(score)))

def get_high_score(file):
    # load high score
    dir = path.dirname(__file__)
    with open(path.join(dir, f"{file}.txt"), "r") as f:
        try:
            return int(f.read())
        except: 
            return 0

def get_font(size):
    return pygame.font.Font("./graphics/font/menu.ttf", size)

def restart():
    best_score = 0
    if game.level == 4:
        best_score = get_high_score('time_high_score')
    else:
        best_score = get_high_score('high_score')
    running = True
    while running:
        MOUSE_POS = pygame.mouse.get_pos()
        ADD_POS = 0

        if game.score > best_score:
            ADD_POS = 150

        SCORE_TEXT = get_font(cell_size * 2).render("SCORE", True, title)
        TEXT_RECT = SCORE_TEXT.get_rect(center=(cell_size * (cell_number / 2), cell_size * 2))

        HIGH_SCORE_TEXT = get_font(cell_size).render("NEW HIGH SCORE!", True, title)
        HIGH_SCORE_RECT = HIGH_SCORE_TEXT.get_rect(center=(cell_size * (cell_number / 2), 250))

        SCORE_VALUE = get_font(cell_size * 2).render(str(game.score), True, (white))
        VALUE_RECT = SCORE_VALUE.get_rect(center=(cell_size * (cell_number / 2), 250 + ADD_POS))

        RESTART_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 400 + ADD_POS), text_input="RESTART", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))
        RETURN_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 550 + ADD_POS), text_input="RETURN", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))

        screen.blit(SCORE_TEXT, TEXT_RECT)

        if game.score > best_score:
            screen.blit(HIGH_SCORE_TEXT, HIGH_SCORE_RECT)
            if game.level == 4:
                save_high_score(game.score, 'time_high_score')
            else:
                save_high_score(game.score, 'high_score')

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
                    print("RETURN")
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

        EASY_BUTTON = Button(image=pygame.image.load("graphics/menu/mode_rect.png"), pos=(cell_size * (cell_number / 2), 200), text_input="EASY", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))
        NORMAL_BUTTON = Button(image=pygame.image.load("graphics/menu/mode_rect.png"), pos=(cell_size * (cell_number / 2), 325), text_input="NORMAL", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))
        HARD_BUTTON = Button(image=pygame.image.load("graphics/menu/mode_rect.png"), pos=(cell_size * (cell_number / 2), 450), text_input="HARD", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))
        TIME_BUTTON = Button(image=pygame.image.load("graphics/menu/mode_rect.png"), pos=(cell_size * (cell_number / 2), 575), text_input="10 SECONDS", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))
        RETURN_BUTTON = Button(image=pygame.image.load("graphics/menu/mode_rect.png"), pos=(cell_size * (cell_number / 2), 700), text_input="RETURN", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))

        screen.blit(LEVEL_TEXT, LEVEL_RECT)

        for button in [EASY_BUTTON, NORMAL_BUTTON, HARD_BUTTON, TIME_BUTTON, RETURN_BUTTON]:
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
                if TIME_BUTTON.checkForInput(MOUSE_POS):
                    play(4)  # Mode 4 is time mode
                    running = False
                if RETURN_BUTTON.checkForInput(MOUSE_POS):
                    running = False

        pygame.display.update()
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
    elif level == 4:
        game.level = 4
        pygame.time.set_timer(SCREEN_UPDATE, 50)
        
    running = True
    paused = False
    pause_font = get_font(cell_size)
    
    pause_text = pause_font.render("PAUSED", True, white)
    pause_rect = pause_text.get_rect(center=(cell_size * (cell_number / 2), cell_size * (cell_number / 2)))
    
    start_time = None
    time_font = pygame.font.Font(None, 30)
    
    while running:
        if level == 4 and start_time is None:
            start_time = pygame.time.get_ticks()
        
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE and not paused:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.game_over()
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if not paused:
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
            
            if level == 4:
                if not paused:
                    elapsed_time = (current_time - start_time) // 1000
                    time_left = 10 - elapsed_time
                    if time_left <= 0:
                        game.start = False
                        game.game_over()
                    else:
                        time_text = time_font.render(f"Time: {time_left}s", True, black)
                        time_rect = time_text.get_rect(center=(cell_size + (cell_size / 2), (cell_size / 2)))
                        bg_time_rect = pygame.Rect(time_rect.x - 10, time_rect.y - 5, cell_size * 3, time_rect.height + 10)
                        pygame.draw.rect(screen, (255, 255, 255), bg_time_rect)
                        screen.blit(time_text, time_rect)
                        pygame.draw.rect(screen, (56, 74, 12), bg_time_rect, 2)
            
            if paused:
                pause_overlay = pygame.Surface((cell_size * cell_number, cell_size * cell_number))
                pause_overlay.fill((0, 0, 0))
                pause_overlay.set_alpha(128)
                screen.blit(pause_overlay, (0, 0))
                screen.blit(pause_text, pause_rect)
        else:
            screen.fill((0, 0, 0))
            game.start = True
            restart()
            if game.restart == False:
                running = False

        pygame.display.update()
        clock.tick(60)

def high_score():
    best_score = get_high_score('high_score')
    time_best_score = get_high_score('time_high_score')

    running = True
    while running:
        screen.blit(menu_bg, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        HIGH_SCORE_TEXT = get_font(cell_size).render("HIGH SCORE", True, title)
        HIGH_SCORE_RECT = HIGH_SCORE_TEXT.get_rect(center=(cell_size * (cell_number / 2), cell_size * 2))
        
        NORMAL_SCORE_TEXT = get_font(cell_size - 10).render("NORMAL MODE:", True, white)
        NORMAL_SCORE_RECT = NORMAL_SCORE_TEXT.get_rect(center=(cell_size * (cell_number / 2), 200))

        NORMAL_VALUE = get_font(cell_size - 10).render(str(best_score), True, (white))
        NORMAL_VALUE_RECT = NORMAL_VALUE.get_rect(center=(cell_size * (cell_number / 2), 300))
        
        TIME_SCORE_TEXT = get_font(cell_size - 10).render("Time Mode:", True, white)
        TIME_SCORE_RECT = TIME_SCORE_TEXT.get_rect(center=(cell_size * (cell_number / 2), 450))
        
        TIME_VALUE = get_font(cell_size - 10).render(str(time_best_score), True, white)
        TIME_VALUE_RECT = TIME_VALUE.get_rect(center=(cell_size * (cell_number / 2), 550))

        RETURN_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 700), text_input="RETURN", font=get_font(cell_size), base_color=button_base_color, hovering_color=(white))

        screen.blit(HIGH_SCORE_TEXT, HIGH_SCORE_RECT)
        screen.blit(NORMAL_SCORE_TEXT, NORMAL_SCORE_RECT)
        screen.blit(NORMAL_VALUE, NORMAL_VALUE_RECT)
        screen.blit(TIME_SCORE_TEXT, TIME_SCORE_RECT)
        screen.blit(TIME_VALUE, TIME_VALUE_RECT)

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