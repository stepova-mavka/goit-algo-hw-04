from colorama import Fore
from pathlib import Path

def get_path():
    path = Path(input('Please enter the path to directory: ')) # create Path object for further path processing
    if path.exists():
        return path
    else:
        return 'Invalid path!!!!!'


def lookup_sub_dir(path:Path, space = ""): #space for clearer folder stucture in output
    for p in path.iterdir():
        if p.is_dir():
            print(space + Fore.BLUE + p.name + "\\" + Fore.RESET)
            lookup_sub_dir(p, space + "    ")
        else:
            print(space + Fore.GREEN + p.name + Fore.RESET)

    
directory_path = get_path()
lookup_sub_dir(directory_path)