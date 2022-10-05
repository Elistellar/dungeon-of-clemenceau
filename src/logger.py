import logging as log
import os
from datetime import datetime

from src.utils.path import path


def init_logger(debug: bool):
    
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    
    if not debug:
        filename = datetime.now().strftime('%Y-%m-%d %Hh%M.log')
        
        log.basicConfig(
            format='[%(asctime)s] [%(threadName)s] [%(levelname)s] %(message)s',
            datefmt='%H:%M:%S',
            level=log.DEBUG,
            handlers=[
                log.FileHandler(path('logs/' + filename), encoding='utf-8'),
                log.StreamHandler()
            ]
        )
