def print_params(a = 1, b = "строка", c = True):
    print(a, b, c)

print_params(30)
print_params(1, 'box')
print_params(5, 'home', False)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

print()

values_list = [1, 'red', 2.5]
values_dict = {'a': 1, 'b': True, 'c': 'class'}

print_params(*values_list)
print_params(**values_dict)

print()

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)