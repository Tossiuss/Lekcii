'''Циклы'''
# Цикл - повторяющийся блок кода

'for' #-> проходится по итерируему объекту:
list, str, set, dict, tuple


'while' # -> работает пока условие верно

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'break' # -> останавливает цикл при условии if

i = 0
while i < 6:
    i +=1
    if i == 3:
        break
    print(i)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'continue' # -> начинает следующий круг цикла, пропуская оставшееся тело цикла (срезает круг)

i = 0
while i < 6:
    i +=1
    if i == 3:
        print('333')
        continue
        print('55555') # (под continue ничего не работает)
    print(i)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'else' # -> если цикл закончился полностью отработав то код в else работает, 
       # если цикл был прерван (break) то не сработает

for i in range(1, 11):
    if i == 20:
        break
    print(i)
else:
    print('цикл кончелся без break')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'pass' # -> просто конец, заглушка

for i in range(1, 11):
    pass

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

while 'логическое вырщжение':
    print()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n = int(input())
mn = 0
while n > 0:
    if n % 10 > mn:
        mn = n % 10
    n = n //10
print(mn)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n = int(input())
mn = 0
while n > 0:
    if n % 10 > mn:
        mn = n % 10
    n = n //10
print(mn)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

list_ = [1, 2]
for i in list_:
    list_.append(i)
    print(i) # бесконечный цикл (Ctri + c "останавливает")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

a = 0
while a < 10:
    a = a + 1
    print(f'hello {a}')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

number = int(input("Enter number: "))
sum_ = 0
for i in str(number):
    sum_ += int(i)
print(sum_)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

number = int(input("Enter number: "))
d = 0
l = 0
while l < len(str(number)):
    d += int(str(number)[l])
    l += 1
print(d)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

a = 0
while True:
    a = a + 1
    print(f'hello {a}') # бесконечный цикл (Ctri + c "останавливает")