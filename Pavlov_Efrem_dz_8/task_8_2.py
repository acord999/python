def web_log_parser(log_file):
    import re
    pattern = re.compile(r'([a-z\d].{4,37}) \- \- \[(.*)\] \"(\w*) ([\w\/]*) .*\" (\d*) (\d*)')
    with open(log_file, 'r', encoding='UTF-8') as logs:
        data = logs.read()
    return pattern.findall(data)


if __name__ == '__main__':
    res_2 = web_log_parser('nginx_logs')
    for item in res_2:
        print(item)
