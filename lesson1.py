# uslovniye operatory

# if ,  else, elif

# age = int(input("Vvedite age: "))
# if age >18:
#      print ("Welcome")
#
# elif age== 18:
#     print("Vam mojno zahodit")
#
# else:
#     print("Vy ne prohodite: Vam net 18")

# num1 = int(input("Vvedite num1: "))
# num2 = int(input("Vvedite num2: "))
# operator = input("Vvedite oper: ")
# if operator == "+":
#     print(num1+num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# else operator == "/"
#     print(num1 / num2)

# gradus = int(input("Vvedite temperaturu: "))
# type_of_temp = input("F or C: ")
# # elif edinisa == "c"
# #      print((0*9/5)+ temp)
# # elif edinisa == "f"
# #     print ((temp - 32)5/9)
# if type_of_temp.lower() == "f":
#     temp = (gradus -32) * (5 /9)
#     print(f"gradus {gradus} ravna farangeytu {temp}")
# elif type_of_temp.lower() == "c":
#     temp = gradus * (9/5) +32
#     print(f"gradus {gradus} ravna celcii {temp}")

#
# year = int(input("Vvedite god: "))
# if year % 4 == 0 and year % 100 != 0:
#     print(f"God {year} - Visokosniy "
#           f"and year % 100 == 0:
#     print("Yes")
# else:
#     print("No")

#Tema: List

# lists = [1, 2, 3, "Hello", 4, 8, 6]
# list1 = list()
# # print(type(lists))
# print(lists[3])

# list1 = list()
# list1.append("Hello")
# list1.append('Hi')
# list1.insert(1 , "World!")
# # print(list1)
# # print(len(list1))
# print(list1)

# fruits = ["banana","banana", "apple", "orange"]
# vegetables = ["potato", "cabage", "tomato"]
# fruits.extend(vegetables)
# print(fruits)
# # print(fruits.count("banana"))
# # print(fruits.index("banana", 2))

# phone_numbers = ["996555090807", "996700765849"]
# black_list = phone_numbers.pop(1)
# print(phone_numbers)
# print(black_list)

# Mega = []
# O = []
# Beeline= []
# number = input ("number: ")
# if number.startswith ("55"):
#     Mega.append(number)
# elif number.startswith ("70"):
#     o.append(number)
# elif number.startswith ("77"):
#     Beeline.append(number)
#
# print("Mega", Mega)
# print("O", O)
# print("Beeline", Beeline)

# l = [1,2,3,4]
# l.extend ('56789')
# print(l)
#
# l = [1,2,3, 'c', [1,8,99]]
# l.append('jnfjs5')
# print(l)

def multiply(a,b, answer):
    return(a*b)
