while True:
    hello_user = input('Как дела? ')
    if hello_user == 'Хорошо'':
        print('Отлично!')
        break
    else:
        print('Что значит плохо? {}'.format(hello_user))
