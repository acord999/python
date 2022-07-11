class Matrix:
    def __init__(self, lst_of_lists: list) -> None:
        self.lst = lst_of_lists

    def __str__(self) -> str:
        result = str()
        for el in self.lst:
            result += '\t'.join(map(str, el)) + '\n'
        return result

    def __add__(self, other):
        result = list()
        for st_1, st_2 in zip(self.lst, other.lst):
            result.append([el_1 + el_2 for el_1, el_2 in zip(st_1, st_2)])
        return Matrix(result)


matrix_obj = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_obj_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_obj)
print(matrix_obj + matrix_obj_2)
