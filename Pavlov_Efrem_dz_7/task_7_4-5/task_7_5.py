def statistic_folder(path):
    sizes = {}
    import os
    for root, dirs, files in os.walk(path):
        for file in files:
            mem = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            ex = os.path.join(root, file).split('.')[-1]
            sizes[mem] = sizes.get(mem, (0, []))
            cnt, ex_lst = sizes[mem]
            if ex not in ex_lst:
                ex_lst.append(ex)
            cnt += 1
            sizes[mem] = (cnt, ex_lst)

    return sizes


if __name__ == '__main__':
    import json
    # Задал папку
    folder_path = './test'
    result = statistic_folder(folder_path)
    print(result)
    with open(fr'{folder_path[2:]}_summary.json', 'w', encoding='UTF-8') as res:
        json.dump(result, res)
