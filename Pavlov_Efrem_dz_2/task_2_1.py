operations = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
for result in operations:
    result_type = str(type(result)).split("'")[1]
    print(f'Тип данных {result_type}')
