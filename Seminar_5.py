# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr".
#  То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.

# inp = str(input("Введите строку: "))
# ans = bool((lambda x: 'plr' in inp, inp))
# print(ans)

# решение преподователя 

# contains = lambda s, sample='ra': sample in s
# s = input()
# print(contains(s))

#####################################################################################
# NOD

# def NOD (a,b):
#     if a % b == 0 :
#         return b
#     else :
#         return NOD(b, a % b)

# a = int(input())
# b = int(input())
# print(NOD(a, b))

# решение преподователя 

# a=20
# b=58

# if a < b :
#     a, b = b, a

# while b!=0:
#     a, b = b, a % b

# print(a)
# # еще одно решение 
# while a != b:
#     if a > b:
#         a -= b
# else:
#     b -= a

# print(a)

##################################################################


# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# A = [1, 2, 3, 4, 6, 7]
# for i in range(1, len(A)):
#     if A[i]-1 != A[i-1]:
#         print(A[i-1]+1)

##############################################################################


# Напишите программу, удаляющую из текста все слова, содержащие "абв".


# пример кода 

# def find_num(lst):
#     for i in range(1, len(lst)):
#         if lst[i] - lst[i - 1] > 1:
#             return i, lst[i] - 1
#             return -1, -1


# with open("data.txt", "r") as fin:
#     lst = [int(i) for i in fin.readline().split()]
#     print(lst)
#     pos, num = find_num(lst)
#     print(pos,num)
#     if (pos != -1):
#         lst.insert(pos, num)
#     print(lst)



with open("data.txt", "r") as fin:
    for line in fin:
        words = line.split()
for word in words:
        if "абв" in word:
            words.remove(word)
sentence = " ".join(words)
print(sentence)