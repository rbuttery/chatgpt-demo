# chatgpt-demo

This repository demonstrates a simple setup for running Python scripts. The
`demo.py` script prints a short greeting. It can serve as a starting point for
more advanced experiments.

## Running the demo

```bash
python3 demo.py
```

## Installing dependencies

All scripts rely only on the Python standard library on Linux and macOS. If
you are running Windows, the `curses` module used by the snake game is not
bundled with Python. Install the `windows-curses` package first or use the
provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Playing the Snake game

A small terminal-based snake game is provided in `snake_game.py`. Use the arrow
keys to move the snake and eat the "*" food items. The game ends when the snake
collides with the border or itself.

```bash
python3 snake_game.py
```

**Note**: The game requires a fully featured terminal that supports the
`curses` library. In some minimal or web-based environments the game window may
not render correctly or may fail to start.
