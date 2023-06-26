'''========= Camprehension ========='''
# Генерация последовательности в одну строку, используя цикл For (синтаксический сахар)

for i in range(11):
    break

Создание = ['результат' for элемент in 'итеррируемый объект']

Фильтрация = ['результат' for элемент in 'итеррируемый объек ' 'if']

'''========= List comprehension ========='''
# Упрощение процесса создания списков:

list_ = []
for i in 'hello':
    list_.append(i)
    print(list_)


list_ = [i for i in 'hello']
print(list_)


list_ = list_((i for i in 'hello'))
print(list_)


'''Time'''

import time

start_time = time.time()

list_ = []
for i in 'hello':
    list_.append(i)
    print(list_)

print(time.time() - start_time)


a = [i for i in range(11) if i % 2 == 0]
print(a)

'''две переменные'''

a = ['четное' if i % 2 == 0 else 'нечетное' for i in range(11)] 
print(a)


'''========= Dict comprehension ========='''

d = {1: 'a', 2: 'b', 3: 'c'}

d = {v: k for k, v  in d.items()}
print(d)

d = {k: v ** 2 for k, v in d.items()}

d = {i: i ** 2 for i in range(1, 11)}
print(d)

l = [1, 1, 2, 3, 2, 1, 4, 5, 3, 2, 1, 2]
d = {i: l.count(i) for i in l}
print(d)

d = {'a': 1 ,'b': 2 ,'c': 3}
d = {k: ('четное' if v % 2 == 0 else 'нечетное') for k, v in d.items()} 
print(d)

l1 = {1,2,3,4,5}
l2 = {'a','b','c','d','e'}
d = {l1[index]: l2[index] for index in range(len(l1))}
print(d)


'''========= Вложенные comprehensions ========='''

d = {i: [j for j in range(1, i + 1)] for i in range(1, 6)}
print(d)

l = [['hello world' for i in range(5)]for i in range(3)]
print(l)

employees = {
'id1': {
        'first name': 'Александр',
        'last name' : 'Иванов',
        'age': 30,
        'job':'программист'
            },
    'id2': {
        'first name': 'Ольга',
        'last name' : 'Петрова',
        'age': 35,
        'job':'ML-engineer'
            }
}

d = {
    key: 
    {k: float(v) 
    if k == 'age' else v 
    for k, v in value.items()} 
    for key, value
    in employees.items()}