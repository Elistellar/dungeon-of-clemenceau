from pathlib import Path


BASE_PATH = Path(__file__).parent.parent.parent

def path(relative_path: str) -> Path:
    abs_path = BASE_PATH
    for d in relative_path.split("/"):
        abs_path /= d
    return abs_path
