import logging as log
from traceback import format_exc
from argparse import ArgumentParser, BooleanOptionalAction

from src.utils.logger import init_logger


if __name__ == "__main__":
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
    
    except SystemExit:
        pass
    
    except:        
        error = format_exc()
        log.error(error)
        
        if not args.debug:
            from src.display.error_window import show_game_crash_window
            show_game_crash_window(error)
