from typing import Callable
from time import time


class Schedule:
    
    events: list[int, Callable[[], None]] = []
    
    @classmethod
    def post(cls, _time: float, on_event: Callable[[], None]):
        cls.events.append((_time + time(), on_event))
    
    @classmethod
    def update(cls):
        t = time()
        
        if len(cls.events) == 0:
            return
        
        i = 0
        while True:
            if cls.events[i][0] < t:
                cls.events.pop(i)[1]()
            else:
                i += 1
            if i == len(cls.events):
                return
