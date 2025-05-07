from dataclasses import dataclass


@dataclass
class WindowSettings:
    """Class to hold window settings for the application."""

    WIDTH: int = 1280
    HEIGHT: int = 720
    INIT_X: int = 0
    INIT_Y: int = 0
    FRAMES_PER_SECOND: int = 60
