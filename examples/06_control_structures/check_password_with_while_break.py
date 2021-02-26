username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

while True:
    if len(password) < 8:
        print('Пароль слишком короткий\n')#true
    elif username in password:
        print('Пароль содержит имя пользователя\n')#true
    else:
        print('Пароль для пользователя {} установлен'.format(username))#false
        # завершает цикл while
        break
    password = input('Введите пароль еще раз: ')
