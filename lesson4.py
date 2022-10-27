# list_names =["Nazgul", "Zamira", "Aliza"]
# i = len(lis_names) -1
# while i <len(list_names):
#     print(list_names[i])
#     if i ==0:
#         break
#     i -=1

# tuple #list #set #dict eto kolleksii
#
# tuples =("Nazgul", [1,2,3], 6)  ##не изменяемая коллекция, но лист внутри может изменять
# # print(type(tuples))
# tuples[1][0] = 6
# print(tuples)

# tuples = ([1,2,3], 4,5)
# tuples =list(tuples)
# tuples.append("Nazgyl")
# tuples =tuple(tuples)
# print(tuples)
# for i in tuples:
#     print(i)

# a = 8
# b = 10
# a, b = b, a
# print(a)
# print(b)

#tuples = ([1,2,3], 4,5)
# lists, number, number2 =tuples
#lists , *number = tuples  #в этом случае мы присвоили 0 индекс к листу а все остальное через звездочку в намбер
#print(lists)
#print(number)

# names = ("Nurlan", "Smanaly", "Aman")
# print(names[::2])
# print(names[-2:])
# print(names.count("Nurlan"))
# print(names.index("Nurlan"))

# tuples = ((), (), ('',), ('a', 'b'),"asv",5, ('a', 'b', 'c'), ('d'))
# tuples =list(tuples)
# tupless =list()
# for i in tuples:
#     if type(i) == tuple and len(i) == 0:
#         continue
#     tupless.append(i)
# tuples =tuple(tupless)
# print(tuples)

# print(type(("a")))
# print(type(("a",)))

# tuples = ((), (), ('',), ('a','b'),"asv",5,6, ('a', 'b', 'c'), ('d','l','h','j'))
# chet=list()
# for i in tuples:
#     if type(i) == tuple and len(i) %2 == 0 and len(i)!=0:
#         chet.append(i)
# tuples =tuple(chet)
# print(tuples)

# tuples = ((), (), ('',), ('a','b'),"asv",5,6, ('a', 'b', 'c'), ('d','l','h','j'))
# tuples =list(tuples)
# chet=list()
# for i in tuples:
#     if type(i) == tuple and len(i) %2 != 0:
#         continue
#     chet.append(i)
# tuples =tuple(chet)
# print(tuples)
#
# num = float(2)
# print(num)