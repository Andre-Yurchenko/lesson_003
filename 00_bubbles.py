# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step, color, radius):
    radius = 50
    point = sd.get_point(x, y)
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)


# Нарисовать три ряда по 10 пузырьков

# for y in range(100, 301, 100):
#    for x in range(100, 1001, 100):
#        point = sd.get_point(x, y)
#        bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# for _ in range(300):
#     for _ in range(10):
#         color = sd.random_color()
#         for _ in range(100):
#             radius = sd.randint(10, 50)
#     point = sd.random_point()
bubble(point=point, color=color, radius=radius, step=5)

sd.pause()
