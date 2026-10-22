from share import check_path, parse_value


def total_salary(path: str) -> tuple[int, float | int] | None:
    """
    calculate total and average salary from file, only if all data in file is correct
    :param path: existing path to file
    :return: (total_salary: int, average_salary: float | int) or None on error
    """
    total = 0
    c = 0
    try:
        check_path(path)
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                s_line = line.split(',')
                if len(s_line) <= 1:
                    raise Exception(f"lein '{line}' have only one value")
                salary = parse_value(s_line[1], int, 'salary')
                total += salary
                c += 1
        return total, total / c
    except Exception as e:
        print(f'Error total_salary: {e}')
