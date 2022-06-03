def thesaurus(*names):
    """
    Sorts names by first letter.

    :param names: Name for sort
    :return: dictionary of names sorted by first letter.
    """
    dict_names = {}
    for name in names:
        first_letter = name[0]
        if dict_names.get(first_letter):
            dict_names[first_letter].append(name)
        else:
            dict_names[first_letter] = [name]
    return dict_names


result = thesaurus("Иван", "Мария", "Петр", "Илья")
print(result)
