def parser_log():
    with open('nginx_logs', 'r', encoding='UTF-8') as logs:
        for line in logs:
            _tmp = line.split()
            yield _tmp[0]


if __name__ == '__main__':
    log = parser_log()
    db_ip = {}
    for ip in log:
        db_ip[ip] = db_ip.get(ip, 0) + 1
    spamer = max(db_ip.items(), key=lambda x: x[1])
    print(f'Spamer detected! \n IP: {spamer[0]} \n Количество запросов: {spamer[1]}')
