for value in range(1, 101):
    value = str(value)
    if value not in ['11', '12', '13', '14']:
        if value[len(value) - 1] == '1':
            word = 'процент'
        elif value[len(value) - 1] in ['2', '3', '4']:
            word = 'процента'
        else:
            word = 'процентов'
    else:
        word = 'процентов'
    print(f'{value} {word}')
