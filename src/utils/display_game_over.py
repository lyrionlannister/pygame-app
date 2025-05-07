import pygame

from config.window_settings import WindowSettings


def display_game_over(screen: pygame.Surface, font: pygame.font.Font):
    """Muestra la pantalla de Game Over."""
    game_over_text = font.render("¡GAME OVER!", True, (255, 0, 0))
    restart_text = font.render(
        "Presiona ESC para volver al menú", True, (255, 255, 255)
    )

    text_rect = game_over_text.get_rect(
        center=(WindowSettings.WIDTH // 2, WindowSettings.HEIGHT // 2)
    )
    restart_rect = restart_text.get_rect(
        center=(WindowSettings.WIDTH // 2, WindowSettings.HEIGHT // 2 + 40)
    )

    screen.blit(game_over_text, text_rect)
    screen.blit(restart_text, restart_rect)
