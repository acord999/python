import pickle

with open('users.csv', encoding='UTF-8') as users:
    lst_users = [''.join(line.splitlines()) for line in users]
with open('hobby.csv', encoding='UTF-8') as hobby:
    lst_hobby = [''.join(line.splitlines()) for line in hobby]

data = {}
if len(lst_hobby) <= len(lst_users):
    for i in range(len(lst_users)):
        try:
            data[lst_users[i]] = lst_hobby[i]
        except IndexError:
            data[lst_users[i]] = None
else:
    exit(1)
with open('result.pickle', 'wb') as res:
    pickle.dump(data, res)

with open('result.pickle', 'rb') as res:
    data_load = pickle.load(res)
    print(data_load)
    print(type(data_load))
