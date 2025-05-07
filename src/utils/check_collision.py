import pygame


def check_collision(
    dart_pos: list[int], vulcano_pos: list[int], dart_size: tuple[int, int]
) -> bool:
    """Verifica si el personaje colide con el enemigo."""
    dart_rect = pygame.Rect(dart_pos[0], dart_pos[1], dart_size[0], dart_size[1])
    vulcano_rect = pygame.Rect(vulcano_pos[0], vulcano_pos[1], 64, 64)
    if dart_rect.colliderect(vulcano_rect):
        intersection = dart_rect.clip(vulcano_rect)
        intersection_area = intersection.width * intersection.height
        dart_area = dart_size[0] * dart_size[1]
        return intersection_area >= dart_area / 2
    return False
