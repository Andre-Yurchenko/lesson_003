# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом


user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
if month == 1:
    print('31 день')
elif month == 2:
    print('28 дней')
elif month == 3:
    print('31 день')
elif month == 4:
    print('30 дней')
elif month == 5:
    print('31 день')
elif month == 6:
    print('30 дней')
elif month == 7:
    print('31 день')
elif month == 8:
    print('31 день')
elif month == 9:
    print('30 дней')
elif month == 10:
    print('31 день')
elif month == 11:
    print('30 дней')
elif month == 12:
    print('31 день')
else:
    print('Не верно введен месяц')
