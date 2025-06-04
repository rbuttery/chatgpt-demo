#!/usr/bin/env python3
"""Simple terminal-based snake game using curses."""

import curses
import random
from collections import deque


def main(stdscr: curses.window):
    # Initialize
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    sh, sw = stdscr.getmaxyx()
    box = [[3, 3], [sh - 3, sw - 3]]

    for y in range(box[0][0], box[1][0]):
        stdscr.addstr(y, box[0][1], "|" + " " * (box[1][1] - box[0][1] - 1) + "|")
    stdscr.refresh()

    snake = deque([
        [sh // 2, sw // 2 + 1],
        [sh // 2, sw // 2],
        [sh // 2, sw // 2 - 1],
    ])
    direction = curses.KEY_RIGHT

    food = [
        random.randint(box[0][0] + 1, box[1][0] - 1),
        random.randint(box[0][1] + 1, box[1][1] - 1),
    ]
    stdscr.addch(food[0], food[1], "*")

    score = 0

    while True:
        key = stdscr.getch()
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            direction = key

        head = snake[0].copy()
        if direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_DOWN:
            head[0] += 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            head[1] += 1

        if (
            head[0] in [box[0][0], box[1][0]]
            or head[1] in [box[0][1], box[1][1]]
            or head in snake
        ):
            msg = f"Game Over! Score: {score}"
            stdscr.nodelay(False)
            stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            stdscr.getch()
            break

        snake.appendleft(head)
        if head == food:
            score += 1
            food = [
                random.randint(box[0][0] + 1, box[1][0] - 1),
                random.randint(box[0][1] + 1, box[1][1] - 1),
            ]
            stdscr.addch(food[0], food[1], "*")
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], " ")

        stdscr.addch(head[0], head[1], "#")
        stdscr.refresh()
        curses.napms(100)


if __name__ == "__main__":
    curses.wrapper(main)
