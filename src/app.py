import pygame
from utils.create_main_menu import create_main_menu
from config.window_settings import WindowSettings


def start_game():
    print("Starting game...")


def show_options():
    print("Showing options...")


def app():
    pygame.init()
    screen = pygame.display.set_mode((WindowSettings.WIDTH, WindowSettings.HEIGHT))
    pygame.display.set_caption("Game Menu")

    menu = create_main_menu(start_game, show_options)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        menu.update(events)
        menu.draw(screen)

        pygame.display.flip()
