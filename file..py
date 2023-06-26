db = [
    {'username': 'hello', 'passward': hash('123323')},
    {'username': 'Jon', 'passward': hash('1233288333')}
]


def in_database(username:str) -> bool:
    for user in db:
        if user['username'] == username:
            return True
        return False


def get_user(username:str, password:str) -> dict:
    if not in_database(username):
        raise Exception('Такого пользователя нет')
    for user in db:
        if user['username'] == username:
            if user['password'] != hash(password):
                raise Exception('Пароль не верный')
            else:
                return user


def registr(username:str, password:str, password_confirm:str) -> str:
    if in_database(username):
        raise Exception ('Имя пользователя занято')
    if password != password_confirm:
        raise Exception ('Пароли не совпадают')
    db.append({'username': username, 'passward': hash(password)})
    return 'Вы успешно зарегистрировались'


def login(username:str, password:str) -> str:
    get_user(username, password)
    return 'Вы успешно вошли'


def change_password(username:str, password:str):
    user = get_user(username, password)
    new_passward = input('Введите новый пароль: ')
    index = db.index(user)
    db[index]['password'] = hash(new_passward)
    return 'Пароль изменен'


def delete_account(username:str, password:str):
    user = get_user(username, password)
    db.remove(user)
    return 'Акаунт удален'


def main():
    print('Добро пожаловать!')
    while True:
        try:
            action = input('1-регистрация, 2-login, 3-изменить пароль, 4-удалить аккаунт, 5-выйти: ')
            if action == '5':
                break
            elif action == '1':
                username = input('Введите имя пользователя: ')
                password = input('Введите пароль: ')
                password1 = input('Введите подтверждение пароля: ')
                print(registr(username, password, password1))
            elif action == '2':
                username = input('Введите имя пользователя: ')
                password = input('Введите пароль: ')
                print(login(username, password))
            elif action == '3':
                pass
            elif action == '4':
                pass
            elif action == '5':
                pass
            else:
                print('Не корректный ввод')

        except Exception as error:
            print(error)
            
main()