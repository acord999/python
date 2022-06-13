from sys import argv

with open('bakery.csv', 'r', encoding='UTF-8') as bakery:
    if (len(argv[1:]) == 1) and (argv[1].isdigit()):
        i = 0
        for line in bakery:
            if i >= int(argv[1]) - 1:
                print(line.replace('\n', ''))
            i += 1
    elif len(argv[1:]) == 2 and (argv[1].isdigit() and argv[2].isdigit()):
        i = 0
        for line in bakery:
            if (i >= (int(argv[1]) - 1)) and (i <= int(argv[2]) - 1):
                print(line.replace('\n', ''))
            i += 1
    else:
        for line in bakery:
            print(line.replace('\n', ''))
