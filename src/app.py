import time
import pygame

from config.characters_settings import *
from config.game_settings import GameSettings
from config.window_settings import WindowSettings
from utils.load_characters import load_characters
from utils.create_menu import create_menu
from utils.handle_input import handle_input
from utils.move_vulcano import move_vulcano
from utils.check_collision import check_collision
from utils.update_score import update_score
from utils.display_game_over import display_game_over


def app():
    """Función principal que maneja la ejecución del juego."""
    pygame.init()
    screen = pygame.display.set_mode((WindowSettings.WIDTH, WindowSettings.HEIGHT))
    pygame.display.set_caption("Game Menu")

    characters = load_characters()
    font = pygame.font.SysFont(None, 36)

    if not characters:
        print("No se pudo cargar ningún personaje.")
        return

    scaled_dart = pygame.transform.smoothscale(characters[0], DartSettings.dart_size)

    scaled_vulcano = pygame.transform.smoothscale(
        characters[1], VulcanoSettings.vulcano_size
    )

    def start_game_action():
        """Inicia el juego cuando se selecciona 'Play' en el menú."""

        GameSettings.score = 0
        DartSettings.dart_position = [100, 100]
        VulcanoSettings.vulcano_position = [400, 300]
        GameSettings.game_over = False
        GameSettings.last_score_time = time.time()
        GameSettings.game_state = "GAME"

    menu = create_menu(start_game_action)

    while GameSettings.running:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                GameSettings.running = False

        screen.fill((50, 50, 50))

        if GameSettings.game_state == "MENU":
            menu.update(events)
            menu.draw(screen)

        elif GameSettings.game_state == "GAME":
            if not GameSettings.game_over:
                handle_input(DartSettings.dart_position, DartSettings.dart_speed)
                move_vulcano(
                    DartSettings.dart_position,
                    VulcanoSettings.vulcano_position,
                    VulcanoSettings.vulcano_speed,
                )

                GameSettings.game_over = check_collision(
                    DartSettings.dart_position,
                    VulcanoSettings.vulcano_position,
                    DartSettings.dart_size,
                )
                GameSettings.last_score_time, GameSettings.score = update_score(
                    GameSettings.last_score_time, GameSettings.score
                )

            screen.blit(scaled_dart, DartSettings.dart_position)
            screen.blit(scaled_vulcano, VulcanoSettings.vulcano_position)

            score_text = font.render(
                f"Puntuación: {GameSettings.score}", True, (255, 255, 255)
            )
            screen.blit(score_text, (10, 10))

            if GameSettings.game_over:
                display_game_over(screen, font)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                GameSettings.game_state = "MENU"

        pygame.display.flip()
        GameSettings.clock.tick(WindowSettings.FRAMES_PER_SECOND)

    pygame.quit()
