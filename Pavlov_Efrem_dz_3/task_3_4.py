def thesaurus_adv(*names, alphabetically=False):
    """
    Sorts firsts and lasts names by first letter.

    :param names: Name for sort
    :type alphabetically: Return a dictionary sorted alphabetically by the first letter of last names.
    :return: dictionary of lasts names with dictionary sorted by first letter
    of firsts names sorted by first letter too.
    """
    dict_names = {}
    for name in names:
        f_name, l_name = name.split()
        l_first_letter = l_name[0]
        f_first_name = f_name[0]
        if dict_names.get(l_first_letter) and dict_names.get(l_first_letter).get(f_first_name):
            dict_names[l_first_letter][f_first_name].append(name)
        elif dict_names.get(l_first_letter):
            dict_names[l_first_letter].update({f_first_name: [name]})
        else:
            dict_names[l_first_letter] = {f_first_name: [name]}
    # Реализация сортировки по ключам
    if alphabetically:
        dict_names_sorted = {}
        for key in sorted(dict_names):
            dict_names_sorted[key] = dict_names[key]
        return dict_names_sorted
    else:
        return dict_names


result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", alphabetically=True)
print(result)
