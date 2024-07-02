def interface():
    print("Добрый день! Вы попали на специальный бот от Geekbrains! \n 1- запись данных \n 2 - вывод данных ")
    command = int(input('Введите число '))

    while command != 1 and command != 2:
        print("Неправильный ввод")
        command = int(input('Введите число '))
    if command == 1:
        input data()
    elif command == 2:
        print data()