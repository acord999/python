weather_info = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
length = len(weather_info)
i = 0
while i < length:
    info_obj = weather_info[i]
    if info_obj.isdigit():
        weather_info[i] = info_obj.zfill(2)
        weather_info.insert(i, '"')
        weather_info.insert(i + 2, '"')
        length += 2
        i += 2
    elif info_obj.startswith('+') and info_obj[1:].isdigit():
        weather_info[i] = f'+{info_obj[1:].zfill(2)}'
        weather_info.insert(i, '"')
        weather_info.insert(i + 2, '"')
        length += 2
        i += 2
    i += 1
i = 0
weather_info_str = ''
while i < length:
    if weather_info[i] == '"':
        weather_info_str += f'{weather_info[i]}{weather_info[i + 1]}{weather_info[i + 2]} '
        i += 3
    else:
        weather_info_str += f'{weather_info[i]} '
        i += 1
print(weather_info)
print(weather_info_str)
