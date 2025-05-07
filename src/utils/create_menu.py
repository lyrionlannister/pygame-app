import pygame_menu
from config.window_settings import WindowSettings


def create_menu(start_game_action: callable) -> pygame_menu.Menu:
    """Crea el menú principal."""
    menu = pygame_menu.Menu(
        "Menú Principal",
        WindowSettings.WIDTH,
        WindowSettings.HEIGHT,
        theme=pygame_menu.themes.THEME_DARK,
    )
    menu.add.button("Play", start_game_action)
    menu.add.button("Quit", pygame_menu.events.EXIT)
    return menu
