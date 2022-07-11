class MyZeroDiv(Exception):
    def __init__(self, *args):
        super().__init__(*args)


if __name__ == '__main__':
    a, b = map(int, input().split())
    try:
        if b == 0:
            raise MyZeroDiv('Zero Division Error')
        print(a / b)
    except MyZeroDiv as ex:
        print(ex)
