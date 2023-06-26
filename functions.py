'''========= Введение в функции ========='''
'''Анатации -> помогают сделать код информативным и избавиться от некоторых проблем динамической типизации'''
'''никак не влияет на реботу кода'''
 
num:int = 10 # предупредит какой тип данных нужно передавать
num = 'hello' 
print(num)

'''========= Функции ========='''

# Функция -> именованный блок кода (есть имя), который выполняет одну задачу
# Может принимать в себя аргументы и возвращать результат
# Вызывается многократно, по имени

# def -> ключивое слово для объявления функции (указывает питону, что мы хотим создать функцию)

'''Синтаксис'''

# def 'название функции'('параметры, если нужно'):
    # 'тело функции'

def my_len(obj):
    count = 0 
    for i in obj:
        count += 1
        print(count)
        return count

my_len([1, 2, 3, 4, 5])
a = my_len([1, 2, 3, 4, 5])
print(a)


def sum_(n1, n2):
    print(n1 + n2)
sum_(3, 6)
sum_(4, 'hello')


'''return -> используется для возвращения результата, который можно сохранить в переменной и где-то использовать'''
'''после return функция завершает свою работу'''
'''если в функции не прописан return функция возвращает None'''


str_ = 'hello'
print(str_.replace('h', 'e'))


'''========= Параметры и аргументы ========='''

# Параметры -> переменные внутри функции, значения этим параметрам задаютсч при вызове функции
# Аргументы -> значения которые мы задаем параметрам

def a(d):
    pass
a(39)

'''========= Виды параметров ========='''

# 1. Обязательные (a, b, list_ ...) -> определяют какие аргументы нужно передать
def f(a):
    print(a)
f(3)

# 2. Необязательные:

# 2.1 Имеют значение по умолчанию
def f(a = 3):
    print(a)
f(7) #тогда работает с 7

# 2.2 args -> принимает неизменяемые аргументы (tuple)
def f(a, *args):
    print(a)
    print(args)
f(3, 4, 5, 6)

# 2.3 kwargs -> принимает именованные аргументы (dict)
def f(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)
f(3, 4, 5, n = 0)


'''========= Виды аргументов ========='''

# 1. Позиционные - по позиции
def f(a, b, c):
    print(a, b, c)
f(2, 4, 6)

#2. Именованные (задаем значение по названию переменной)
def f(a, b, c):
    print(a, b, c)
f(b = 2, c = 4, a = 6)


# Распакоука (*) или для ключа и значения (*) (**)
l = [*range(1,11)]
print(l)


def sum_numbers(number1, number2, *args, **kwargs):
    print(args, kwargs)
    print(kwargs.values())
    return number1 + number2 + sum(args) + sum(kwargs.values())
print(sum_numbers(1, 7))
print(sum_numbers(1, 7, 99, 8, 5, n = 9, k = 87, o = 0))


while True:
    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        return x / y
    
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    
    choice = input("Введите номер операции (1/2/3/4): ")
    
    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    elif choice == '4':
        result = divide(num1, num2)
        operation = '/'
    else:
        print("Неверный ввод")
        exit()

    print(f"{num1} {operation} {num2} = {result}")