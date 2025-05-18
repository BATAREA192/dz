import function

def main():
    print("Доступные функции:")
    print("1. Угадай")
    print("2. Перевод длины из имперской систему в метрическую")
    print("3. Калькулятор")
    print("4. Конвертирование валют")
    print("5. Угдайка(код вероники)")

    choice = input("Введите номер функции, которую хотите запустить (1-5): ")

    if choice == '1':
        function.rasp()
    elif choice == '2':
        function.dyim()
    elif choice == '3':
        function.clc()
    elif choice == '4':
        function.convert()
    elif choice == '5':
        function.veronika()
    else:
        print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")


main()
