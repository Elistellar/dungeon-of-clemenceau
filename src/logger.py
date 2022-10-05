from cgitb import handler
import logging as log
import os
from datetime import datetime

from src.utils.path import path


def init_logger(debug: bool):
    
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    
    handlers = [
        log.StreamHandler()
    ]
    
    if not debug:
        filename = datetime.now().strftime('%Y-%m-%d %Hh%M.log')
        
        handlers.append(
            log.FileHandler(path('logs/' + filename, raise_on_not_found=False), encoding='utf-8')
        )
        
    log.basicConfig(
        format='[%(asctime)s] [%(threadName)s] [%(levelname)s] %(message)s',
        datefmt='%H:%M:%S',
        level=log.DEBUG,
        handlers=handlers
    )
