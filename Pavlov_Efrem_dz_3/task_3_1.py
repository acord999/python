def num_translate(number):
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
    return en_ru_dictionary.get(number)


print(num_translate('ten'))
