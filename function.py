import random

def rasp():
    day_week = input("Выберите текущий день недели: ПН, ВТ, СР, ЧТ, ПТ, СБ, ВС: ")
    if day_week == "ПН":
        print("Сегодня: математика, русский, ин-яз, физика")
    elif day_week == "ВТ":
        print("Сегодня: физика, физ.-культура, русский, классный час")
    elif day_week == "СР":
        print("Сегодня: математика, обществознание, литература, классный час")
    elif day_week == "ЧТ":
        print("Сегодня: математика, ин-яз, история, классный час")
    elif day_week == "ПТ":
        print("Сегодня: физика, ОБЗР, python, биология")
    elif day_week == "СБ":
        print("Сегодня: русский, литература")
    elif day_week == "ВС":
        print("Сегодня выходной")
    else:
        print("Извините, я вас не понял!")


def dyim():
    unit = input("Вы хотите перевести дюймы или футы? (введите 'дюйм' или 'фут'): ")

    if unit == "дюйм":
        inches = int(input("Введите количество дюймов: "))
        centimeters = inches * 2.54
        print(f"{inches} дюймов = {centimeters} сантиметров.")
    elif unit == "фут":
        feet = int(input("Введите количество футов: "))
        meters = feet * 0.3048
        print(f"{feet} футов = {meters} метров.")
    else:
        print("Не понял, введите 'дюйм' или 'фут'.")


def clc():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
        print("Результат:", result)
    elif operation == "-":
        result = num1 - num2
        print("Результат:", result)
    elif operation == "*":
        result = num1 * num2
        print("Результат:", result)
    elif operation == "/":
        if num2 == 0:
            print("На ноль делить нельзя!")
        else:
            result = num1 / num2
            print("Результат:", result)
    else:
        print("Неверная операция")

def convert():
    yuan = 11.16
    eur = 91.75
    usd = 88.34

    rub = float(input("Введите количество рублей: "))
    print(rub, "RUB =", rub / yuan, "CNY")
    print(rub, "RUB =", rub / eur, "EUR")
    print(rub, "RUB =", rub / usd, "USD")

def veronika():
    s = random.randint(1, 100)
    a = 5
    print("Робот загадал число от 1 до 100.")

    for i in range(a):
        print("Попытка", str(i + 1), "из", a)
        g = int(input("Введите ваше число: "))

        if g < s:
            print("Загаданное число больше.")
        elif g > s:
            print("Загаданное число меньше.")
        else:
            print("Поздравляем! Вы угадали число", str(s), "!")
            break
    else:
        print("Попытки закончились. Загаданное число было", str(s), ".")