import pygame, sys
from pygame.math import Vector2
from utils import screen, menu_bg, cell_size, cell_number, clock, grass_land
from package.button import Button
from package.game import Game

pygame.init()
pygame.display.set_caption('Snakes Game by Python - UIT')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

game = Game()

def get_font(size):
    return pygame.font.Font("./graphics/font/menu.ttf", size)

def play():
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
            running = False

        # draw all elements
        pygame.display.update()
        # frame rate
        clock.tick(60)
    

def main():
    while True:
        screen.blit(menu_bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(cell_size * 2).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(cell_size * (cell_number / 2), cell_size * 2))

        PLAY_BUTTON = Button(image=pygame.image.load("graphics/menu/play_rect.png"), pos=(cell_size * (cell_number / 2), 250), text_input="PLAY", font=get_font(cell_size), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("graphics/menu/option_rect.png"), pos=(cell_size * (cell_number / 2), 400), text_input="OPTIONS", font=get_font(cell_size), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("graphics/menu/quit_rect.png"), pos=(cell_size * (cell_number / 2), 550), text_input="QUIT", font=get_font(cell_size), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # options()
                    print('Option')
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

main()