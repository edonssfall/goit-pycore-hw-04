import pathlib
import sys

from colorama import Fore, init

from share import check_path


def process_path(path, prefix=Fore.BLUE):
    try:
        check_path(path)
    except Exception as e:
        print(f'Error: {e}')

    items = sorted(pathlib.Path(path).iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    l_items = len(items)

    res = str()
    for i, item in enumerate(items):
        res += prefix
        last = i == l_items - 1
        connector = ' ┗ ' if last else ' ┣ '

        if item.is_file():
            res += Fore.GREEN + connector + "📜" + item.name + '\n'
        elif item.is_dir():
            res += connector + "📂" + item.name + '\n'

            res += process_path(str(item), prefix=prefix + (' ┃' if not last else '  '))

    return res


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise Exception("path mus be provided as argument")
        path = sys.argv[1]

        init(autoreset=True)

        result = Fore.YELLOW + ' 📦' + pathlib.Path(path).name + '\n'
        result += process_path(path).rstrip()

        print(result)
    except Exception as e:
        print(f'Error: {e}')
