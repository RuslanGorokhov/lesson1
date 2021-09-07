
# Задание 1
user = input('Введите свой возрост: ')

def years(user):
    if user < 0:
        return 'Вы должны учиться в дет.саду!'
    elif 1 <= user <= 15:
        return 'Вы должны учитсья в школе!'
    elif 16 <= user <= 24:
        return 'Вы должны учиться в Вузе!'
    else:
        return 'Вы должны работать!'
print(years(50))
print(user)


