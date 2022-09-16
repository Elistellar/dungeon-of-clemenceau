from typing import Protocol

from pygame import Rect


class HasRect(Protocol):
    rect: Rect
