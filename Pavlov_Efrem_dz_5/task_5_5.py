src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
_tmp = sorted(src)
result = [num for num in src if num not in
          [_tmp[i] for i in range(len(_tmp)) if _tmp[i - 1] == _tmp[i] or _tmp[i + 1] == _tmp[i]]]
print(result)
