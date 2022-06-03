def prices_printer(prices_lst):
    result = ''
    for price in prices_lst:
        price = str(price).split('.')
        price.append('00')
        result += f'{price[0]} руб {price[1].zfill(2)} коп, '
    print(result[:len(result) - 2])


prices = [74, 99.29, 82.85, 56, 33.51, 65.84, 96, 47.06, 95, 10.22, 21.15, 2.55, 55.17, 29.93]
prices_printer(prices)
print(f'Id before sort {id(prices)}')
prices.sort()
print(f'Id after sort {id(prices)}')
prices_printer(prices)
prices_2 = sorted(prices, reverse=True)
prices_printer(prices_2)
prices_printer(prices_2[:5])
