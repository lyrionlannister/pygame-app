import time

import pygame


class GameSettings:
    score: int = 0
    last_score_time: float = time.time()
    game_over: bool = False

    running: bool = True
    clock: pygame.time.Clock = pygame.time.Clock()
    game_state: str = "MENU"
