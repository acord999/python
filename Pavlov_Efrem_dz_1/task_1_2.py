cubed_lst = [number ** 3 for number in range(1, 1001, 2)]
result = 0
result_plus_17 = 0
for number in cubed_lst:
    num = 0
    tmp_number = number
    while tmp_number != 0:
        num += tmp_number % 10
        tmp_number //= 10
    if num % 7 == 0:
        result += number
    num = 0
    tmp_number = number + 17
    while tmp_number != 0:
        num += tmp_number % 10
        tmp_number //= 10
    if num % 7 == 0:
        result_plus_17 += number + 17

print(result)
print(result_plus_17)
