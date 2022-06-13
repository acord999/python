def parser_users():
    with open('users.csv', encoding='UTF-8') as users:
        for line in users:
            yield ''.join(line.splitlines())


def parser_hobby():
    with open('hobby.csv', encoding='UTF-8') as hobby_file:
        for line in hobby_file:
            yield ''.join(line.splitlines())


lst_users = parser_users()
lst_hobby = parser_hobby()

while True:
    try:
        hobby = next(lst_hobby)
    except StopIteration:
        hobby = None
    try:
        user = next(lst_users)
        with open('users_hobby.txt', 'a', encoding='UTF-8') as res:
            res.write(f'{user}: {hobby} \n')
    except StopIteration:
        if hobby:
            exit(1)
        else:
            break
