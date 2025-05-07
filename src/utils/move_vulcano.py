def move_vulcano(dart_pos: list[int], vulcano_pos: list[int], vulcano_speed: int):
    """Mueve al enemigo hacia el jugador."""
    dx = dart_pos[0] - vulcano_pos[0]
    dy = dart_pos[1] - vulcano_pos[1]
    distance = max(1, (dx**2 + dy**2) ** 0.5)
    dx = dx / distance
    dy = dy / distance
    vulcano_pos[0] += dx * vulcano_speed
    vulcano_pos[1] += dy * vulcano_speed
