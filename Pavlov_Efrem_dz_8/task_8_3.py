def type_logger(func):
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        result = [func(n) for n in all_args]
        print(', '.join([f'{func.__name__}({n}:{type(n)})' for n in all_args]))
        return result

    return wrapper


@type_logger
def calc_cube(n):
    return n ** 3


if __name__ == '__main__':
    a = calc_cube(5, 4, 7, val=4)
    print(calc_cube.__name__)
    print(a)
