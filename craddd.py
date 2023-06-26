categories = [
    'веб-разработка',
    'разработка мобильных приложений',
    'разработка игр'
]

subcategories = [
    'python',
    'javaScript',
    'java'
]

levels = [
    'начальный',
    'средний',
    'профессиональный'
]
id = 0
def get_id():
    def inner():
        global id
        id += 1
    inner()
    return id


db = {
    get_id(): {
        'category': 'веб-разработка',
        'subcategory': 'python',
        'level': 'начальный',
        'title': 'Веб-разработка для начинающих',
        'description': 'Эффективные модели и практики организации профориентационной и научно-исследовательской работы с детьми с применением современных технологий',
        'price': {'currency': 'сом', 'sum': 5000}
    }
}

def get_courses():
    return db

def get_course(id: int) -> dict:
    course = db.get(id)
    if course:
        return course
    else:
        raise Exception('Такого курса нет')
    

def validate_data(data):
    if data['category'] not in categories:
        raise Exception('Такой категории нет')
    if data['subcategory'] not in subcategories:
        raise Exception('Такой подкатегории нет')
    if data['level'] not in levels:
        raise Exception('Такого уровня нет')
    
    if len(data['title']) > 60 :
        raise Exception('Максимальное кол-во символов 60')
    
    if len(data['description'].split()) < 10:
        raise Exception('Слишком короткое описание, минимум должно бфть 10 слов')
    # print(data[1]['description'].split())
    if data['price']['currency'] == 'dollar':
        data['price']['currency'] = 'сом'
        data['price']['sum'] *= 87.2
    return data 


def delete_course(id: int):
    try:
        poped = db.pop(id)
        return poped
    except KeyError:
        return f'Курса с таким id - {id} нет'

    
def update_course(id: int):
    course = db.pop(id)
    print(course)

    choise = input('Что вы ходите изменить (title - 1, description - 2, price - 3)')
    if choise == '1':
        course['title'] = input('Введите новый заголовок: ')
    elif choise == '2':
        course['description'] = input('Введите новое описание: ')
    elif choise == '3':
        course['price']['currency'] = input('Введите валюту: ')
        course['price']['sum'] = int(input('Введите новую стоимость курса: '))
    else:
        return 'Такого выбора нет'
    validated_data = validate_data(course)
    db.update({id: validated_data})
    return {'msg': 'Курс успешно обновлен'}


def create_course():
    new_course = {
            'category': input(f'Выберите категорию {categories}: '),
            'subcategory': input(f'Выберите подкатегорию {subcategories}: '),
            'level': input(f'Выберите уровень курса {levels}: '),
            'title': input('Введите название курса: '),
            'description': input('Введите описание курса: '),
            'price': {'currency': input('Выберите валюту (cом/dollar): '), 'sum': float(input('Введите стоимость курса: '))}
        }
    validated_data = validate_data(new_course)
    new_course = {get_id(): validated_data}
    db.update(new_course)
    return {'msg': 'Вы курс успешно создан'}

def main():
    print('Привет, Тебе доступны следующие действия: 1 - listing, 2 - retrive, 3 - create, 4 - update, 5 - delete ')
    choise = input('Выберите действие: ')
    if choise == '1':
        print(get_courses())

    elif choise == '2':
        id = int(input('Введите id курса: '))
        print(get_course(id))
    
    elif choise == '3':
        print(create_course())
    
    elif choise == '4':
        id = int(input('Введите id курса: '))
        print(update_course(id))
    
    elif choise == '5':
        id = int(input('Введите id курса: '))
        print(delete_course(id))

    else:
        print('Такого действия нет')
    
    ask = input('Хотите продолжить? да/нет: ')
    if ask.lower() == 'да':
        main()
    else:
        print('Пока')

main()