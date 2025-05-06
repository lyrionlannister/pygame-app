from dataclasses import dataclass


@dataclass
class WindowSettings:
    """Class to hold window settings for the application."""

    WIDTH: int = 800
    HEIGHT: int = 600
    INIT_X: int = 0
    INIT_Y: int = 0
