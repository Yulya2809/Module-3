data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    summa = 0
    for arg in args:
        if isinstance(arg, (list, tuple, set)):
            summa += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            summa += calculate_structure_sum(*arg.items())
        elif isinstance(arg, str):
            summa +=len(arg)
        elif isinstance(arg, (int, float)):
            summa += arg

    return summa


result = calculate_structure_sum(data_structure)
print(result)