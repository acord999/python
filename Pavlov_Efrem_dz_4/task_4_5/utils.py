def currency_rates(code):
    from requests import get
    from decimal import Decimal
    import datetime
    response = str(get('http://www.cbr.ru/scripts/XML_daily.asp').content).split('</Valute>')
    keys, values = [], []
    for data in response:
        data = data.split('<')
        for obj in data:
            if obj.startswith('CharCode>'):
                keys.append(obj[9:])
            elif obj.startswith('Value>'):
                values.append(Decimal(obj[6:].replace(',', '.')))
            elif obj.startswith('ValCurs Date="'):
                date = obj[14:24]
                dd, mm, yy = map(int, date.split('.'))
                date = datetime.date(yy, mm, dd)
    currency = dict(zip(keys, values))
    if currency.get(code.upper()):
        return [currency.get(code.upper()), date]


# Создал лишние команды, которые не должны выполниться при импорте
if __name__ == '__main__':
    print('Hello world!!!')
    for inf in currency_rates('amd'):
        print(inf)
