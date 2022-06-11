result = []
with open('nginx_logs', 'r', encoding='UTF-8') as logs:
    for line in logs:
        _tmp = line.split()
        result.append((_tmp[0], _tmp[5][1:], _tmp[6]))
print(result)