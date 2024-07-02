# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.


# s = 12
# p = 27 

# for x in range (p):
#     for y in range (p):
#         if s == x + y and p == x * y and x>=y:
#             print(x,y)

# list_1 = [1, 3, 3, 3, 3]
# k = 3
# c = 0
# for i in list_1:
#     if i == k:
#         c += 1
# print(c)       
# numbers = [5, 1, 88, 44, 3]
# target_value = 5
# n= 0
# for i in numbers:
#     n = target_value - i
        
# print ( i if n <=1  else 0)
# 1
# def find_common_elements(var1, var2, var3):
#     n, m = map(int, var1.split())  
#     set1 = set(map(int, var2.split()))
#     set2 = set(map(int, var3.split()))
    
#     common_elements = sorted(set1.intersection(set2))
#     return common_elements
# result = find_common_elements(var1, var2, var3)
# result_str = ' '.join(map(str, result))
# print(result_str)
# n_bushes = [5, 8, 6, 4, 9, 2, 7, 3]
# arr = list()
# for i in n_bushes:
#     a = n_bushes[i]
#     arr.append(a)

# def max_berry_count(arr):
#     n = len(arr)
#     if n == 0:
#         return 0
#     if n == 1:
#         return arr[0]
    
#     max_count = 0
#     for i in range(n):
#         berries = arr[i] + arr[(i+1) % n] + arr[(i+2) % n]
#         max_count = max(max_count, berries)
    
#     return max_count

# # arr = [5, 8, 6, 4, 9, 2, 7, 3]
# print(max_berry_count(arr))
# def f(a, b):
#     if b == 0:
#         return 1
#     elif b > 0:
#         return a * f(a, b - 1)
#     else:
#         return 1 / f(a, -b)

# # Пример использования
# a = 2
# b = 3
# print(f(a, b))

# import modul1
# print(modul1.max1(5, 9))

def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a ^ b, (a & b) << 1)

# Пример использования
result = sum(2, 2)
print(result)  # Выведет 7

def DecToBin (a):

    bin = ''

    while a > 0:

        a, bin = a // 2, str (a % 2) + bin

    print (bin)

DecToBin(12)



def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))

print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]