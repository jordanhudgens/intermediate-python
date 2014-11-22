__author__ = 'admin'

my_array = [1, 2, 3, 4, 5, 6, 7]
zip_dictionary = {'Jordan': '79424', 'Tiffany': '90210', 'Chase': '79763'}

# for i in zip_dictionary.values():
#     print(i)

it = iter(zip_dictionary.values())
print(next(it))
print(next(it))
print(next(it))
print(next(it))