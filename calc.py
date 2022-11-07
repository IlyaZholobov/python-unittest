def calc_func(sign):

    return {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
        '-': lambda a, b: a - b,
        '/': lambda a, b: a / b,
    }[sign]


def calc_sting(expression):
    signs = '+-*/'

    if type(expression) == 'string':
        raise ValueError('на вход строка')
    if not expression:
        raise ValueError('Пустая строка')

    for sign in signs:
        if sign in expression:
            try:
                left, right = [int(part) for part in expression.split(sign)]

                return calc_func(sign)(left, right)
            except ValueError:
                raise ValueError('два числа тип инт и один знак операции')


if __name__ == '__main__':
    print(calc_sting('2-2'))
