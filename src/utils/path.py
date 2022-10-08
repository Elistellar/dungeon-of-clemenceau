from os import makedirs
from pathlib import Path


BASE_PATH = Path(__file__).parent.parent.parent

def path(r_path: str, default_value: str = None) -> Path:
    """
    Convert the given str path to a Path object cross platform.
    
    Parameters:
        r_path (str): A relative path form the project root directory.
        default_value (str | None): Used when the file does not exists. If not None, create the file and write the value. Else, a FileNotFoundError will be raised.
        
    Returns (Path):
        An absolute path for the disk root directory.
    """
    abs_path = BASE_PATH
    for d in r_path.split("/"):
        abs_path /= d
    
    if not abs_path.exists():
        if default_value:
            # Create all directories leading to the path if they do not exist.
            for parent in abs_path.parents:
                if not parent.exists():
                    makedirs(parent)
            # Create the file
            abs_path.touch()
            # Write the default value
            with open(abs_path, "w", encoding="utf-8") as file:
                file.write(default_value)
            
        else:
            raise FileNotFoundError(abs_path)
        
    return abs_path
