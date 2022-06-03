def currency_rates(code):
    from requests import get
    response = str(get('http://www.cbr.ru/scripts/XML_daily.asp').content).split('</Valute>')
    keys, values = [], []
    for data in response:
        data = data.split('<')
        for key in data:
            if key.startswith('CharCode>'):
                keys.append(key[9:])
        for value in data:
            if value.startswith('Value>'):
                values.append(float(value[6:].replace(',', '.')))
    currency = dict(zip(keys, values))
    return currency.get(code.upper())


print(currency_rates('USD'))
