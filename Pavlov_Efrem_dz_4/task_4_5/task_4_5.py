from sys import argv
import utils

try:
    print(*utils.currency_rates(argv[1]), sep=', ')
except:
    print(None)
