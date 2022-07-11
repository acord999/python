class IsDigitError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


if __name__ == '__main__':
    res = list()
    while True:
        try:
            inp = input()
            if inp == 'stop':
                break
            elif not inp.isdigit():
                raise IsDigitError()
            else:
                res.append(inp)
        except IsDigitError:
            print('Incorrect input. Input must be digit.')
    print(res)
