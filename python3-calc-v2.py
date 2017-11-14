#!/usr/bin/python3

def num_test(str):
    
    '''
    Функция, проверяющая правильность ввода
    '''
    
    while True:
        try:
            x = float(input("Введите " + str + " значение: "))
            return x
        except ValueError:
            print("Вы ввели неправильный символ")
        else:
            break


if __name__ == "__main__":
    print("Для завершения программы введите q вместо знака операции")
    while True:
        s = input("Введите знак операции (+, -, *, /)")
        if s == "q":
            print("Программа завершена")
            break
        elif s in ("+", "-", "*", "/"):
            a = str(num_test("первое"))
            b = str(num_test("второе"))
    # Логика калькулятора и вывод ответа
            try:
                print('{} + {} = '.format(a, b), eval(a + s + b))
            except ZeroDivisionError:
                print('{} / {} '.format(a, b))
                print("Деление на ноль!")
        else:
            print("Неверный знак")
