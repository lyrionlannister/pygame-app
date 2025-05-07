import time


def update_score(last_score_time: float, score: int) -> tuple[float, int]:
    """Actualiza en pantalla la puntuación del jugador."""
    current_time = time.time()
    if current_time - last_score_time >= 1.0:
        score += 2
        last_score_time = current_time
    return last_score_time, score
