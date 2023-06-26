'''========= Обработка исключений ========='''

# Ошибки - проблемы с синтаксисом

SyntaxError # -> забыли двоеточиеб скобку...
IndentationError # -> неправельный отступ
TabError # -> неправильная табуляция


# Исключения - код написан правельно, но работае не так как ожидалось

ArithmeticError # -> арифмитические ошибки
ZeroDivisionError # -> ошибка деления на ноль
ValueError # -> ошипка типа данных (при распаковке, переводе однго типа донных в другой)
NameError # -> обращение к несуществующей переменной по несуществующему имени
TypeError # -> ошибка типа (сложение числа и строки, передача в функцию не верного количества элементов)
KeyError # -> обращение к несуществующиму ключу
IndexError # -> обращение к несуществующиму индесу
AttributeError # -> обращаемся к несуществующему методу объекта (используем для списка метод словаря)
ImportError # -> неправильный импорттируемый объект
ModuleNotFoundError # -> импорт несуществующей библтиотеки (вместо import math, - import mat)
BaseException # -> прородитель ошибок


'''========= try exept ========='''
# Чтобы код не прекращал работу при ошибке в нем

try:
    'тело' 'try'
# код который может вызвать ошибку
except:
    'тело' 'except'
# код который сработает если в try возникнет ошибка
else:
    'тело' 'else'
# код который отработает если в try ошибки не будет
finally:
    'тело' 'finally'
# код который отработает в любом случае


try:
    num = int(input('Введите число: '))
    num2 = int(input('Введите число: '))
    res = num/num2
except ValueError:
    print('Введите только число!')
    num = int(input('Введите число: '))
except ZeroDivisionError:
    print('На 0 делить нельзя!')
else:
    print(res)
finally:
    print('пака')


try:
    d = {key: key ** 2 for key in range(11) if key % 'a' == 0}
    print(d)
except NameError:
    print('Переменная а не объявленна')


try:
    i = int(input())
except Exception as e:
    print(e)


try:
    a = int(input())
    b = int(input())
    d = a + b
except ValueError:
    print('Введите только число!')
    a = int(input())
    b = int(input())
    print(a + b)
else:
    print(d)


while True:
    try:
        a = int(input())
        b = int(input())
    except ValueError:
        print('Введите только число!')
        a = int(input())
        b = int(input())
        print(a + b)
    else:
        print(d)
        break


'''========= raise ========='''
# исскуственно вызывает ошибку

try:
    age = int*input('Ваш возраст ')
    if age < 18:
        raise ValueError('Пшол вон')
    print('Pithup')
except ValueError:
    print('Вы ввели не число или вам нет 18')