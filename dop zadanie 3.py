data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
res = []
def calculate_structure_sum(*args):
    result = 0
    for a in args:
        if isinstance(a, list) or isinstance(a, tuple) or isinstance(a, set):
            result += calculate_structure_sum(*a)
        if isinstance(a, dict):
            result += calculate_structure_sum(*a.items())
        if isinstance(a, str):
            result += len(a)
            res.append(f'len("{a}")')
        if isinstance(a, int):
            result += a
            res.append(a)
    return result
print(calculate_structure_sum(*data_structure))
