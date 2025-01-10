import pygame, sys
from utils import screen, menu_bg, cell_size, cell_number
from screen.play import play
from package.button import Button

pygame.init()
pygame.display.set_caption('Snakes Game by Python - UIT')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

def get_font(size):
    return pygame.font.Font("./graphics/font/menu.ttf", size)

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