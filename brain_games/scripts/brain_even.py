#!/usr/bin/env python3

# Usage: python -m brain_games.scripts.brain_even

from brain_games.games import engine
from brain_games.games import even


def main():
    engine.run_game(even)


if __name__ == '__main__':
    main()
