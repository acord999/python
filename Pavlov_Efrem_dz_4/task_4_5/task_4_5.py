from sys import argv
import utils

# Решил добавить обработку ошибок, если нельзя не бейте. Основной функционал оставил без изменений.
try:
    print(*utils.currency_rates(argv[1]), sep=', ')
except TypeError:
    print(None)
except IndexError:
    print('Ошибка! Валюта не указанна.')
