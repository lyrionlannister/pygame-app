# 🎩 Pygame App

Este es un pequeño juego hecho con [Pygame](https://www.pygame.org/) donde controlas un personaje y evitas colisiones con un enemigo que te persigue. Incluye un menú principal, detección de colisiones y sistema de puntajes.

## 📂 Estructura del proyecto

```
src/
├── app.py                  # Lógica principal del juego
├── main.py                 # Punto de entrada del juego
├── config/                 # Configuraciones generales
│   ├── characters_settings.py
│   ├── game_settings.py
│   └── window_settings.py
├── images/
│   └── characters/         # Sprites de personajes
│       ├── dart.png
│       └── vulcano.png
├── memory/                 # Datos persistentes como puntajes y jugadores (Proximamente)
│   ├── players.json
│   └── scores.json
└── utils/                  # Funciones auxiliares
    ├── check_collision.py
    ├── create_main_menu.py
    ├── create_menu.py
    ├── display_game_over.py
    ├── handle_input.py
    ├── load_characters.py
    ├── move_vulcano.py
    ├── player_manager.py
    ├── register_player_menu.py
    ├── score_manage.py
    └── update_score.py
```

## 🚀 Cómo ejecutar el juego

### 1. Clona el repositorio

```bash
git clone https://github.com/lyrionlannister/pygame-app.git
cd pygame-app
```

### 2. No es necesario que crees un entorno virtual uv lo hará por ti, pero asegurate de intalar uv

```bash
pip install uv
```

### 3. Instala las dependencias

```bash
uv pip install -r requirements.txt
```

### 4. Ejecuta el juego

```bash
py -B src/main.py
```

## 🎮 Controles

- Flechas de dirección: Mover al personaje
- ESC: Regresar al menú principal
- El personaje enemigo se mueve automáticamente hacia ti

## 🧠 Características

- Menú principal interactivo (con `pygame_menu`)
- Movimiento fluido del personaje
- Enemigo que te sigue
- Colisiones con detección de "game over"
- Sistema de puntaje que aumenta con el tiempo
- Modularidad en el código para facilitar la escalabilidad

## 📸 Recursos

- Imágenes de personajes en `src/images/characters/`
- Datos persistentes en `src/memory/` (jugadores y puntuaciones) (En desarrollo)

## 🛠️ Requisitos

- Python 3.12
- pygame 2.6.1
- pygame_menu 4.5.2
