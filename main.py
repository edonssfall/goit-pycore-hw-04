from hws import total_salary, get_cats_info

if __name__ == '__main__':
    file = 'assets/salary.txt'
    if t_salary := total_salary(file):
        print('Загальна сума заробітної плати: %s, Середня заробітна плата: %s' % t_salary)
    else:
        print(f"'total_salary' Not processable file - {file}")

    file = 'assets/cats.txt'
    if cats := get_cats_info(file):
        print(cats)
    else:
        print(f"'get_cats_info': Not processable file - {file}")
