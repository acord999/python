def currency_rates(code):
    from requests import get
    response = str(get('http://www.cbr.ru/scripts/XML_daily.asp').content).split('</Valute>')
    keys, values = [], []
    for data in response:
        data = data.split('<')
        for obj in data:
            if obj.startswith('CharCode>'):
                keys.append(obj[9:])
            elif obj.startswith('Value>'):
                values.append(float(obj[6:].replace(',', '.')))
    currency = dict(zip(keys, values))
    return currency.get(code.upper())


# Тестирую функцию
if __name__ == '__main__':
    print(currency_rates('GBP'))
    print(type(currency_rates('USD')))
    print(currency_rates('net takoi valuty'))
