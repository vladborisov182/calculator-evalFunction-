#Функция, проверяющая правильность ввода
def num_test(str):
    while True:
        try:
            x = float(input("Введите " + str + " значение: "))
            return x
        except ValueError:
            print("Вы ввели неправильный символ!")
            continue
        break
#Сама программа
print("Для завершения программы введите q вместо знака операции")
while True:
    s = input("Введите знак операции (+, -, *, /)")
    if s is "q":
        print("Программа завершена")
        break
    if s in ("+", "-", "*", "/"):
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
