'''Облости видимости и пространства имен'''

'''пространства имен'''

name = 'hello'

# 1. builtins (встроенные) ->  все, что встроено в стандартную библиотеку питона (print, input, len...)
# 2. global (глобальное) -> все переменные внутри файла, которые мы создали (без табуляции)
print(globals()) # -> возвращает все глобальные переменные
print(dir(__builtins__)) # -> возвращает все встроенные имена
# 3. enclosed (не локальное, замкнутое) -> находится между двумя пространствами
# 4. local (локальное) 

a = 100
b = 0
z = 99
globals()['a'] = 45
print(globals())
 

'''локальные -> переменные (в функциях)'''

def f(test):
    a =10
    d = 20
    print(locals())

f(6)

# {test: 6, 'a': 10, 'b': 20}

locals() # -> выводит имена той области в которой находится


def f1():
    a = 1
    b = 2
    print(a, b)
def o():
    global a
    a = 8
    def i():
        global a
        a = 10
        print('i', a)
    i()
    print('o', a)

o()
print('global', a)
f1()


'''enclosed'''

# возникает при вложенности функция (функция в функции)

def f1():
    a = 88 # не локальная
    print(a)
    def f2():
        b = 99 # локальная
        print(b)

    f2()
f1()


'''порядок поиска переменных'''
# local -> enclosed -> global -> builtins


x = 10

def f():
    global x # изменяет global
    x = 20
    print(x)
f()
print(x)


c = 0

def cr():
    global c 
    c += 1
    return c

name = input()
age = input()

print({id: cr(), 'name': name, 'age': age})

a = 0

def o():
    a = 8
    def i():
        nonlocal a # изменяет enclosed
        a = 10
        print('i', a)
    i()
    print('o', a)

o()
print('global', a)


from time import sleep
def cr(n):
    c = 0

    def add():
        nonlocal c
        c += 1
        print(c)
        sleep(1)

    for i in range(n):
        add()

cr(10)