#!/usr/bin/env python3

"""
    Usage: python -m brain_games.scripts.brain_progression
"""

from brain_games.games import engine
from brain_games.games import progression as game


def main():
    engine.run_game(game)


if __name__ == '__main__':
    main()
