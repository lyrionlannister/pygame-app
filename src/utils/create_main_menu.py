import pygame_menu
import pygame_menu.events

from config.window_settings import WindowSettings


def create_main_menu(start_game: callable) -> pygame_menu.Menu:
    """
    Crea el menú principal del juego.

    Returns:
        Menu: Un objeto pygame_menu.Menu con botones preconfigurados.
    """
    menu = pygame_menu.Menu(
        "Menú Principal",
        WindowSettings.WIDTH,
        WindowSettings.HEIGHT,
        theme=pygame_menu.themes.THEME_DARK,
    )
    menu.add.button("Play", start_game)
    menu.add.button("Quit", pygame_menu.events.EXIT)
    return menu
