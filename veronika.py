import random

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