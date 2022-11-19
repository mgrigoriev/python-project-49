#!/usr/bin/env python3

"""
    Usage: python -m brain_games.scripts.brain_gcd
"""

from brain_games.games import engine
from brain_games.games import gcd as game


def main():
    engine.run_game(game)


if __name__ == '__main__':
    main()
