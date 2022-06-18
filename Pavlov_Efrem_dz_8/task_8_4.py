def val_checker(val_func):
    from functools import wraps

    def decorate(func):
        @wraps(func)
        def result(x):
            if val_func(x):
                return func(x)
            else:
                msg = f'wrong val {x}'
                raise ValueError(msg)

        return result

    return decorate


@val_checker(lambda x: x > 0)
def calc_cube(n):
    return n ** 3


if __name__ == '__main__':
    a = calc_cube(5)
    print(a)
    print(calc_cube.__name__)
