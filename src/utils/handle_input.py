import pygame
from config.window_settings import WindowSettings


def handle_input(dart_pos: list[int], dart_speed: int):
    """Maneja la entrada del jugador para mover el personaje."""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dart_pos[0] -= dart_speed
    if keys[pygame.K_RIGHT]:
        dart_pos[0] += dart_speed
    if keys[pygame.K_UP]:
        dart_pos[1] -= dart_speed
    if keys[pygame.K_DOWN]:
        dart_pos[1] += dart_speed

    dart_pos[0] = max(0, min(dart_pos[0], WindowSettings.WIDTH - 64))
    dart_pos[1] = max(0, min(dart_pos[1], WindowSettings.HEIGHT - 64))
