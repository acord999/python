def templates_organizer(path, rm_original=False):
    """
    Copying templates files from original folder
    Keyword arguments:
    path -- path to project folder
    rm_original -- recursion remove original templates folder
    """
    import os
    from shutil import copy, rmtree
    paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                path_file = os.path.join(root, file)
                paths.append(path_file)

    for single_path in paths:
        new_path = os.path.join(path, 'templates', single_path.split('/')[-2])
        os.makedirs(new_path, exist_ok=True)
        print(f'Copying from {single_path} to {new_path}')
        copy(single_path, new_path)
    if rm_original:
        for single_path in paths:
            single_path = single_path.split('/')
            if os.path.exists(os.path.join(*single_path[:-2])):
                rmtree(os.path.join(*single_path[:-2]))


if __name__ == '__main__':
    templates_organizer('./my_project')
