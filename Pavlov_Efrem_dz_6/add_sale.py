from sys import argv


def writer(data):
    with open('bakery.csv', 'a', encoding='UTF-8') as out:
        out.write(f'{data} \n')


if __name__ == '__main__':
    exit(writer(argv[1]))
