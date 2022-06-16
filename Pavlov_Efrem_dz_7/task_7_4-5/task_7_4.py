def statistic_folder(path):
    sizes = {}
    import os
    for root, dirs, files in os.walk(path):
        for file in files:
            mem = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            sizes[mem] = sizes.get(mem, 0) + 1
    return sizes


if __name__ == '__main__':
    # Задал папку
    folder_path = './test'
    print(statistic_folder(folder_path))
