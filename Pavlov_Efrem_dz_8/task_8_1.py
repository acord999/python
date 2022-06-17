def email_parse(email):
    import re
    pattern = re.compile(r'(([a-z\d._%-]+)@([a-z\d._-]+\.[a-z]{2,}))')
    if pattern.match(email):
        _, username, domain = pattern.findall(email)[0]
        return {'username': username, 'domain': domain}
    else:
        msg = f'wrong email: {email}'
        raise ValueError(msg)


if __name__ == '__main__':
    result = email_parse('conta1ct1@efrempavlov.ru')
    print(result)
