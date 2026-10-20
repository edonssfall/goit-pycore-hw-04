import pathlib
import sys

from colorama import Fore, init

from share import check_path


def process_path(path, prefix=Fore.BLUE):
    """
    recursive function to go as deep as possible into folder and concatenate all strings into one
    :param path: must be an existing path
    :param prefix: folder color and tree lines of parent levels
    :return: tree as string, empty if folder can't be read
    """
    res = str()
    try:
        check_path(path)
    except Exception as e:
        print(Fore.RED + f'Error: {e}')
        return res

    items = sorted(pathlib.Path(path).iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    l_items = len(items)

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
        check_path(path)
        if not pathlib.Path(path).is_dir():
            raise Exception("path must be a dir")

        init(autoreset=True)

        result = Fore.YELLOW + ' 📦' + pathlib.Path(path).name + '\n'
        result += process_path(path).rstrip()

        print(result)
    except Exception as e:
        print(f'Error: {e}')
