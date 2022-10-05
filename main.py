import logging as log
from traceback import format_exc
from argparse import ArgumentParser, BooleanOptionalAction

from src.logger import init_logger


if __name__ == '__main__':
    parser = ArgumentParser(description="Start Dungeon of Clemenceau")
    parser.add_argument(
        "-d", "--debug",
        help="Launch the game in debug mode",
        dest="debug",
        action=BooleanOptionalAction
    )
    args = parser.parse_args()
    
    # Start logger
    init_logger(args.debug)

    # Start game
    try:
        from src.game import Game

        Game.start()
    
    except:
        log.error(format_exc())
