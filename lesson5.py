# a = [[1,3],
#      [2,9]]
# for i in a:
#     for j in i:
#         print(j)


# for i in range(1,11):
#     for j in range(1,10):
#         result =i * j
#         print(f'{j} * {i} = {result}', end="\t")
#     print()

# str_n = "naz\tgul"
# print(str_n)
#
# str_n = "naz\rgul"
# print(str_n)

# array_list = [[3,2,1],
#               [2,3,3],
#               [0,2,5]]
#
# for i in range(len(array_list)):
#     for j in range(len(array_list[i])):
#         if i  == j:
#             array_list[i][j] =0
#         print(array_list[i][j], end = " ")
#     print()

# array_list = [[3,2,1],
#               [2,3,3],
#               [0,2,5]]
#
# for i in range(len(array_list)):
#     for j in range(len(array_list[i])):
#         if i  == j:
#             array_list[i][j] =0
#         elif i > j:
#             array_list[i][j] = 1
#         elif i < j:
#             array_list[i][j] = 2
#         print(array_list[i][j], end = " ")
#     print()

from random import choice
cities= ["Moscow", "Bishkek", "New-York"]
city = random.choice(cities)
a = input("Vvedite bukvu: ")
