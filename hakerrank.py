# def diagonalDifference(arr):
#     dlinamassiva = len(arr[0])
#     print([arr[x][dlinamassiva - 1 - x] for x in range(dlinamassiva)])
#     return 0
#
# def sorting(num):
#     if num > 0:
#         return 1
#     elif num == 0:
#         return 0
#     else:
#         return -1
# def plusminus(arr1):
#     n = len(arr1)
#     # arr2 =  [sorting(arr1[i])  for i in range(n)]
#     print([1 if x >0 else 0 if x==0 else -1 for x in arr1].count(1))
#     print(len([x for x in arr1 if x>0]))
#     print(len([x for x in arr1 if x == 0]))
#     print(len([x for x in arr1 if x < 0]))
#     # print(arr2.count(1)/n, '\n', arr2.count(0)/n, '\n', arr2.count(-1)/n)
#
# arr = [[6,6,7,-10,0,-3,8,9,-1], [9,7,-10,6,4,1,6,1,1],
# [-1,-2, 4, -6, 1, -4, -6, 3, 9], [-8, 7, 6, -1, -6, -6, 6, -7, 2],
# [-10, -4, 9, 1, -7, 8, -5, 3, -5],[-8, -3, -4, 2, -3, 7, -5, 1, -5],
# [-2, -7, -4, 8,3, -1, 8, 2, 3],[-3, 4, 6, -7, -7, -8, -3, 9, -6],[-2, 0, 5, 4, 4, 4, -3, 3, 0]]
# diagonalDifference(arr)
#
# print([arr[t][t] for t in range(9)])
# print(plusminus(arr[0]))

# for i in range(3,0, -1):
#     blancs = ' '*(i-1)
#     commas = '#'*(3-i+1)
#     stroka = blancs + commas
#     print(stroka)

# candles = [1,5,5,2,1]
# print(candles.count(max(candles)))

# resultarray = []
#
# def convertarray(inp_array):
#     converted_array = [[1 if i[idx] != 'x' else 0  for i in inp_array] for idx in range(len(inp_array[0]))]
#     return converted_array
#
# def count_check(inp_array):
#     if inp_array[0].count('x') == 0:
#         if inp_array[len(inp_array) - 1].count('x') == 0:
#             if [ind[0] for ind in inp_array].count('x') == 0:
#                 if [ind1[-1] for ind1 in inp_array].count('x') == 0:
#                     return True
#
#
# def proverkagranic(inp_array):
#     if inp_array[0][0] == '.' and inp_array[0][len(inp_array[0])-1]
#     =='.' and inp_array[len(inp_array)-1][0] == '.' and inp_array[len(inp_array)-1][len(inp_array[0])-1] == '.':
#         #resultarray.append(str(inp_array).count('1'))
#         if count_check(inp_array):
#             resultarray.append((len(inp_array)-1)*2 + (len(inp_array[0])-1)*2)
#
# def array_run(inp_array):
#     for i in range(len(inp_array), 1, -1):
#         proverkagranic(inp_array[:i])
# arr4 = [['.','.','.','.','.'], ['.','x','.','x','.'], ['.','.','.','.','.'],
# ['.','.','.','.','.'],['.','.','x','.','.']]
# array_for_convert = [['.','.','.','.'],['.','.','x','.'],['x','.','.','.'],['.','x','.','x']]
# #print(convertarray(array_for_convert))
# def kMarsh (arr3):
#     for j in range(len(arr3[0]),1, -1):
#         newarr = []
#         for k in range(0, len(arr3)):
#             newarr.append(arr3[k][0:j])
#
#         array_run(newarr)
#     if not resultarray:
#         print('impossible')
#     else:
#         print(max(resultarray))
# #print([arr3[:5][:j] for j in range(n,0,-1)])
#
# if __name__ == '__main__':
#     #mn = input().split()
#     f = open('C:\\python\\test.txt')
#     grid = [line.strip() for line in f]
#     f.close()
#     kMarsh(grid)
#     #print(convertarray(array_for_convert))
#
#     # m = int(mn[0])
#     #
#     # n = int(mn[1])
#     # grid = []
#
#     # for _ in range(m):
#     #     grid_item = input()
#     #     grid.append(grid_item)
#     #

# #a = int(input())
# a = 'AABCAAADA'
# n = 3
# segment = len(a)//3
# #
# stroka = [a[i:i+segment] for i in range(0, len(a), segment)]
# #keys = {{i[j]:i for i in stroka} for j in range(0, segment)}
#
# for i in stroka:
#     mnoj = set()
#     resstr = ''
#     for j in range(0, len(i)):
#         if i[j] not in mnoj:
#             mnoj.add(i[j])
#             resstr += i[j]
#     print(resstr)
#
# #print(stroka)
#
#
# a,b,c,d = (int(input()) for _ in range(4))
# print (pow(a,b)+pow(c,d))

# for i in range(1,int(input())):
#     print(int(str(i)*i))
# num1, st1, num2, st2 = (set(input().split()) for i in range(4))
# print(len(st1 - st2))
# a = [[[1,2,4],[],[6,7,8,9]]]
# a = [[[1,2,4],[],[6,7,8,9]]]
# # for i in a:
# #print(type(a[0]))
# if 'list' in str(type(a[0][0])):
#      print(len(a[0]))
# x = 1
# y = 1
# z = 2
# n = 3
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     first_max = max(arr)
#     while first_max in arr:
#         arr.remove(first_max)
#     print(max(arr))


python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# python_students = []
# for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         python_students.append([name, score])
# st_dict = {}
# for i in python_students:
#     ex_val = st_dict.get(i[1])
#     if ex_val:
#         ex_val.append(i[0])
#         st_dict[i[1]] = ex_val
#     else:
#         st_dict[i[1]] = [i[0]]
# print('\n'.join(sorted(st_dict[min([x for x in st_dict.keys() if x!=min(st_dict.keys())])])))
# print('\n'.join(sorted(min([b for a,b in python_students if b!=min([y[1] for y in python_students])]))))
# #print([a for a,b in python_students if b == min([y[1] for y in python_students])])
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     print('{:.2f}'.format(sum(student_marks[query_name])/len(student_marks[query_name])))
# if __name__ == '__main__':
#     N = int(input())
#     commands = []
#     my_list = []
#     for _ in range(N):
#         command = input().split()
#         commands.append(command)
#     for command in commands:
#         if command[0] == 'insert':
#             my_list.insert(int(command[1]), int(command[2]))
#         elif command[0] == 'print':
#             print(my_list)
#         elif command[0] == 'remove':
#             my_list.remove(int(command[1]))
#         elif command[0] == 'append':
#             my_list.append(int(command[1]))
#         elif command[0] == 'sort':
#             my_list.sort()
#         elif command[0] == 'pop':
#             my_list.pop()
#         elif command[0] == 'reverse':
#             my_list.reverse()

# n = int(input())# ШИКАРНЫЙ ПРИМЕР! Делает то же самое, что предыдущий код, только через eval.
# l = []
# for _ in range(n):
#     s = input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print(l)
# Идея такая, getattr позволяет получить атрибут, или вызвать метод
# (когда заранее неизвестны ни объект, ни имя метода, ни имя атрибута)
# со списком аргументов. Т.е. получаем команду и список аргуметнов
# * перед аргументами означает, что получаем любое кол-во, сплитом
# превращаем это все в список. далее getattr(объекта, метод) и
# * распаковка (получаем последовательно аргументы один за одним) аргументов
# L = []
# for _ in range(int(input())):
#     command, *args = input().split()
#     try:
#         getattr(L, command)(*(int(x) for x in args))
#     except AttributeError:
# number_count = int(input())
# my_tuple = tuple(list(map(int,input().split()))[:number_count])
# print(hash(my_tuple))
# def swap_case(my_string: str):
#     return ''.join([_.lower() if _.isupper() else _.upper() for _ in my_string])#my_string.swapcase()
# print(swap_case('HackerRank.com presents "Pythonist 2".'))
# print('-'.join((input().rstrip()).split()))
# print('Hello {firstname} {lastname}! You just delved into python.'.format(firstname = input(), lastname = input()))
# def print_full_name(a, b):
#     print('Hello {firstname} {lastname}! You just delved into python.'.format(firstname = a, lastname = b))
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)
# def mutate_string(string, position, character):
#     new_list = list(string)
#     new_list[position] = character
#     return ''.join(new_list)
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


# def count_substring(string, sub_string):
#     c = 0
#     for i in range(len(string)-len(sub_string)+1):
#         sub_sub_string = string[i:i+len(sub_string)]
#         if sub_sub_string == sub_string:
#             c += 1
#     return c
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#     count = count_substring(string, sub_string)
#     print(count)
# Интересное решение с startwith. Если начинается с подстроки, то точно включает ее
# После этого передвигаемся на шаг вперед
# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:].startswith(sub_string):
#             count += 1
#     return count

# Еще одно решение, с циклом while. Тут вообще клево. Пока подстрока содержится в строке, цикл
# Находим позицию подстроки в строке, после этого формируем новую строку от следующей позиции, до конца
# ШИКАРНО!
# Если мы хотим узнать, сколько вхождений подстроки в строку будет после выкусывания позиции
# подстроки, тогда надо добавить к формированию новой строки кусочек S[:i] +
# S, sub = raw_input(), raw_input()
# count = 0
#
# while sub in S:
#     i = S.find(sub)
#     S = S[i + 1:]
#     count += 1
#
# print count
# if __name__ == '__main__':
#     s = input()
#     isAlnum = False
#     isAlpha = False
#     isDigit = False
#     isLower = False
#     isUpper = False
#     for _ in s:
#         if _.isalnum() and isAlnum != True:
#             isAlnum = True
#         if _.isalpha() and isAlpha != True:
#             isAlpha = True
#         if _.isdigit() and isDigit != True:
#             isDigit = True
#         if _.islower() and isLower != True:
#             isLower = True
#         if _.isupper() and isUpper != True:
#             isUpper = True
#
#     print(isAlnum, isAlpha, isDigit, isLower, isUpper, sep='\n')

# То же самое, но с any и eval. КРАСИВО!
# s = input()
# for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
#     print(any(eval("c." + test + "()") for c in s))

# То же самое, без eval, с типами и методами. ВООБЩЕ КРУТОТЕНЬ!
# s = input()
# t = type(s)
# for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
#   print(any(method(c) for c in s))

# my_string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# max_len = 4
# for i in range(0,len(my_string), max_len):
#     if (len(my_string) - i)//max_len >= 1:
#         print_string = my_string[i:i+max_len]
#     else:
#         print_string = my_string[i:]
#
#     print(print_string)

# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

# digit = 17
#
# print('\n'.join(["{0:d} {0:o} {0:x} {0:b}".format(i) for i in range(1, digit + 1)]))
# import string
# alpha = string.ascii_lowercase
#
#
# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))
# def solve(s):
#     # for i in s:
#     #     if i > 0:
#     #         if i
#     my_list = list(s)
#     for i in range(len(my_list)):
#         if i > 0:
#             if my_list[i-1] == ' ':
#                 my_list[i] = my_list[i].capitalize()
#         else:
#             my_list[i] = my_list[i].capitalize()
#     return ''.join(my_list)
#     s = s.split(' ')
#     return ' '.join([i.capitalize() for i in s])
# s = input()
# result = solve(s)
# print(s)
# s = [i.capitalize() for i in s]
# print(*s)
# print(*[i.capitalize() for i in s])

# Еще один способ. Тут мы используем функцию map
# string = input()
# print(' '.join(map(str.capitalize, string.split(' '))))

# def split_words(s):
#     for i in range(len(s)):
#         for j in range(i+1,len(s)+1):
#             new_string = s[i:j]
#             if new_string[0] not in vowels:
#                 if new_string not in consonants:
#                     consonants.add(new_string)
#             else:
#                 if new_string not in vowels_set:
#                     vowels_set.add(new_string)
#
# def count_enters(string, sets):
#     # c = 0
#     # for sub_string in sets:
#     #     for i in range(len(string)-len(sub_string)+1):
#     #         sub_sub_string = string[i:i+len(sub_string)]
#     #         if sub_sub_string == sub_string:
#     #             c += 1
#     # return c
#     count = 0
#     for sub_string in sets:
#         for i in range(len(string)):
#             if string[i:].startswith(sub_string):
#                 count += 1
#     return count

# ТУТ Я НЕ РЕШИЛ, ТОЧНЕЕ РЕШИЛБ НО РЕШЕНИЕ МЕДЛЕННОЕБ ЭТО РЕШЕНИЕ С ХАКЕРРАНКА
# def minion_game(string):
#     vowel =['A','E','I','O','U']
#     S=0
#     K=0
#     for i in range(len(string)):
#         if string[i] in vowel:
#             K+= len(string)-i
#         else:
#             S+=len(string)-i
#     if S>K:
#         print("Stuart"+" "+ "%d" % S)
#     elif K>S:
#         print("Kevin"+" "+'%d' % K)
#     else:
#         print("Draw")
#
# # word = 'BANANA'
# # consonants = set()
# # vowels_set = set()
# # vowels = "aeiou".upper()
# my_string = 'NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN'#input().upper()
# minion_game(my_string)
# split_words(my_string)

# Stuart = count_enters(my_string, consonants)
# Kevin = count_enters(my_string, vowels_set)
# if Stuart > Kevin:
#     print('Stuart ' + str(Stuart))
# elif Kevin > Stuart:
#     print('Kevin ' + str(Kevin))
# else:
#     print('Draw')

# list_of_numbers = [113048, 1044516, 287083, 2030351, 1821357, 1349438,
#                    686781, 312932, 5033275, 1225240, 1731096, 112943]
# from itertools import combinations

# input = [3, 7, 20, 44]
#
# output = [list(map(list, combinations(input, i))) for i in range(len(input) + 1)]
# print(output)

# list_of_numbers = [1, 2, 3, 4, 5]
#
# sums_of_list = []
#
# for i in range(len(list_of_numbers)):
#     for j in range(i+i, len(list_of_numbers)+1):
#         sums_of_list.append(list_of_numbers[i:j])
#
#     # for k in range():
#
# print(sums_of_list)
# def combs(a):
#     if len(a) == 0:
#         return [[]]
#     cs = []
#     for c in combs(a[1:]):
#         cs += [c, c+[a[0]]]
#     return cs
# my_list = combs(list_of_numbers)
# sums = set()
# for i in my_list:
#     sums.add(sum(i))
#
# print('\n'.join([str(i) for i in sorted(sums)]))
# def average(array):
#     set_a = set(array)
#     return sum(set_a)/len(set_a)
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

# num_int, num_int_in_sets =map(int, input().split())
# my_array = tuple(map(int, input().split()[:num_int]))#tuple(map(int, input().split()[:num_int]))
# set_a = set(map(int, input().split()[:num_int_in_sets]))
# set_b = set(map(int, input().split()[:num_int_in_sets]))
# # print(len(my_array.intersection(set_a)) - len(my_array.intersection(set_b)))
# # print([(i in set_a) - (i in set_b) for i in my_array])
#
# # count = [0 + 1 if x in A else 0-1 if x in B else 0 + 0 for x in arr]
# count = [1 if x in set_a else -1 if x in set_b else 0 + 0 for x in my_array]
# print(count)
# c =0
# for i in range(len(my_array)):
#     if my_array[i] in set_a:
#         c += 1
#     if my_array[i] in set_b:
#         c -= 1
# print(c)

#
#
# set_a = {2,4,5,9}
# set_b = {2,4,11,12}
#
# print(*sorted(set_a^set_b), sep='\n')

# print(len({input() for _ in range(int(input()))}))

# n = int(input())
# my_set = set(map(abs, map(int, input().split()[:n])))
# my_new_set = set()
# for i in my_set:
#     if i <= 9:
#         my_new_set.add(i)
# my_set.clear()
#
# for _ in range(int(input())):
#     command, *args = input().split()
#     try:
#         getattr(my_new_set, command)(*(int(x) for x in args))
#     except KeyError:
#         pass
# print(sum(my_new_set))

# n = int(input())
# english_set = set(map(int, input().split()[:n]))
# m = int(input())
# french_set = set(map(int, input().split()[:m]))
# print(len(english_set | french_set))

# ТО ЖЕ САМОЕ, НО ПРИМЕР ДВОЙНОГО ВВОДА
# _, a = input(), set(input().split())
# _, b = input(), set(input().split())
# print(len(a.union(b)))

# _, my_set = input(), set(map(int, input().split()))
# counter = int(input())
# for i in range(counter):
#     command, _ = input().split()
#
#     another_set = map(int, set(input().split()))
#     getattr(my_set, command)(another_set)
# print(sum(my_set))

# n = int(input())
# english_set = set(map(int, input().split()[:n]))
# m = int(input())
# french_set = set(map(int, input().split()[:m]))
# print(len(english_set ^ french_set))

# def strict_super_set(other_set):
# # return other_set.issubset(my_set) and len(my_set) > len(other_set)
#     print(id(other_set))
#     return my_set > other_set
#
# my_set = set(input().split())
# is_ok = True
# for _ in range(int(input())):
#     other_set = set(input().split())
#     print(id(other_set))
#     if not strict_super_set(other_set):
#         is_ok = False
#         print('False')
#         break
# if is_ok:
#     print('True')

# С ПОМОЩЬЮ ГЕНЕРАТОРА И ФУНКЦИИ ALL. ГЕНЕРАТОР ТО ОКАЗЫВАЕТСЯ МОЖНО ПОДАТЬ НА ВХОД ФУНКЦИИ...
# НАПРИМЕР SUM. И ВСЕ ПРЕКРАСНО СЛОЖИТСЯ.
# a = set(input().split())
# print(all((a > set(input().split()) for _ in range(int(input())))))
# print(sum(i for i in range(1, 4)))

# from collections import Counter
# # list_of_shoes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
# _, list_of_shoes = input(), map(int, input().split())
# number_of_sizes = Counter(list_of_shoes)
# print(number_of_sizes)
# desire = []
# for _ in range(int(input())):
#     size_s, price = map(int, input().split())
#     if number_of_sizes[size_s] > 0:
#         desire.append(price)
#         number_of_sizes[size_s] -= 1
# print(sum(desire))
#
#
# ЗАМЕЧАНИЯ ПРО КОЛЛЕКЦИИ. НЕЛЬЗЯ УДАЛЯТЬ ЭЛЕМЕНТЫ КОЛЛЕКЦИИБ ПОКА МЫ
# БЕЖИМ ПО НЕЙ! МОЖНО БЕЖАТЬ ПО КОПИИ КОЛЛЕКЦИИБ И ТОГДА БЕЗ ПРОБЛЕМ
# МОЖНО УДАЛЯТЬ ЭЛЕМЕНТЫ ИСХОДНОЙ КОЛЛЕКЦИИ. LIST() СОЗДАЕТ КОПИЮ СПИСКА.
# for elm in list(my_list):
# Теперь можете удалять и добавлять элементы в исходный список my_list,
# так как итерация идет по его копии.


# ПРИКОЛ! ЕСЛИ ИСПОЛЬЗОВАТЬ sum([int(i) if i.isdigit() else 0 for i in text.split()]), ТО
# ОБЯЗАТЕЛЬНО НУЖЕН ELSE! А ЕСЛИ IF В КОНЦЕ, ТО НЕ ОБЯЗАТЕЛЬНО!!!!
# def sum_numbers(text: str) -> int:
#     # your code here
#      return sum([int(i) for i in text.split() if i.isdigit()])

#array = [0, 1, 2, 3, 4, 5]
# array = []
# print(sum([array[i] for i in range(0, len(array), 2)])*(array[-1] if array else 0))
# print("rightright".replace('right','left'))
# words = "bla bla bla 1 bla"
# a = ''.join(['1' if i.isalpha() else '0' for i in words.split()])
# return if '111' in a
# def checkio(words: str) -> bool:
#     c = 0
#     for i in words.split():
#         if i.isalpha():
#             c += 1
#         else:
#             c = 0
#         if c == 3:
#
#             return True
#     return False
# print(checkio(words))
# string = '10'
#
# print(len(string) - len(''.join([' ' if i == '0' else i for i in string]).rstrip()))
# print(b)
# print(rev_string.index((str([i for i in range(1, 9)]))))
# print(string[::-1][:string[::-1].index(not '0')].count('0'))
# my_list = [7, 7, 7, 7, 7, 7, 7, 7, 7]
# def remove_all_before(items: list, border: int):
#
#
#     return items[items.index(border):] if border in items else items
#
# print(remove_all_before(my_list, 7))
#
# my_list = [1, 2, 3, 4, 5]
#
# print(my_list[1:] + my_list[0:1])
#
# number = 0
# print(sorted(list(str(number)))[-1])
# def split_pairs(a):
#     b = list([ch1 for ch1 in zip(a[::2],a[1::2]+'_')])
#     # print([i if len(i) == 2 else i+'_' for i in b])
#     print(b)
# split_pairs('abcde')

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# # numbers, letters = zip(*pairs)
# a,b = zip(*pairs)
# print(a)

# number = '0000'
#
# print(len(number) - len(number.lstrip('0')))

# def nearest_value(values: set, one: int) -> int:
#     values = list(values)
#
#     min_znach = abs(values[0] - one)
#     min_el = values[0]
#     for i in range(1, len(values)):
#         distance = abs(values[i] - one)
#         if distance < min_znach:
#             min_znach = distance
#             min_el = values[i]
#         elif distance == min_znach:
#             min_el = min_el if min_el < values[i] else values[i]
#
#
#     return one if one in values else min_el#sorted_x[0][0]
#
# #print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
# print(nearest_value([0,-2],-1))

#ВОТ ЭТО КРУУУУТО! СУПЕР РЕШЕНИЕ ПРЕДЫДЦЩЕЙ ЗАДАЧИ. ЧУВСТВОВАЛ ЧТО ЧТО-ТО ПОДОБНОЕ ЕСТЬ!
# def nearest_value(values: set, one: int) -> int:
#     def distance(value): return abs(value - one), value #> one # - ЭТО КОРТЭЖ!
#     return min(values, key=distance)
#
# #А ТАК ЕЩЕ ЛУЧШЕ!!!!!!!!!!!!
# def nearest_value(values: set, one: int) -> int:
#     return min(values, key=lambda n: (abs(one - n), n))



# def between_markers(text: str, begin: str, end: str) -> str:
#
#     return text.split(begin)[1].split(end)[0]
#
# print(between_markers('What is >apple<', '>', '<'))


# def correct_sentence(text: str) -> str:
#
#     return text[0].upper() + text[1:] + ('.' if text[-1] != '.' else '')
# import itertools
# def check_I(subj):
#     return subj[-1:-4:-1] == '!!!'
#
# def check_upper(subj):
#     return subj.upper() == subj
#
# def del_nonalphas(word):
#
#     return [letter for letter in word if letter.isalpha()]
#
# def del_dubls(word):
#     return [a[0] for a in itertools.groupby(word)]
#
#
# def check_words(subj):
#     stress_words = ['help', 'asap', 'urgent']
#     list_words = subj.lower().split()
#     a = []
#     for i in list_words:
#         i = ''.join(del_nonalphas(i))
#         i = ''.join(del_dubls(i))
#         a.append(i in stress_words)
#     return any(a)
#
# def is_stressful(subj):
#     return check_I(subj) or check_upper(subj) or check_words(subj)
#
#
#
# print(is_stressful("HI asap hhhheeeeeelllllpppp!!!"))
# print(is_stressful("I neeed H-E-L-P"))
# print(is_stressful("I neeed HL-P!!"))
# print(is_stressful("UUUURGGGEEEEENT here"))
#




# def to_camel_case(text):
#     if text:
#         text = text.replace('_', ' ')
#         text = text.replace('-', ' ')
#         list_of_words = text.split()
#         return list_of_words[0] + ''.join([list_of_words[i].capitalize() for i in range(1, len(list_of_words))])
#     return ''

# def narcissistic(value):
#     my_str = str(value)
#     return sum([int(i)**len(my_str) for i in my_str]) == value
#
# print(narcissistic(371))

# def is_stressful(subj):
#     for word in ('help', 'asap', 'urgent'):
#         s = ''.join(x for x in subj.lower() if x in word+' ')
#         for i in s*len(s): s = s.replace(i+i, i)
#         if s.count(word): return True
#     return subj == subj.upper() or subj.endswith('!!!')
#
# print(is_stressful("H-eeeeeeeeeL-P!!"))

# def first_word(text: str) -> str:
#     # trans_table = str.maketrans('123', '.-_')
#     # text = text.translate(trans_table)
#     # text.title().translate(".","-")
#     translation_table = str.maketrans(".-_,", "    ")
#     text = text.translate(translation_table)
#     my_list = text.split()
#     return my_list[0]
#
# print(first_word("Hello.World"))
# print(first_word("... and so on ..."))

# import datetime
# def days_diff(a, b):
#     y, m, d = zip(a,b)
#     return abs((datetime.date(y[0], m[0], d[0]) - datetime.date(y[1], m[1], d[1])).days)
#
# print(days_diff((1982, 4, 19), (1982, 4, 22)))
# my_d = [2020, 9, 28]
# print((datetime.date(2020, 9, 29) - datetime.date(my_d)).days)

# # ТО ЖЕ, С РАСПАКОВКОЙ ПАРАМЕТРОВ. ИНТЕРЕСНО!!!
# def days_diff(date1, date2):
#     return abs((datetime(*date1)-datetime(*date2)).days)

# ИНИЦИАЛИЗАЦИЯ КЛЮЧА В СЛОВАРЕ, ЕСЛИ ЕГО НЕТ setdefault()
# fruits.setdefault('pears', 0)

# import datetime
# def how_spammed(str_date):
#     convert_date = list(map(int, str_date.split('-')))
#
#     start_time = datetime.date(convert_date[0], convert_date[1], convert_date[2])
#     end_time = start_time + datetime.timedelta(days=1)
#
#
#     start_time_timestamp = (start_time - datetime.date(1970, 1, 1)) / datetime.timedelta(seconds=1)
#     end_time_timestamp = (end_time - datetime.date(1970, 1, 1)) / datetime.timedelta(seconds=1)
#

# SEND GRID API KEY = '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'

# name = 'Den'
# BODY = 'Hi {name}'
# plain_text_content = BODY.format(name=name)
# print(plain_text_content)

# СОРТИРОВКА СЛОВАРЯ ВНУТРИ СПИСКА ПО ЗНАЧЕНИЮ ПОЛЯ, А ПОТОМ ПО ЗНАЧЕНИЮ ДРУГОГО
# ПОЛЯ. ДЛЯ ЭТОГО НАДО СДЕЛАТЬ TUPLE, В КОТОРОМ НА ПЕРВОМ МЕСТЕ БУДЕТ ИДТИ ПЕРВОНАЧАЛЬНОЕ
# ПОЛЕ СОРТИРОВКИ, А ЗАТЕМ ВТОРОЕ ПОЛЕ. СМ. НИЖЕ

# def bigger_price(limit: int, data: list) -> list:
#
#     return sorted(data, key = lambda i: (i['price'], i['name']))#, reverse=True)
#
# print(bigger_price(2, [
#         {"name": "wine", "price": 138},
#         {"name": "bread", "price": 138},
#         {"name": "meat", "price": 138},
#         {"name": "water", "price": 1}
#     ]))

# def between_markers(text: str, begin: str, end: str) -> str:
#     open_index = text.find(begin) if begin in text else 0
#     offset = len(begin) if text.find(begin) >= 0 else 0
#     close_index = text.find(end) if end in text else len(text)
#     return text[open_index + offset:close_index]
#
# print(between_markers("<head><title>My new site</title></head>",
#                             "<title>", "</title>"))
# print(between_markers('No[/b] hi', '[b]', '[/b]'))
# print(between_markers('No [b]hi', '[b]', '[/b]'))
# print(between_markers('No hi', '[b]', '[/b]'))
# print(between_markers('No <hi>', '>', '<'))
# print(between_markers("Never send a human to do a machine's job.","Never","do"))

# def checkio(data: list) -> list:
#
#     # return [i for i in data if (data.count(i) > 1 or all(list(data.count(i) == 1 for i in data)))] if len(data) > 1 else []
#         return [i for i in data if data.count(i) > 1 ] if len(data) > 1 else []
#
# print(list(checkio([1, 2, 3, 1, 3])))
# print(list(checkio([1, 2, 3, 4, 5])))
# print(list(checkio([5, 5, 5, 5, 5])))
# print(list(checkio([10, 9, 10, 10, 9, 8])))
# print(list(checkio([2])))

# В языке программирования Python есть встроенная функция filter(), которая принимает два
# параметра и возвращает объект-итератор. Первый аргумент этой функции - какая-либо другая
# функция, а второй - последовательность (строки, списки и кортежи), итератор или объект,
# поддерживающий итерацию.
#
# Функция filter() возвращает итератор, состоящий из тех элементов последовательности, для
# которых переданная в качестве первогоучше аргумента функция вернула истину (true) или ее аналог
# (не ноль, не пустую строку, не None).
# ТО ЖЕ САМОЕ, НО С filter()
# def checkio(data: list) -> list:
#     return list(filter(lambda x: data.count(x) != 1, data))

# from collections import Counter
# def popular_words(text: str, words: list) -> dict:
#
#
#     # return {key:value  for key, value in Counter(text.lower().split()).items() if key in words}
#     return {key:Counter(text.lower().split())[key] for key in words}


#
# print(popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']))

# ИНТЕРЕСНО! ТО ЖЕ САМОЕ, НО ТУТ МЫ В lower_count КОНСТРУИРУЕМ ФУНКЦИЮ, КОТОРУЮ ВЫЗЫВАЕМ В ГЕНЕРАТОРЕ СЛОВАРЯ!

# def popular_words(text, words):
#     lower_count = text.lower().split().count
#     return {word: lower_count(word) for word in words}



# def second_index(text: str, symbol: str) -> [int, None]:
#     """
#         returns the second index of a symbol in a given text
#     """
#     position = text.find(symbol, text.find(symbol)+1 ,len(text))
#     # your code here
#     return  position if position > 0 else None
# # string_my = 'When I was Two'.lower()
# # print(string_my.find('w', string_my.find('w')+1 ,len(string_my)))
# print(second_index("hi", " "))

# def frequency_sort(items):
#     order = {key:items.index(key) for key in items}
#     return sorted(items, key = lambda i: (-items.count(i), order[i]))
#
# print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))
# print(list(frequency_sort([17, 99, 42])))
# print(list(frequency_sort([])))
# print(list(frequency_sort([1])))
#


# def find_neighbours(element: str) -> set:
#     neighbours_list = []
#     left_index = (chr(ord(element[0])-1))
#     right_index = (chr(ord(element[0])+1))
#     down_index = str(int(element[1])-1)
#     neighbours_list.append(left_index+down_index)
#     neighbours_list.append(right_index + down_index)
#     return set(neighbours_list)
#
# def safe_pawns(pawns: set) -> int:
#     safe_count = 0
#
#     for element in pawns:
#         neighbours = find_neighbours(element)
#         # print(any([i in pawns for i in neighbours]))
#
#         neighbours &= pawns
#         if  neighbours:
#             safe_count += 1
#     return safe_count
#
# print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
# print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))

# ТО ЖЕ САМОЕ, НО БОЛЕЕ ПРОСТО!!!!
# def safe_pawns(ps):
#     p_indexes = set([(int(p[1])-1, ord(p[0])-97) for p in ps])
#
#     return sum([1 for r, c in p_indexes if (r-1, c-1) in p_indexes or (r-1, c+1) in p_indexes])


# ВОТ ТАК РАБОТАЕТ KEY В СОРТИРОВКЕ!!!!!!!! В НЕГО ПЕРЕДАЕТСЯ ИМЯ ФУНКЦИИ, ИЛИ ЛЯМБДА ФУНКЦИЯ
# СРАЗУ ВЫДАЕТ РЕЗУЛЬТАТ!!!!
# def my_compare(list: list) -> int:
#     return list[1]
#
# a = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
# print(sorted(a, key = my_compare))

# GRADUS_PER_MINUTE = 0.25
# MINUTES_PER_HOUR = 60
# SUN_RISE_AT = 6
#
# def sun_angle(time: str) -> float:
#     time_list = time.split(':')
#     hours = int(time_list[0])
#     if 6<=hours<=18:
#         minutes = int(time_list[1])
#         minutes_after_six = MINUTES_PER_HOUR*(hours - SUN_RISE_AT) + minutes
#         if minutes_after_six <= 720:
#             return minutes_after_six * GRADUS_PER_MINUTE
#         else:
#             return "I don't see the sun!"
#
#     return "I don't see the sun!"


# def split_list(items: list) -> list:
#     slice_index = (len(items) // 2)  if (len(items) % 2) == 0 else (len(items) // 2) + 1
#
#     return [items[:slice_index]] + [items[slice_index:]]

# from typing import List, Any
#
# def all_the_same(elements: List[Any]) -> bool:
#
#     return len(set(elements)) in (0,1)

# def date_time(time: str) -> str:
#     month_dict = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May',
#                   '06':'June', '07':'July', '08':'August', '09':'September', '10':'October',
#                   '11':'November', '12':'December'}
#     time_list = time.split()
#     h_m_list = time_list[1].split(':')
#     date_list = time_list[0].split('.')
#     return_string_date = str(int(date_list[0])) + ' ' + month_dict[date_list[1]] + ' ' +date_list[2] + ' year '
#     hour_or_hours = ' hours ' if str(int(h_m_list[0])) > '1' else ' hour '
#     minute_or_minutes = ' minutes' if str(int(h_m_list[1])) > '1' else ' minute'
#     return_string_h_m = str(int(h_m_list[0])) + hour_or_hours + str(int(h_m_list[1])) + minute_or_minutes
#     return return_string_date + return_string_h_m

# ТАК ЛУЧШЕ!!!!! ФОРМАТНАЯ СТРОКА, КЛЕВО!
# import calendar
# def date_time(time: str) -> str:
#
#     day, month, year = map(int, time.split()[0].split('.'))
#     hour, min = map(int,time.split()[1].split(':'))
#     month = calendar.month_name[month]
#
#     res = (f"{day} {month} {year} year {hour} {'hour' if hour==1 else 'hours'} "
#     + f"{min} {'minute' if min==1 else 'minutes'}")
#     return res

# MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
#          '-..':   'd', '.':     'e', '..-.':  'f',
#          '--.':   'g', '....':  'h', '..':    'i',
#          '.---':  'j', '-.-':   'k', '.-..':  'l',
#          '--':    'm', '-.':    'n', '---':   'o',
#          '.--.':  'p', '--.-':  'q', '.-.':   'r',
#          '...':   's', '-':     't', '..-':   'u',
#          '...-':  'v', '.--':   'w', '-..-':  'x',
#          '-.--':  'y', '--..':  'z', '-----': '0',
#          '.----': '1', '..---': '2', '...--': '3',
#          '....-': '4', '.....': '5', '-....': '6',
#          '--...': '7', '---..': '8', '----.': '9', '':' '
#         }
#
# def morse_decoder(code: str) -> str:
#     phrase = ''.join([MORSE[i] for i in code.replace('   ', '  ').split(' ')])
#     return phrase.capitalize()
#
# print(morse_decoder("... --- -- .   - . -..- -"))

# from typing import Iterable
#
#
# def except_zero(items: list) -> Iterable:
#
#     zero_pos = [i for i in range(len(items)) if items[i] == 0 ]
#     items = sorted(items)[len(zero_pos):]
#     for i in zero_pos:
#         items.insert(i, 0)
#     return items

# def frequency_sorting(numbers):
#
#     return sorted(numbers, key = lambda i: (-numbers.count(i), i))
# def how_deep(structure):
#     return 1 + max(how_deep(itm) for itm in structure) if type(structure) == tuple else 0
# # print(how_deep((1, 2, (3,))))
# # print(how_deep((1, 2, (3, (4,)))))
# print(how_deep((1, ((),), (3,))))

# def how_deep(list_):
#     return 1 + max(how_deep(itm) for itm in list_) if type(list_) == tuple else 0


# def how_deep(l):
#     if isinstance(l, (list, tuple)):
#         t = (0,)
#         for itm in l:
#             t += how_deep(itm),
#         return 1 + max(t)
#     return 0

# БОЛЕЕ ПОНЯТНАЯ РЕКУРСИЯ, ЧЕМ ВЫШЕ
# def how_deep(structure):
#     result = [1]
#     for itm in structure:
#         if isinstance(itm, tuple):
#             result.append(how_deep(itm) + 1)
#     return max(result)

# def reverse_ascending(items):
#     res_array = []
#     count = 0
#     for i in range(1, len(items)):
#         if items[i] <= items[i-1]:
#             res_array += items[count:i][::-1]
#             count = i
#     if len(res_array) < len(items):
#         res_array += items[count:][::-1]
#
#     return res_array
#     # return [item for sublist in res_array for item in sublist[::-1]]

# from typing import Iterable


# def compress(items: list) -> Iterable:
#     res_array = []
#     if items:
#         res_array.append(items[0])
#         for i in range(1, len(items)):
#             if res_array[len(res_array)-1] != items[i]:
#                 res_array.append(items[i])
#
#     return res_array


# def del_dubls(word):
#     return list(dict.fromkeys(word))
#
#
# def checkio(data):
#     res_string = list(data[0])
#
#     for i in range(1,len(data)):
#         is_worked = 1
#         for j in range(len(data[i])):
#             if data[i][j] in res_string:
#                 res_string.insert(res_string.index(data[i][j]), data[i][:j+1] + data[i][j+1:])
#                 res_string = del_dubls(list(''.join(res_string)))
#                 is_worked = 0
#         if is_worked:
#             res_string.append(data[i])
#             res_string = del_dubls(list(''.join(res_string)))
#
#
#     return ''.join(del_dubls(list(''.join(res_string))))

# def checkio(data):
#     alphabet = sorted(set(''.join(data))) # unique alphabet
#     result = ''
#     for n in range(len(alphabet)):
#         # find minimum
#         for c in alphabet:
#             if c in result: continue # already used
#             if all(c not in word or c == word[0] for word in data): break # found
#         result += c
#         # remove c from data
#         for i in range(len(data)): data[i] = data[i].replace(c, '')
#
#     return result

# print(checkio(["acb", "bd", "zwa"]))
# print(checkio(["dfg", "frt", "tyg"]))
# print(checkio(["klm", "kadl", "lsm"]))
# print(checkio(["a", "b", "c"]))
# print(checkio(["aazzss"]))
# print(checkio(["dfg", "frt", "tyg"]))
# print(checkio(["hello","low","lino","itttnosw"]))
# print(checkio(["qwerty","asdfg","zxcvb","yagz"]))
# print(checkio(["hfecba","hgedba","hgfdca"])) #hgfedcba
#
# def xo(s):

#     s = s.lower()
#     return s.count('x') == s.count('o')
#     return not bool(sum(1 if i == 'x' else -1 for i in s.lower() if i in ('xo')  ))

# import math
# def find_next_square(sq):
#     if sq:
#         number = math.sqrt(sq)
#         if (number % int(number)) != 0:
#             return -1
#         else:
#             return int((number+1)**2)
#     else:
#         return 0

# ТАК ЛУЧШЕ!!!!
# def find_next_square(sq):
#     root = sq ** 0.5
#     if root.is_integer():
#         return (root + 1)**2
#     return -1

# import collections
# a = [1,2,3,4,5,1]
# d = collections.deque(a)
# b = collections.Counter(a)
# d.rotate()
# print(d)
# print(b)

# from itertools import *
# my_list = [1, 2, 3, 4]
# print(list(permutations(my_list)))
# print(list(combinations (my_list, 3)))

# import collections
#
# freq = collections.Counter([input() for _ in range(int(input()))])
# print(len(freq))
# print(*freq.values())

# import collections

# print(*[str(i[0]) + ' '+ str(i[1]) for i in collections.Counter(sorted(input())).most_common(3)], sep='\n')
# ВАЖНО! ВОТ ТАК НУЖНО ИСПОЛЬЗОВАТЬ ПЕЧАТЬ В РАСПАКОВКЕ КОРТЕЖА!!!!!
# [print(*c) for c in collections.Counter(sorted(input())).most_common(3)]

# from collections import deque
#
# for _ in range(int(input())):
#     _, queue = input(), deque(map(int, input().split()))
#
#     for cube in reversed(sorted(queue)):
#         if queue[-1] == cube:
#             queue.pop()
#         elif queue[0] == cube:
#             queue.popleft()
#         else:
#             print('No')
#             break
#     else:
#         print('Yes')


# from collections import deque
# my_deque = deque()
# for _ in range(int(input())):
#     command, *args = input().split()
#
#     getattr(my_deque, command)(*args)
# print(*my_deque)

# from itertools import *
#
# n, modu = map(int, input().split())
# my_list = []
# for i in range(n):
#     my_list.extend([list(map(int, set(input().split())))])
# produt_list = list(product(*my_list))
# # a = max(test(sub) for sub in produt_list)
# a = max(sum(i**2 for i in sub)%modu for sub in produt_list)
# print(a)
#
# # ВОТ ТАК ПРОХОДИТ ВСЕ ТЕСТЫ
# from itertools import product
#
# K,M = map(int,input().split())
# N = (list(map(int, input().split()))[1:] for _ in range(K))
# results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
# print(max(results))

# from itertools import *
# list1, list2 = [map(int, input().split()) for _ in range(2)]
# print(*product(list1,list2))

# from itertools import *
# my_string, c = input().split()
# [print(*i, sep='') for i in permutations(sorted(my_string), int(c))]


# from itertools import *
#
# print(*[( len([*j]), int(i)) for i, j in groupby(input())])

# from itertools import *
# n = int(input())
# my_list = input().split()
# k = int(input())
# indexes = set([i+1 for i in range(len(my_list)) if my_list[i] == 'a'])
# my_string = list(range(1,n+1))
# a = list(combinations(my_string,k))
#
#
# # for i in a:
# #     for j in i:
# #       if j in indexes:
# #           b.append(1)
# #           break
#
#
# print(round(sum(1 if set(sub) & indexes else 0 for sub in a )/len(a),3))

# from collections import namedtuple
# n = int(input())
# names = input()
# Student = namedtuple('Student', names)
# names_list = names.split()
# data_list = [input().split() for _ in range(n)]
#
# Students = []
# for i in data_list:
#     Students.append(Student(ID = i[names_list.index('ID')], MARKS = i[names_list.index('MARKS')],
#                             NAME = i[names_list.index('NAME')], CLASS = i[names_list.index('CLASS')]))
#
# # print(f'{sum([int(i.MARKS) for i in Students])/len(Students):.2}f')
# # return f"{numObj:.{digits}f}"
# print(float('{:.3f}'.format(sum([int(i.MARKS) for i in Students])/len(Students))))

# from collections import OrderedDict
# ordinary_dictionary = OrderedDict()
# n = int(input())
# for _ in range(n):
#     my_string = input().split()
#     my_key = ' '.join(my_string[:-1])
#     ordinary_dictionary[my_key] = ordinary_dictionary.setdefault(my_key, 0) + int(my_string[-1])
# [print(i,j) for i, j in ordinary_dictionary.items()]

# МОЖНО С ПОМОЩЬЮ rpartition РАЗДЕЛИТЬ КЛЮЧ И ЗНАЧЕНИЕ! ЭТА ФУНКЦИЯ ДЕЛИТ СТРОКУ НА 3 ЧАСТИ
# item, space, price = input().rpartition(' ')

# import collections
# braces = {'(':')', '[':']', '{':'}'}
#
# def test(my_string):
#     while my_string:
#         if not braces[my_string.popleft()] == my_string.popleft():
#             return False
#     return True
#
# def validBraces(string):
#     my_string = collections.deque(string)
#     my_string1 = my_string.copy()
#     while my_string:
#         if not braces[my_string.popleft()] == my_string.pop():
#             return test(my_string1)
#     return True
#
# print(validBraces("(){}[]"))

# from itertools import *
#
# def is_pali(word):
#     return word == word[::-1]
#
#
#
# def lowest(s):
#     palindromes = []
#     palindromes_list = []
#     s1 = list(s[::])
#     palindromes = sorted(set([''.join(j) for i in range(1, len(s1)+1) for j in list(permutations(''.join(s1),i)) if is_pali(''.join(j))]), key = lambda x: len(x))
#     print(palindromes)


# def is_palindrom(s):
#     return s == s[::-1]
#
# def lowest(s):
#     ''' Возвращает длину наименьшего палиндрома из палиндромов, составленных с использованием всех символов
#         входной строки
#     '''
#     if is_palindrom(s):
#         return len(s)
#     letters = set(s)
#     odd = 0
#     for x in letters:
#         if s.count(x) % 2:
#             odd += 1
#     if odd == 0:
#         return len(s)
#     return 1 + ((len(s) - odd)//(2*odd)) * 2
#
# print(lowest('aebecda'))

# def is_in_middle(s):
#     while len(s)>4:
#         s = s[1:-1]
#     return 'abc' in s
#
# print(is_in_middle("AabcBB"))

# a = [1,0,0,0]
# def fill(a):
#     matrix = []
#     max_el = max(a)
#     for i in range(len(a)):
#         row = []
#         for j in range(max_el):
#             if a[i] > 0:
#                 row.append(1)
#                 a[i] -= 1
#             else:
#                 row.append(0)
#         matrix.append(row)
#     return list(zip(*matrix))[::-1]
#
#
# def move(d, a):
#     summa = sum(a)
#     for i in range(len(a)):
#         if summa > 0:
#             if d == 'R':
#                 a[(len(a)-1)-i] = 1
#             else:
#                 a[i] = 1
#             summa -= 1
#         else:
#             if d == 'R':
#                 a[(len(a)-1) - i] = 0
#             else:
#                 a[i] = 0
#     return a
#
#
# def flip(d, a):
#     matrix = fill(a)
#     print(*matrix, sep = '\n')
#     new_matrix  = []
#     for i in matrix:
#         new_matrix.append(move(d,list(i)))
#
#     return [sum(k) for k in zip(*new_matrix)]




# def zipped(a):
#     return zip(a)
# def flip(d,a):
#     return sorted(a, reverse=d=='L')
# print(flip('L', [3, 2, 1, 2]))
#

# def mirror(data: list) -> list:
#     my_list = []
#     data1 = data.copy()
#     if data:
#         max_el = max(data1)
#         data1.remove(max_el)
#         my_list.extend(sorted(data1))
#         my_list.append(max_el)
#         my_list.extend(sorted(data1, reverse=True))
#     return my_list

# def mirror(data: list) -> list:
#     arr = sorted(data)
#     return arr + arr[-2::-1]

# def binary_array_to_number(arr):
    # arr1 = arr[::-1]
    # b = []
    # for i in range(len(arr)):
    #     if arr1[i]:
    #         b.append(2**i)

    # return sum([2**i for i in range(len(arr)) if arr[::-1][i]])

# ВОТ ТАК! ПРЕОБРАЗОВАНИЕ К ЧИСЛУ С ОСНОВАНИЕМ СИСТЕМЫ СЧИСЛЕНИЯ!!!!
#     return int("".join(map(str, arr)), 2)

# def greet(name):
#     return f"Hello, {name} how are you doing today?"

# def areYouPlayingBanjo(name):
#     if name.lower().startswith('r'):
#         s = f"{name} plays banjo"
#     else:
#         s = f"{name} does not play banjo"
#     return s

# def reverse(n):
#     return int(str(n)[::-1])

import itertools
# import collections
# def repeats(arr):
#     # print(collections.Counter(arr))
#
#     my_array = [i for i, j in collections.Counter(arr).items() if j == 1]
#
#     return sum(set(b) & set(my_array))
#
#
#
#
# print(repeats([9, 10, 19, 13, 19, 13]))
# import math
# time = 1.4
# print(math.floor(time*0.5))
# print(round(time*0.5))
#
# def invert(lst):
#     return [-i for i in lst]
#
# print(invert([1,2,3,4,5]))

# def hero(bullets, dragons):
#     # return (dragons*2)//(bullets) <= 1
#     return dragons - bullets/2
# print(hero(9, 4))
# print(hero(7, 4))
# print(hero(10, 5))
# print(hero(4, 5))

#
# def cap(word: str):
#     return word.capitalize()
# def fix(paragraph):
#     return '. '.join(list(map(cap, paragraph.split('. '))))

# ВОТ ТАК НАДО!!!
# return '. '.join(map(str.capitalize, paragraph.split('. ')))

# РЕГУЛЯРКИ
# . - любой символ, кроме новой строки
# \d - любая цифра
# \D - любой символ, кроме цифры
# \s - любой пробельный символ
# \S - любой непробельный символ
# \w - любая буква (то что может быть частью слова), в том числе цифра и _
# \W - любая не буква, не цифра и не подчеркивание
# [..] - один из символов в скобках, или любой из диапазона a-b, пример [a-z0-9!]
# [^..] - любой, кроме перечисленных
# \b - начало или конец слова (слева пусто или не-буква, справа буква и наоборот). Надо экранировать \!!!!!!!
# \B - Не граница слова: либо и слева, и справа буквы, либо и слева, и справа НЕ буквы
# {n} - ровно n повотрений
# {m,n} - От m до n повторений включительно
# {m,} - Не менее m повторений
# {,n} - Не более n повторений
# ? - 0 или 1 повторение, синоним {0,1}
# * - Ноль или более, синоним {0,}
# + - Одно или более, синоним {1,}
# *? - По умолчанию квантификаторы жадные —
# +?     захватывают максимально возможное число символов. ПРИМЕР \(.*\) (a + b) * (c + d) * (e + f)
# ??     Добавление ? делает их ленивыми,                  ПРИМЕР \(.*?\) (a + b)
# {m,n}? они захватывают
# {, n}? минимально возможное число символов
# {m,}?
# | - это операция ИЛИ для регулярных выражений, т.е. выражение А|В совпадает, если подходит А или В
# Итак, если REGEXP — шаблон, то (?:REGEXP) — эквивалентный ему шаблон. Разница только в том, что теперь к (?:REGEXP)
# можно применять квантификаторы, указывая, сколько именно раз должна повториться группа.
# Например, шаблон для поиска MAC-адреса, можно записать так:
# [0-9a-fA-F]{2}(?:[:-][0-9a-fA-F]{2}){5}
# Также скобки (?:...) позволяют локализовать часть шаблона, внутри которого происходит перечисление.
# Например, шаблон (?:он|тот) (?:шёл|плыл) соответствует каждой из строк
# «он шёл», «он плыл», «тот шёл», «тот плыл», и является синонимом он шёл|он плыл|тот шёл|тот плыл.
# Если в шаблоне есть группирующие скобки, то вместо списка найденных подстрок будет возвращён список кортежей,
# в каждом из которых только соответствие каждой группе. Это не всегда происходит по плану,
# поэтому обычно нужно использовать негруппирующие скобки (?:...)

# print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'))
# -> ['Где', 'скажите', 'мне', 'мои', 'очки', '']

# Если в шаблоне нет группирующих скобок, то re.split работает очень похожим образом на str.split.
# А вот если группирующие скобки в шаблоне есть, то между каждыми разрезанными строками будут в
# се соответствия каждой из подгрупп.
# import re
# print(re.split(r'(\s*)([+*/-])(\s*)', r'12  +  13*15   - 6'))
# # -> ['12', '  ', '+', '  ', '13', '', '*', '', '15', '   ', '-', ' ', '6']
# В некоторых ситуация эта возможность бывает чрезвычайно удобна! Например, достаточно из предыдущего
# примера убрать лишние группы, и польза сразу станет очевидна!
# import re
# print(re.split(r'\s*([+*/-])\s*', r'12  +  13*15   - 6'))
# # -> ['12', '+', '13', '*', '15', '-', '6']

# Использование групп добавляет замене (re.sub, работает не только в питоне, а почти везде) очень удобную
# возможность: в шаблоне для замены можно ссылаться на соответствующую группу при помощи \1, \2, \3, ....
# Например, если нужно даты из неудобного формата ММ/ДД/ГГГГ перевести в удобный ДД.ММ.ГГГГ, то можно использовать такую регулярку:
# import re
# text = "We arrive on 03/25/2018. So you are welcome after 04/01/2018."
# print(re.sub(r'(\d\d)/(\d\d)/(\d{4})', r'\2.\1.\3', text))
# # -> We arrive on 25.03.2018. So you are welcome after 01.04.2018.
# Если групп больше 9, то можно ссылаться на них при помощи конструкции вида \g<12>

# ^ - Начало всего текста или начало строчки текста, если flag=re.MULTILINE
# $ - Конец всего текста или конец строчки текста, если flag=re.MULTILINE
# \A - Строго начало всего текста
# \Z - Строго конец всего текста
# \b - Начало или конец слова (слева пусто или не-буква, справа буква и наоборот)
# \B - Не граница слова: либо и слева, и справа буквы, либо и слева, и справа НЕ буквы

# (?=...) - lookahead assertion, соответствует каждой позиции, сразу после которой начинается
#         соответствие шаблону ПРИМЕР: Isaac (?=Asimov) Isaac (ПОДХОДИТ)Asimov, Isaac other
# (?!...) - negative lookahead assertion, соответствует каждой позиции, сразу после которой
#         НЕ может начинаться шаблон ПРИМЕР: Isaac (?!Asimov) Isaac Asimov, Isaac (ПОДХОДИТ)other
# (?<=...) - positive lookbehind assertion, соответствует каждой позиции, которой может заканчиваться шаблон
#         Длина шаблона должна быть фиксированной, то есть abc и a|b — это ОК, а a* и a{2,3} — нет
#         ПРИМЕР: (?<=abc)def abcdef(ПОДХОДИТ), bcdef
# (?<!...) - negative lookbehind assertion, соответствует каждой позиции, которой НЕ может заканчиваться шаблон
#         ПРИМЕР: (?<!abc)def abcdef, bcdef(ПОДХОДИТ)

# ПОИСК ЛЮБЫХ 2 ПОВТОРЯЮЩИХСЯ СИМВОЛОВ .*(.).*\1.*  ЕСЛИ В СКОБКАХ ПОСТАВИТЬ БУКВУ, БУДЕТ ИСКАТЬ ЕЕ ПОВТОРЕНИЕ

# ИЩЕТ ОДИНАКОВЫЕ ЦИФРЫБ ЧЕРЕЗ ОДНУ (\d)(?=.\1)

# ИЩЕТ 2 И БОЛЕЕ ПОДРЯД ИДУЩИХ СЛОВА, ЧЕРЕЗ ПРОБЕЛ (\b\w+\b)(\s+(\1\b))+

# НЕ МЕНЕЕ 3 РАЗЛИЧНЫХ СИМВОЛОВ (?P<x>.).*?(?!(?P=x))(?P<y>.).*?(?!(?P=x))(?!(?P=y))(.)



import re
# def repl(m):
#
#     return str(int(m[0])**3)
# text = "Было закуплено 12 единиц техники по 410.37 рублей."
# print(re.sub(r'\b[0-9]+\b', repl, text))
# print(''.join([i.upper() for i in re.findall(r'\b[А-Яа-я]', 'микоян авиацию снабдил алкоголем, народ доволен работой авиаконструктора')]))
# def haiku(string: str)-> bool:
#     result = False
#     my_list = ''.join(re.findall(r'/|[аеёиоуыэюяАЕЁИОУЫЭЮЯ]',string)).split('/')
#     if len(my_list) == 3:
#         if (str(len(my_list[0])) + ' ' + str(len(my_list[1])) + ' ' + str(len(my_list[2]))) == '5 7 5':
#             result = True
#     return result
#
# print(haiku('Жизнь скоротечна… / Думает ли об этом / Маленький мальчик.'))
#
# print(re.split(r'[^A-Za-zА-Яа-я.]', 'Он --- серо-буро-малиновая редиска!! >>>:->А не кот. www.kot.ru'))
#

# from datetime import datetime
# import re
#
#
# class Mongo(object):
#
#     @classmethod
#     def is_valid(cls, s):
#
#         return True if re.match(r'(?:[0-9A-Fa-f]{2}){12}', str(s)) != None else False
#
#     @classmethod
#     def get_timestamp(cls, s):
#         if type(s) != type(''):
#             return False
#         result = False
#         if Mongo.is_valid(s):
#             result = datetime.fromtimestamp(int(s[:8], 16))
#
#         return result

# import  re
#
# def convert_to(ss, i):
#     c = re.split(r'(?<=\b)|((?<=[a-z])(?=[A-Z]))', ss)
#     a =  '_'.join([j for j in c if j])
#     part_string[i] = a
#
# s = 'MyVar17 = OtherVar + YetAnother2Var TheAnswerToLifeTheUniverseAndEverything = 42'
# part_string = re.split(r'\s*([=+*/-])\s*', s)
#
#
#
#
# for i in range(len(part_string)):
#     if part_string[i][0].isalpha():
#         convert_to(part_string[i], i)
#
# print(' '.join(part_string))

# import collections
# import re
# s = 'Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод.'
# k = s.split()
#
# b = [(i, j) for i, j in collections.Counter(re.findall(r'[А-Яа-я]+', s)).items() if j > 1]
# for i in b:
#     count = i[1]
#     while count > 1:
#         k.remove(i[0])
#         count -= 1
# print(' '.join(k))
#

# import re
# # for _ in range(int(input())):
# #     # print(list(map(lambda x: bool(re.fullmatch(r'^[+-]\d*\.\d+', x)), input())))
# #     # print(bool(re.fullmatch(r'^[+-]\d*\.\d+', input())))
# #     print(list(map(int, input())))
# s = '100,000,000.000'
# print(*re.split(r'[.,]', s), sep='\n')


# import re
# result = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])+[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', input())
# print(*result, sep='\n') if result else print(-1)

# ТОЛЬКО ПРИ ИСПОЛЬЗОВАНИИ compile У search ПОЯВЛЯЕТСЯ АРГУМЕНТЫ НАЧАЛО ПОЗИЦИИ С КОТОРОЙ НУЖНО ИСКАТЬ, И ДО КОТОРОЙ НУЖНО ИСКАТЬ!!!!!!!!!!!!

# import re
# S = input()
# k = input()
# m = re.search(k, S)
# pattern = re.compile(k)
# if not m: print("(-1, -1)")
# while m:
#     print("({0}, {1})".format(m.start(),m.end()-1))
#     m = pattern.search(S,m.start()+1)

# import re
# #
#
# pattern = r'(?<= )((&&)|(\|\|))(?= )'
# for _ in range(int(input())):
#     result = re.sub(pattern, lambda x: 'or' if x.group(3) == '||' else 'and', input())
#     print(result)

# import re
# print(True) if re.fullmatch(r'\b[IVXLCDM]+\b', input()) else print(False)

# import re
# pattern = r'^<[a-zA-Z0-9]+[-._a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>'
# for _ in range(int(input())):
#     name, email = input().split()
#     print (name, email) if re.fullmatch(pattern, email) else -1

# import re
# pattern = r'(?!^)#[0-9A-Fa-f]{3,6}'
# for _ in range(int(input())):
#     result = re.findall(pattern, input())
#     print(*result, sep='\n') if result else -1

# import re
#
# # n, w = input().split()
# # matrix = [list(input()) for _ in range(int(n))]
# # pattern = r'(?![^\w+]+$)[^\w+]+'
# # s = ''.join([i for sub in list((zip(*matrix))) for i in sub])
# # print(re.sub(pattern, ' ', s))
#
# num = 92.0506792
# pattern = r'(\.\d\d[1-9]?)\d*' # ИЩЕМ .ЦИФРАЦИФРАЦИФРА_ЕСЛИ_НЕ_0, СОХРАНЯЕМ ЭТОТ КУСОК В ГРУППУ, ИЩЕМ ДАЛЬШЕ ВСЕ ЦИФРЫ ДО КОНЦА.
# print(re.sub(pattern, r'\1', str(num))) # МЕНЯЕМ ВСЕ ЧТО НАШЛИ НА ТО, ЧТО В ГРУППЕ!

# import re
# def remove_consecutive_duplicates(s):
#     pattern = r'(\b[a-zA-Z]+)(\s+(\1\b))+'
#     return re.sub(pattern, r'\1', s)
#
# s = 'alpha beta gamma gamma delta alpha beta gamma gamma delta'
# print(remove_consecutive_duplicates(s))


# ВОТ ТУТ КЛЕВО. МЕНЯЕМ СНАЧАЛА ГЛАСНЫЕ НА ПУСТЫЕ СТРОКИБ А ПОТОМ ВСЕ ОСТАВШИЕСЯ СОГЛАСНЫЕ НА СЕБЯ ЖЕ, ТОЛЬКО С ТОЧКОЙ В НАЧАЛЕ

# import re
# def string_task(s):
#     return re.sub(r"(.)", '.\\1' ,re.sub(r"[aeiouy]", '', s.lower(), flags = re.I))
# s = 'Codewars'
# print(string_task(s))

# import re
# s = 'furrrrXXXlittlexxxxxxx'
# def triple_x(s):
#     pattern = r'(.)\1{2}'
#     result =re.search(pattern, s)
#     print(result)
#
#     return True if (result and s.find('x') == result.start()) else False
#
# print(triple_x(s))

# def reduce(number):
#     while len(number) > 1:
#         number = str(sum(map(int, list(number))))
#     return int(number)
#
#
# def life_path_number(birthdate:str) -> int :
#     my_list = birthdate.split('-')
#     return reduce([reduce(i) for i in my_list])
#
# print(life_path_number('1879-03-14'))

# import re
#
#
# def remove_bmw(string):
#     pattern = r'[bmw]'
#     try:
#         return re.sub(pattern, '', string, flags=re.IGNORECASE)
#     except TypeError:
#         raise TypeError("This program only works for text.")
#
# print(remove_bmw([]))

import re


# def vowel_start(st):
#     result = [i.lower() for i in re.split(r'([aeoiu][^aeoiu]+)', re.sub(r'[\W_]', '', st), flags=re.IGNORECASE) if i != '']
#     print(result)
#     return ' '.join(result)
#
#
# print(vowel_start('wtho'))

# def words_order(text: str, words: list) -> bool:
#     print([i for i in text.split() if i in words])
#     return ([i for i in text.split() if i in words] == words) and (len(set(words)) == len(words))
# # return (''.join([i for i in text.split() if i in words]) == ''.join(words)) and (len(set(words)) == len(words))
#
# print(words_order('hi world im here', ['world', 'here']))

# import re
# def sorting(s):
#
#     pattern = r'(.*\.)(.*)'
#     result = re.search(pattern, s)
#     print((result.group(1), result.group(2)))
#     if result.group(1) == '.':
#         return_value = (result.group(2), '?')
#     elif result.group(2) == '':
#         return_value = (result.group(1), '@')
#     else:
#         return_value = (result.group(1), result.group(2))
#
#     return return_value
#
# def sort_by_ext(my_list):
#     return sorted(my_list, key=lambda x: (sorting(x)[1], sorting(x)[0]))

# ВОТ ТАК ПРОВЕРЯТЬ НА ВЕРХНИЙ РЕГИСТР!!!!
# return False if (not bool(text.strip()) or text.isdigit()) else text.upper() == text

# from typing import Iterable
# def is_ascending(items: Iterable[int]) -> bool:
#     if len(items) > 1:
#         if len(set(items)) == 1:
#             return False
#
#     return items == sorted(items)

# ВОТ ТАК ЛУЧШЕ!!!
# return items == sorted(set(items))

# def isometric_strings(str1: str, str2: str) -> bool:
#     my_dict = {}
#     for i in range(len(str1)):
#         item = my_dict.get(str1[i])
#         if item == None:
#             my_dict[str1[i]] =str2[i]
#         elif my_dict.get(str1[i]) != str2[i]:
#             return False
#     return True

# ВОТ ТАК КРАСИВЕЕ!!!!
# def isometric_strings(str1: str, str2: str) -> bool:
#     cipher = {k:v for (k,v) in zip(str1, str2)}
#     return "".join([cipher[a] for a in str1]) == str2

# from itertools import combinations
# my_string, num_com = input().split()
# for j in range(int(num_com)):
#     [print(''.join(i))  for i in list(combinations(sorted(my_string), j + 1))]

# ВОТ ТАК КОРОЧЕ!
# posibles,k = input().split()
# print(*[''.join(x) for y in range(1,int(k)+1) for x in combinations(sorted(posibles),int(y))],sep='\n')

# from itertools import combinations_with_replacement
# my_string, num_com = input().split()
# [print(''.join(i))  for i in list(combinations_with_replacement(sorted(my_string), int(num_com)))]

# ВОТ ТАК ЭФФЕКТИВНЕЕ ПО ПАМЯТИ!
# s = input().split()
# string, number = sorted(s[0]), int(s[1])
# print(*list(map(''.join, itertools.combinations_with_replacement(string, number))), sep='\n')

# import re
# result = re.search(r'(\d|[a-z])\1', input(), re.IGNORECASE)
# print(result.group(1) if result else -1)

# import re
# pattern = r'(?<=<!--)(.+\n.+)(?=-->)|(?<=<div>)(.+)(?=</div>)|(?<=<!--)(.+)(?=-->)'
# s = ''
#
# for _ in range(int(input())):
#     s += input() + '\n'
# print(s)
# result = re.fullmatch(pattern,s, re.MULTILINE)
# # print(result.group(1), result.group(2), result.group(3), sep='\n')
# print(result)

# import re, sys
#
# regex = r'(?<=<!--)(.+\n.+)(?=-->)|(?<=<div>)(.+)(?=</div>)|(?<=<!--)(.+)(?=-->)'
#
# for m in re.finditer(regex, sys.stdin.read()):
#     titles = ['Multi-line Comment', 'Single-line Comment', 'Data']
#     print(f'>>> {titles[m.lastindex - 1]}')
#     for data in m.group(m.lastindex).split('\n'):
#         print(data)

# cols, rows = map(int, input().split())
# print(*[sum(i)/rows for i in list(zip(*[list(map(float, input().split())) for _ in range(rows)]))], sep='\n')

# x, y = map(int, input().split())
# print(y == eval(input()))

# input()
# numbers = input().split()
# print(not '-' in ''.join(numbers) and any(i == i[::-1] for i in numbers))

# ТАК ЛУЧШЕ!!!!
# n = int(input())
# arr = input().split(" ")
# print(all(int(i)>=0 for i in arr) and any(i == i[::-1]for i in arr))

# СОРТИРОВКА ПО КЛЮЧУ!
# rows, _ = map(int, input().split())
# my_list =[list(map(int, input().split())) for _ in range(rows)]
# k = int(input())
# [print(*i) for i in sorted(my_list, key=lambda x: x[k])]


# ВАЖНО! ОФИГЕННЫЙ ПРИМЕР СОРТИРОВКИ!!! СТРОКА Sorting1234 ПРЕВРАЩАЕТСЯ В ginortS1324

# print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')


# def fibonacci(n):
#     pred = 0
#     tek = 1
#     for i in range(1,n):
#         pred, tek = tek, tek + pred
#
#         print(tek)
#
# fibonacci(6)

# ВАЖНО! ВОТ ТАК ФИББОНАЧЧИ С РЕКУРСИЕЙ!!!
# fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2)
# print map(lambda x: x**3, map(fib, range(input())))

# НАПИСАТЬ САМОСТОЯТЕЛЬНО!!!!!!!

# def is_acceptable_password(a: str) -> bool:
#     # return bool(re.search(r'((?=.{6,})(?=.*\d.*)(?=.*\D.*)|(?=.{10,}))', password))
#     print((re.search(r'^((?!password).)*$', a, re.I)))
#     return bool(re.search(r'((?=.{6,})(?=.*\d.*)(?=.*\D.*)|(?=.{10,}))', a)) and bool(re.search(r'^((?!password).)*$', a, re.I))

# ВОТ ТАКОЙ ШАБЛОН РАБОТАЕТ, НО НЕ СОВСЕМ КОРРЕКТНО, В НАЧАЛЕ ПРОПУСКАЕТ passward
# (?i)(?!.*password)((?=.*\d)(?=.*\D)|(?=.{10})).{7,}

# def line_coord(x1, y1, x2, y2):
#     k = (y2 - y1) / (x2 - x1)
#     b = (x2 * y1 - x1 * y2) / (x2 - x1)
#     ur = f''+str(k) + '*{x} + ' + str(b)
#     # ur2 = '-((' + str(b) + '-{y})/' + str(k)+')'
#     print('k = ' + str(k), 'b = ' + str(b))
#     print(ur)
#     return ur

# def sprava_sleva_vishe_nije(x1, y1, x2, y2):#, xtochki ,ytochki):
    # ur = line_coord(x1, y1, x2, y2)[0].replace('{x}',str(xtochki))
    # ur2 = line_coord(x1, y1, x2, y2)[1].replace('{y}',str(ytochki))
    # yprov = eval(ur)
    # xprov = eval(ur2)
    # if yprov < ytochki:
    #     print('Точка ниже прямой')
    # elif yprov > ytochki:
    #     print('Точка выше прямой')
    # else:
    #     print('Точка равна прямой')
    #
    # if xprov < xtochki:
    #     print('Точка правее прямой')
    # elif xprov > xtochki:
    #     print('Точка левее прямой')
    # else:
    #     print('Точка равна прямой')


    # print(yprov)
    # print(ur)


# line_coord(2,1,1,5)

#
#     text = text.translate(translation_table)

# import re
#
# def unix_match(filename: str, pattern: str) -> bool:
#     # translation_table = str.maketrans({'*': '.*', '?': '.', '.': '\.'})
#     # text = pattern.translate(translation_table)
#
#     result = re.split(r'(?<=\[)([^]]+)(?=\])', pattern)
#
#     print(result)
#     for i in range(len(result)):
#         if i % 2 != 0:
#             if result[i] != '!':
#                 if result[i][0] == '!':
#                     result[i] = result[i].replace('!', '^', 1)
#                 result[i] = result[i].translate(str.maketrans({'*': '.*', '[': '\[', ']': '\]', '?': '.', '.': '\.'}))
#     result = ''.join(result)
#     print(result)
#     result = re.sub(r'(?<!\\)(\[\])', '\[\]', result)
#     result = re.sub(r'(?<!\\)(\[!\])', '\[!\]', result)
#     print(result)
#     return bool(re.fullmatch(result, filename))
    # print(before_skob, skob, after_skob)
# print(unix_match("n[]amce.a!gg2.txtc[]","n[]am[c[]e.[!.][!][!.][!.][123].txt[!abv][]"))
# n[]am[c[]e.[!.][!][!.][!.][123].txt[!abv][] пример шаблона
# n\[\]am[c\[]e.[^.][!][^.][^.][123]\.txt[^abv]\[\] вот такой надо получить
# n[]amce.a!gg2.txtc[] пример совпадающего текста

# ВОТ ТАК ЗНАЧИТЕЛЬНО ПРОЩЕ!!!!!
# import re
#
# PATTERNS = ('.', '\.'), ('?', '.'), ('*', '.*'), ('[!', '[^'), ('[^]', '\[!]'), ('[]', '[^.]')
#
#
# def unix_match(filename, pattern):
#     for a, b in PATTERNS:
#         pattern = pattern.replace(a, b)
#
#     return bool(re.match(pattern, filename))

# ИЛИ ТАК!!!
# from re import search
#
# def unix_match(filename: str, pattern: str) -> bool:
#     try: return search(pattern.replace('[!','[^'),filename).group(0)==filename
#     except: return pattern==filename

# def goes_after(word: str, first: str, second: str) -> bool:
#     return bool(word) and (word.find(first) < word.find(second)) and (first in word) and (second in word) and (first + second in word[word.find(first):word.find(first) + 2])
# ВОТ ТАК ХОРОШО!!!!!!
# def goes_after(word: str, first: str, second: str) -> bool:
#     return word.find(first) + 1 == word.find(second) if first in word else False

# РЕГУЛЯРКА С ПАРАМЕТРАМИ!!!!
# from re import search
#
# def goes_after(word: str, first: str, second: str) -> bool:
#     m = search(rf'[{first}{second}][^{first}{second}]*[{first}{second}]', word)
#     return bool(m) and m.group() == first + second

# from itertools import zip_longest
# def checkio(text, word):
#     my_list = [''.join(i.split()) for i in text.lower().split('\n')]
#
#     for i in range(len(my_list)):
#         result = my_list[i].find(word.lower())
#         if result > 0:
#             return [i + 1, result + 1, i + 1, result + len(word)]
#
#
#     zipp_my_list = []
#     zipped_array = list(map(list, list(zip_longest(*my_list))))
#     for sub in zipped_array:
#         zipp_my_list.append([i for i in sub if i is not None])
#
#     zipp_my_list = [''.join(i) for i in zipp_my_list]
#
#
#     for i in range(len(zipp_my_list)):
#         result = zipp_my_list[i].find(word.lower())
#         if result != -1:
#             return [result + 1, i + 1, result + len(word), i + 1]
#
#


# def time_converter(time):
#     my_list = time.split(':')
#     result = my_list[0] if my_list[0][0] != '0' else my_list[0][1]
#     result = str(int(result) - 12) if int(result) > 12 else result
#     if result == '0':
#         result = '12'
#     return result+':'+my_list[1] + ' p.m.' if int(my_list[0]) >=12 and int(my_list[0]) <= 23 else result+':'+my_list[1] + ' a.m.'

# from typing import Tuple
#
# def sum_by_types(items: list) -> Tuple[str, int]:

    # if not items:
    #     return ('', 0)
    # my_string = ''
    # my_sum = 0
    # for i in items:
    #     if isinstance(i,str):
    #         my_string += i
    #     else:
    #         my_sum += i
    # result = (my_string, my_sum)
    # return result

# ВОТ ТАК С ПОМОЩЬЮ ГЕНЕРАТОРА!!!!!
# return ''.join(e for e in items if isinstance(e, str)), sum(e for e in items if isinstance(e, int))

# import re, functools
# def translate(phrase):
#
#     # result = re.sub(r'(?<=[^aeiouy ])[aeiouy]', '', phrase)
#     # result = re.sub(r'([aeiouy])\1\1', r'\1', result)
#
#
#     # return re.sub(r'([aeiouy])\1\1', r'\1', re.sub(r'(?<=[^aeiouy ])[aeiouy]', '', phrase))
#
#     translate = functools.partial(re.sub, r'(\w)\1?.', r'\1')
#     return translate(phrase)
#
# print(translate("hoooowe yyyooouuu duoooiiine"))

# def checkio(line1: str, line2: str) -> str:
#
#     return ','.join(sorted([i for i in line1.split(',') if i in line2.split(',')]))
#
# # ТО ЖЕ САМОЕ, ЧЕРЕЗ МНОЖЕСТВА!!!
# def checkio(line1: str, line2: str) -> str:
#     return ','.join(sorted(set(line1.split(',')) & set(line2.split(','))))
#

# def follow(instructions):
#     y = [1 if i == 'f' else -1 for i in instructions if i in 'fb']
#     x = [1 if i == 'r' else -1 for i in instructions if i in 'rl']
#
#     return (sum(x), sum(y))
#
# # ВОТ ТАК ПРИКОЛЬНО!!!!!
# follow = lambda i: [i.count(x)-i.count(y) for x, y in ('rl', 'fb')]

# import re
# def check_pangram(text):
#
#     return len(set(re.sub(r'[^a-z]', '', text.lower()))) == 26
#
# # КЛЕВОЕ РЕШЕНИЕ!!!
# from string import ascii_lowercase
# def check_pangram(text):
#     return set(text.lower()).issuperset(ascii_lowercase)

# import re
# def caps_lock(text: str) -> str:
#     result = re.split(r'a', text)
#     print(result)
#     if not bool(result[0]):
#         return ''.join([result[i].upper() if i % 2 == 0 else result[i] for i in range(len(result))])
#     else:
#         return ''.join([result[i].upper() if i % 2 == 1 else result[i] for i in range(len(result))])

# import collections, re
# def checkio(text: str) -> str:
#     print(collections.Counter(text.lower()).most_common())
#
#     return sorted(collections.Counter(re.sub('[^a-z]', '', text.lower())).most_common(), key=lambda x: (-x[1], x[0]))[0][0]
#
# # ВОТ ТАК ЗНАЧИТЕЛЬНО ПРОЩЕ!
# import string
#
# def checkio(text):
#     return max(string.ascii_lowercase, key=text.lower().count)

# import re
# def from_camel_case(name):
#
#     return '_'.join([i.lower() for i in re.split(r'([A-Z][a-z]+)', name) if i])
#
# # ТАК ПРОЩЕ!!!!
# return re.sub(r'\B([A-Z])', r'_\1', name).lower()

# def to_camel_case(name):
#     return ''.join([i.capitalize() for i in name.split('_')])
#
# # ТАК ПРОЩЕ!!!!!
#     return name.title().replace('_', '')
#

# import re
# def try_convert(n):
#     if n.isdigit():
#         result = int(n)
#     elif n == 'false':
#         result = False
#     elif n == 'true':
#         result = True
#     elif n == '':
#         result = None
#     else:
#         result = n
#     return result
# def yaml(a):
#     my_list = a.split('\n')
#     my_dict = {}
#     my_tuple_list = []
#     for i in my_list:
#         st = i.replace(r'\\\\', r'\\')
#         result = re.search(r'(\w+)(?=:):(\s*(\w|\d|\s|,|\.|\"|\\)+)', st)
#         if result is not None:
#             my_dict[result.group(1).strip()] = try_convert(result.group(2).strip())
#
#             # my_tuple_list.append((result.group(1).strip(), try_convert(result.group(2).strip())))
#
#
#     return my_dict#{key:value for key, value in sorted(my_tuple_list, key=lambda x: (-1 if str(x[1]).isdigit() else 0, my_tuple_list.index(x)))}
# #
# # ТАК ПРОЩЕ! ДУМАЙ!!!!!
# def yaml(a):
#     result = a.split('\n')
#     result = [i.split(': ') for i in result if ': ' in i]
#     result = {i[0]: int(i[1]) if i[1].isnumeric() else i[1] for i in result}
#     return result

# print(yaml("name: \"Alex \\\"Fox\\\"\"\nage: 12\n\nclass: 12b"))
#{"age":12,"name":"Alex \"Fox\"","class":"12b"}

# def checkio(*args):
#
#     return (sorted(list(args))[-1] - sorted(list(args))[0]) if args else 0

# import re
#
#
# def find_quotes(a):
#     pattern = r'\b(?<=\").*?(?=\")\b'
#
#     result = re.findall(pattern, a) or ([""] if re.findall(r'\"\"', a.replace('\"','"')) else []) # re.findall(r'\"\"', a.replace('\"', '"')[0].replace('\"','"'+'"'))
#     return result
#
# # ВОТ ТАК КРАСИВО!!!!!
# def find_quotes(a):
#     return a.split('"')[1::2]

# import re
# def long_repeat(line: str) -> int:
#     result = re.findall(r'(.)(\1+)', line)
#     if not bool(result):
#         return 1 if line else 0
#     else:
#         return len(sorted(result, key=lambda x: len(x[1]))[-1][1]) + 1 if line else 0

# ИЛИ ВОТ ТАК!!!! МОЕ РЕШЕНИЕ
# import itertools
# def long_repeat(line: str) -> int:
#     return sorted([len((a[0],*a[1]))-1 for a in itertools.groupby(line)])[-1] if line else 0

# import re
# PATTERN = r'[a-z0-9_-]+@[a-z0-9]+\.[a-z]{,3}'
#
# print(list(filter(lambda x: re.fullmatch(PATTERN, x),[input() for _ in range(int(input()))])).sort())

# from fractions import Fraction
# from functools import reduce
#
# def product(fracs):
#     t = reduce(lambda x,y: x*y, fracs)
#     return t.numerator, t.denominator
#
# if __name__ == '__main__':
#     fracs = []
#     for _ in range(int(input())):
#         fracs.append(Fraction(*map(int, input().split())))
#     result = product(fracs)
#     print(*result)

# import re
# def wrapper(f):
#     def fun(l):
#         f(['+91 ' + re.search(r'((?<=0)(\d{5})(\d{5}))|((?<=91)(\d{5})(\d{5}))', i).group() if len(i) != 10 else '+91 ' + i[2:5] + ' ' + i[5::] for i in l])
#
#
#     return fun
#
# @wrapper
# def sort_phone(l):
#     # print(*sorted(l), sep='\n')
#     print(l)
#
# if __name__ == '__main__':
#     l = [input() for _ in range(int(input()))]
#     sort_phone(l)

# import operator
#
# def person_lister(f):
#     def inner(people):
#
#         return [f(i) for i in sorted(people, key=lambda x: (int(x[2]), people.index(x)))]
#     return inner
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
#
# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')

# Логирование

# import operator
# import functools
# def wrapper(func):
#     funcs_count = {}
#
#     def logger(*args):
#         logger.count += 1
#         print('еще один способ подсчитать кол-во запусков функции. Оказывается, у функции, через точку, можно указывать любой придуманный атрибут!!!! Функция же объект, ну вот.' + str(logger.count))
#         print('логирование началось, запущена функция ' + func.__name__ + ' с аргументами ' + str(args))
#         funcs_count[func.__name__] = funcs_count.setdefault(func.__name__, 0) + 1
#         if funcs_count[func.__name__] > 3:
#             raise Exception('Функция запущена более 3 раз! низзяяя!')
#         result = func(*args)
#         print('логирование завершено, функция ' + func.__name__ + ' запущена ' + str(funcs_count[func.__name__]) + '-й раз')
#         return result
#
#     logger.count = 0
#     return logger
#
# @wrapper
# def my_sum(*args):
#     return sum(args)
#
# @wrapper
# def my_mul(*args):
#     return functools.reduce(operator.mul, args)


# import random
# def test():
#
#     test.test = random.choice(range(10))
#     print(test.test)
#
# testes = [test, test, test]
# for i in testes:
#     print(type(i))
#     i()

# Менеджеры контекста!!!!!!!

# import time
# class Izmerator:
#     def __init__(self):
#         pass
#     def __enter__(self):
#         self.time_start = time.time()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('мы спали ' + str(time.time() - self.time_start))
#
# def vipolnyalka():
#     time.sleep(1)
#     print('проснулся!')
#
# with Izmerator():
#     vipolnyalka()
#
#
# from contextlib import contextmanager
# import time
#
# @contextmanager
# def izmeryalka():
#     izmeryalka.start_time = time.time()
#     yield
#     print('работали ' + str(time.time() - izmeryalka.start_time))
#
# with izmeryalka():
#     print('начали ')
#     time.sleep(1)


# def make_adder(n):
#     def add(x):
#         print('n = ' + str(n))
#         print('x = ' + str(x))
#
#         return x+n
#     return add
#
# plus_3 = make_adder(3)
# plus_3(4)

# Тренируемся с декоратором и контекстным менеджером
# def wraper(funk):
#     def counter(*args):
#         counter.counter += 1
#         print('Функция ' + funk.__name__ + ' запущена в ' + str(counter.counter) + '-й раз')
#         return funk(*args)
#     counter.counter = 0
#     return counter
#
# @wraper
# def summator(*args):
#     return sum(args)
#
# print(summator(1,2,3))
# print(summator(7,9,15))

# import time
# class My_context_manager:
#     def __init__(self):
#         pass
#     def __enter__(self):
#         My_context_manager.counter = 0
#         My_context_manager.start_time = time.time()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         My_context_manager.counter +=1
#
#         print('Run ' + str(My_context_manager.counter) + ' times')
#         print('Work ' + str(time.time() - My_context_manager.start_time))
#
# with My_context_manager():
#     print('Huge code...')
#     time.sleep(2)
#     print('Exit from context')
#     print('test ' + str(My_context_manager.start_time))



# def check_user(username):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             if kwargs.get('username') != username:
#                 print('upsssss..' + username)
#                 return -1
#             print('start some logging...' + username)
#             inner.counter += 1
#             print('func ' + func.__name__ + ' running ' + str(inner.counter) + ' times')
#             result = func(*args)
#             print('end logging')
#             return result
#         inner.counter = 0
#         return inner
#     return wrapper
#
# @check_user('admin')
# def summator(*args, username='test'):
#     return sum(args)
#
# print(summator(1,2,3, username='admin'))
# print(summator(4,7,9, username='adda'))

# def wrapper1(func):
#     def inner(*args):
#         print('w1 start')
#         func(*args)
#         print('w1 end')
#
#     return inner
#
# def wrapper2(func):
#     def inner(*args):
#         print('w222222 start')
#         func(*args)
#         print('w2222 end')
#
#     return inner
#
# @wrapper1
# @wrapper2
# def summator(*args):
#     print(sum(args))
#
#
# summator(1,2,3)

# import re
# def alphabet_war(bf):
#     if '#' in bf:
#         print(re.findall(r'([a-z#]*)\[([a-z]+)\](?=([a-z#]*))',bf))
#         return ''.join(['' if (c[0]+c[2]).count('#') > 1 else c[1] for c in re.findall(r'([a-z#]*)\[([a-z]+)\](?=([a-z#]*))',bf)])
#     return re.sub(r'\[|\]','',bf)
#
# print(alphabet_war('wvl[hio]sz#r[nrk]##ir[xybt]#wqs'))
#
# import re
# def trump_detector(trump_speech):
#     pattern = r'([aeiou])(\1+)'
#     result = re.findall(pattern, trump_speech, flags=re.IGNORECASE)
#     repeated_vowels = sum(len(i[1]) for i in result)
#     total_vowels = sum(1 if j.lower() in 'aeiou' else 0 for j in ''.join([re.sub(pattern, r'\1', i, flags=re.IGNORECASE) for i in trump_speech.split()]))
#     return round(repeated_vowels/total_vowels, 2)

# import re
# def trump_detector(ts):
#     x=re.findall(r'([aeiou])(\1*)',ts,re.I)
#     print(x)
#     y=[len(i[1]) for i in x]
#     print(y)
#     return round(sum(y)/len(y),2)
#
# print(trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT"))