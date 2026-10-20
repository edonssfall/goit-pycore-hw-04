import os


def check_path(path):
    if not path:
        raise Exception(f'path must be set')

    if not os.path.exists(path):
        raise Exception(f'{path} is not exists or dont have enough permissions')


def parse_value(value, type, name):
    try:
        return type(value)
    except Exception:
        raise Exception(f'{name}: {value} have not valid format')
