def strings_checkin(string12, string2):

    if type(string12) == str and type(string2) == str:
        print(1)
    else:
        return 0

    if string12 == string2:
        print('Строки одинаковые')
    elif len(string12) >= len(string2):
        print('Не одинаковые и первая строка больше или равна второй')
    elif string2 == 'learn':
        print(3)

    return 'Проверка закончена'

print(strings_checkin('neme1233', 'learn'))
print(strings_checkin(1, 'learn'))

