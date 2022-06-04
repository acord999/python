def currency_rates(code):
    from requests import get
    from decimal import Decimal
    response = str(get('http://www.cbr.ru/scripts/XML_daily.asp').content).split('</Valute>')
    keys, values = [], []
    for data in response:
        data = data.split('<')
        for obj in data:
            if obj.startswith('CharCode>'):
                keys.append(obj[9:])
            elif obj.startswith('Value>'):
                values.append(Decimal(obj[6:].replace(',', '.')))
    currency = dict(zip(keys, values))
    return currency.get(code.upper())


print(currency_rates('USD'))
