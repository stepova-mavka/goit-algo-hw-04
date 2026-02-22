import sys
from colorama import (Fore, init,)
from pathlib import Path

init()

def get_path(cmd_path):
    path = Path(cmd_path) # create Path object for further path processing
    return path


def lookup_sub_dir(path:Path, space = ""): #space for clearer folder stucture in output
    for p in path.iterdir():
        try:
            if p.is_dir():
                print(space + Fore.BLUE + p.name + "/" + Fore.RESET)
                lookup_sub_dir(p, space + "    ")
            else:
                print(space + Fore.GREEN + p.name + Fore.RESET)
        except PermissionError:
            print(Fore.RED + "Insufficient permissions to show path contents!" + Fore.RESET)


def main():
    if len(sys.argv) > 1: 
        directory_path = get_path(sys.argv[1])
    else:
        print(Fore.RED + "No path inutted!" + Fore.RESET)
        sys.exit(1)

    if directory_path.exists() and directory_path.is_dir():
        lookup_sub_dir(directory_path)
    else:
        print(Fore.RED + "Invalid path!" + Fore.RESET)
        sys.exit(1)


main()