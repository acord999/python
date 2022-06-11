import sys


def parser(path):
    with open(path, encoding='UTF-8') as fille:
        for line in fille:
            yield ''.join(line.splitlines())


def grouping(u_path, h_path, out):
    lst_hobby = parser(h_path)
    lst_users = parser(u_path)
    while True:
        try:
            hobby = next(lst_hobby)
        except StopIteration:
            hobby = None
        try:
            user = next(lst_users)
            with open(out, 'a', encoding='UTF-8') as res:
                res.write(f'{user}: {hobby} \n')
        except StopIteration:
            if hobby:
                return 1
            else:
                break


if __name__ == "__main__":
    users_path = ''
    hobby_path = ''
    out_path = ''
    if len(sys.argv[1:]) >= 3:
        users_path, hobby_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    if not users_path:
        users_path = "./users.csv"

    if not hobby_path:
        hobby_path = "./hobby.csv"

    if not out_path:
        out_path = "./out.txt"

exit(grouping(users_path, hobby_path, out_path))
