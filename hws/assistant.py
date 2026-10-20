import re
import sys

from colorama import Fore, init

CACHE = dict()


def validate_args(*args) -> tuple[str, str]:
    if len(args) != 2:
        raise Exception(f"Can't parse args, because it only 2 args accepted: {args}")
    name, phone = args
    if not re.fullmatch(r'[a-zA-Z]+', name):
        raise Exception(f"Can't add contact, because of invalid name: {name}")
    if not re.fullmatch(r'^\+?\d{9,12}', phone):
        raise Exception(f"Can't add contact, because of invalid phone: {phone}")
    return name, phone


def get_key(name: str):
    res = None
    l_name = name.lower()
    for key in CACHE.keys():
        if l_name == key.lower():
            res = key
            break
    return res


def add_contact(*args) -> str | None:
    name, phone = validate_args(*args)
    if key := get_key(name):
        CACHE[key] = phone
    else:
        CACHE[name] = phone
    return 'Contact added'


def change_contact(*args) -> str | None:
    name, phone = validate_args(*args)
    if key := get_key(name):
        CACHE[key] = phone
        return 'Contact updated'
    raise Exception(f"Can't show contact, because of invalid name: {name}")


def show_phone(*args) -> str | None:
    if len(args) != 1:
        raise Exception(f"Can't show contact, because of invalid args: {args}")
    name = args[0]
    if not re.fullmatch(r'[a-zA-Z]+', name):
        raise Exception(f"Can't add contact, because of invalid name: {name}")
    if key := get_key(name):
        return CACHE[key]
    raise Exception(f"Can't show contact, because of invalid name: {name}")


def show_all() -> str:
    if CACHE:
        return ''.join(
            f"{Fore.BLUE if i % 2 == 0 else Fore.YELLOW}{name}: {phone}\n"
            for i, (name, phone) in enumerate(CACHE.items())
        )
    return 'Nothing to show, because DB is empty'


def parse_input(user_input: str) -> tuple[str, list]:
    if not user_input.strip():
        raise Exception('Please enter a command.')
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            cmd, *args = parse_input(user_input)

            if cmd in ['close', 'exit']:
                raise EOFError
            match cmd:
                case 'hello':
                    print('How can I help you?')
                case 'add':
                    print(add_contact(*args))
                case 'change':
                    print(change_contact(*args))
                case 'phone':
                    print(show_phone(*args))
                case 'all':
                    print(show_all().rstrip())
                case _:
                    print(Fore.RED + 'Invalid command.')
        except EOFError:
            print('\nGood bye!')
            sys.exit()
        except Exception as e:
            print(Fore.RED + f'Error: {e}')


if __name__ == '__main__':
    init(autoreset=True)
    main()
