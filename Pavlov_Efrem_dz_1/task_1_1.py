duration = 400153
if duration > 0:
    if duration < 60:
        result = f'{duration} сек'
    elif duration < 3600:
        result = f'{duration // 60} мин {duration % 60} сек'
    elif duration < 86400:
        result = f'{duration // 3600} час {duration % 3600 // 60} мин {duration % 3600 % 60} сек'
    else:
        result = f'{duration // 86400} дн {duration % 86400 // 3600} час {duration % 86400 % 3600 // 60} мин {duration % 86400 % 3600 % 60} сек'
    print(result)
