def get_jokes(n, repeats=True):
    """
    This function creates n number of jokes from random words.

    :param n: numbers of jokes
    :param repeats: = True, the words in the jokes may be repeated,
    :param repeats: = False the words in the jokes will be unique
    :return: a list of jokes
    """
    from random import randint
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []
    if repeats:
        for i in range(n):
            num = [randint(0, 4) for j in range(0, 3)]
            result.append(f'{nouns[num[0]]} {adverbs[num[1]]} {adjectives[num[2]]}')
    else:
        _cnt = 4
        for i in range(n):
            num = [randint(0, _cnt) for j in range(0, 3)]
            result.append(f'{nouns.pop(num[0])} {adverbs.pop(num[1])} {adjectives.pop(num[2])}')
            _cnt -= 1
    return result


print(get_jokes(5, repeats=False))
