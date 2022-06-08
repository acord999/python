tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen():
    for i in range(len(tutors)):
        if i < len(klasses):
            yield tutors[i], klasses[i]
        else:
            yield tutors[i], None


if __name__ == '__main__':
    generator = gen()
    print(type(generator))
    while True:
        print(next(generator))
