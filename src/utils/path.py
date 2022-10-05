from pathlib import Path


BASE_PATH = Path(__file__).parent.parent.parent

def path(r_path: str) -> Path:
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
    return abs_path
