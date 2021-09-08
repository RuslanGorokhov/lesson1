while True:
    hello_user = input('Как дела? ')
    if hello_user == 'Хорошо' or 'Отлично':
        print('Отлично!')
        break
    else:
        print('Что значит плохо? {}'.format(hello_user))