def starter(project_name):
    import os
    main_path = fr'./{project_name}'
    if not os.path.exists(main_path):
        os.mkdir(main_path)
    required_folders = ['settings', 'mainapp', 'adminapp', 'authapp']
    for folder_name in required_folders:
        os.makedirs(os.path.join(main_path, folder_name), exist_ok=True)


if __name__ == '__main__':
    starter('my_project')
