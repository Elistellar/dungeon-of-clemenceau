from pathlib import Path
from typing import Callable


BASE_PATH = Path(__file__).parent.parent.parent

def path(r_path: str, on_not_found: Callable[[Path], None] = None, raise_on_not_found=True) -> Path:
    """
    Convert the given str path to a Path object cross platform.
    
    Parameters:
        r_path (str): A relative path form the project root directory.
        
    Returns (Path):
        An absolute path for the disk root directory.
    """
    abs_path = BASE_PATH
    for d in r_path.split("/"):
        abs_path /= d
    
    if not abs_path.exists():
        if on_not_found:
            on_not_found(abs_path)
        elif raise_on_not_found:
            raise FileNotFoundError(abs_path)
        
    return abs_path
