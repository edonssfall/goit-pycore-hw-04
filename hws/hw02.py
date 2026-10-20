from share import check_path, parse_value


def get_cats_info(path: str) -> list[dict[str, str | int]] | None:
    cats = list()
    cats_keys = ['id', 'name', 'age']
    try:
        check_path(path)
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                s_line = line.rstrip('\n').split(',')
                if not len(s_line) == 3:
                    raise Exception(f'Error {line} have not 3 values')
                parse_value(s_line[2], int, 'age')

                cats.append(dict(zip(cats_keys, s_line)))
        return cats
    except Exception as e:
        print(f'Error get_cats_info: {e}')
