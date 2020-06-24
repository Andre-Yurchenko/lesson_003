# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
x = []
print(x)
x.append(1)
print(x)

for key in goods:
    for k in (store[goods[key]]):
        quantity = []  # создать список, добавлять в него каждую итерацию
        y = (k['price'])

        if goods[key] == '23456':
            m = k['quantity']
            quantity.append(m)
        else:
            print('Товаров с кодом {}: {} шт'.format(goods[key], quantity))

     elif goods[key] == '23456':
         print('Стол')
         print(s['quantity'], s['price'])
     elif goods[key] == '34567':
         print('Диван')
     elif goods[key] == '45678':
         print('Стул')