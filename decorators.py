'''Декораторы'''

def o(x):
    def i(y):
        return x + y
    return i

i_func = o(9)
print(i_func(8))


'''функция высшего порядка -> функция которая может принимать в качестве аргумента другую функцию и, 
или возвращать функцию как результат'''

def test_f(func):
    def i_test_f():
        func()
        # тело
    return i_test_f

def hello(func):
    # тело
    pass


'''декоратор -> функция высшего порядка (в качестве аргумента принимает функцию и возвращает функцию), 
которая оборачивает другую функцию для расширения её функцианала при этом не изменяя её код'''

def test(func):
    func()
    print('hello')

def a():
    print('hi')

test(a)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def benchmark(func):
    import time
    start = time.time()
    func()
    end = time.time()
    print(end - start)

def loop():
    i = 0
    while i < 1000000:
        print(i)
        i += 1

benchmark(loop)

def test_for_loop():
    for i in range(1000000):
        print(i)

benchmark(test_for_loop)


'''синтаксис'''

def decorator(func):
    def wrapper():
        print('обертка')
        print('оборачиваем функцию')
        func()
        print('выходим из обертки')
    return wrapper

@decorator
def sey_hi():
    print('hi')

sey_hi()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def upper_d(func):
    def wrapper():
        func_ = func()
        upper_str = func.upper()
        return upper_str
    return wrapper

@upper_d
def inp_str():
    str_ = input()
    return str_

print(inp_str())

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def benchmark(func):
    import time
    start = time.time()
    func()
    end = time.time()
    print(end - start)

@benchmark
def loop():
    i = 0
    while i < 1000000:
        print(i)
        i += 1

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def benchmark(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)
    return wrapper

@benchmark
def loop():
    i = 0
    while i < 1000000:
        print (i)
        i += 1

loop()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def smart(func):
    def wrapper(x, y):
        print('======')
        if y == 0:
            return
        return func(x, y)
    return wrapper

@smart        
def division(x, y):
    return x/y 

print(division(6, 3))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def i1(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@i1(6)
def greet(name):
    print(f"Hi, {name}!")

greet("Niga")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def strong(func):
    def wrapper():
        return '<strong>' + func() + '<strong>'
    return wrapper

@strong
def get():
    return 'Hello'

print (get())