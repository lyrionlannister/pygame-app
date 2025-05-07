import os
import pygame
from typing import List


def load_characters(
    relative_path: str = "src/images/characters",
    character_names: list[str] = ["dart", "vulcano"],
) -> List[pygame.Surface]:
    """
    Carga las imagenes desde el directorio: src/images/characters
    Las imagenes deben ser formato png

    Returns:
        List[pygame.Surface]: lista de imagenes cargadas
    """
    characters: List[pygame.Surface] = []

    image_path = os.path.abspath(relative_path)

    print(f"Loading images from: {image_path}")

    for name in character_names:

        print(f"Loading image from: {image_path}")
        try:
            image = pygame.image.load(f"{image_path}\{name}.png").convert_alpha()
            characters.append(image)
            print(f"Loaded image: {image_path}")
        except pygame.error as e:
            print(f"Error loading image {image_path}: {e}")

    return characters
