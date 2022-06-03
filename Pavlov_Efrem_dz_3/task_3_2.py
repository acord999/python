def num_translate_adv(number):
    """ Translating English numeral into Russian """
    en_ru_dictionary = {'zero': 'ноль',
                        'one': 'один',
                        'two': 'два',
                        'three': 'три',
                        'four': 'четыре',
                        'five': 'пять',
                        'six': 'шесть',
                        'seven': 'семь',
                        'eight': 'восемь',
                        'nine': 'девять',
                        "ten": 'десять'}
    if en_ru_dictionary.get(number):
        return en_ru_dictionary[number]
    elif en_ru_dictionary.get(number.lower()):
        return en_ru_dictionary[number.lower()].title()


print(num_translate_adv('zero'))
# print(help(num_translate_adv))
