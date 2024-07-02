# def max1(a,b):
#     if a>b:
#         return a
#     return b

# def calculate_word_score(k):


#     scores_ru = []

  
#     scores = scores_ru
#     score = sum(scores.get(letter.upper(), 0) for letter in k)
#     return score

# result = calculate_word_score(k)
# print(result)
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# indices = [i for i, num in enumerate(list_1) if min_number <= num <= max_number]
# print(indices)


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 4
# max_number = 8

# indices = [i for i, num in enumerate(list_1) if min_number <= num <= max_number]
# print("\n".join(str(index) for index in indices))


# a1 = 2 
# d = 3 
# n = 4

# progression = [a1 + i * d for i in range(n)] 
# print("\n".join(progression))

# a1 = 2 d = 3 n = 4

# progression = [a1 + i * d for i in range(n)] 
# for num in progression: 
#     print(num)

# stroka = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'

# phrases = stroka.split()
# syllables = []
# for phrase in phrases:
#     syllables.append(len([char for char in phrase if char in 'аеёиоуыэюя']))
# if len(phrases) == 1:
#     print('Количество фраз должно быть больше одной!')
# elif len(set(syllables)) == 1:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')
# print(len(phrases))

# def print_operation_table(operation, num_rows=9, num_columns=9): 
#     if num_rows < 2 or num_columns < 2: 
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!") 
#     else:
#         for i in range(1, num_rows+1): 
#             row_values = [str(operation(i, j)) 
#                 for j in range(1, num_columns+1)] 
#             print(" ".join(row_values))

# print_operation_table(lambda x, y: x * y, 3, 3)
import pandas as pd df = pd.read_csv('california_housing_train.csv') avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean() # Средняя стоимость дома, где количество людей от 0 до 500 


import pandas as pd df = pd.read_csv('california_housing_train.csv')
 # Найти минимальное значение 'population' 
min_population = df['population'].min() 

# Отфильтровать строки с минимальным значением 'population' и найти максимальное значение 'households'
max_households_in_min_population = df[df['population'] == min_population]['households'].max()




