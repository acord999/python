weather_info = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
weather_info_modified = []

for info_obj in weather_info:
    if info_obj.isdigit():
        weather_info_modified.extend(['"', info_obj.zfill(2), '"'])
    elif info_obj.startswith('+') and info_obj[1:].isdigit():
        weather_info_modified.extend(['"', f'+{info_obj[1:].zfill(2)}', '"'])
    else:
        weather_info_modified.append(info_obj)
length = len(weather_info_modified)
i = 0
weather_info_str = ''
while i < length:
    if weather_info_modified[i] == '"':
        weather_info_str += f'{weather_info_modified[i]}{weather_info_modified[i + 1]}{weather_info_modified[i + 2]} '
        i += 3
    else:
        weather_info_str += f'{weather_info_modified[i]} '
        i += 1
print(weather_info_modified)
print(weather_info_str)

