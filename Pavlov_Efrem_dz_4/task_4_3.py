def currency_rates(code):
    from requests import get
    import datetime
    response = str(get('http://www.cbr.ru/scripts/XML_daily.asp').content).split('</Valute>')
    keys, values = [], []
    for data in response:
        data = data.split('<')
        for obj in data:
            if obj.startswith('CharCode>'):
                keys.append(obj[9:])
            elif obj.startswith('Value>'):
                values.append(float(obj[6:].replace(',', '.')))
            elif obj.startswith('ValCurs Date="'):
                date = obj[14:24]
                dd, mm, yy = map(int, date.split('.'))
                date = datetime.date(yy, mm, dd)
    currency = dict(zip(keys, values))
    if currency.get(code.upper()):
        return currency.get(code.upper()), date


# Тестирование
if __name__ == '__main__':
    func = currency_rates('USD')
    if func:
        print(*func, sep=', ')
        for i in func:
            print(type(i))
