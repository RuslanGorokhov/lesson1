# Задание 2_if
def strings_checkin(string12, string2):
    if type(string12) == str and type(string2) == str:
        return 1
    else:
        return 2

print(strings_checkin('name1', 'name2'))