# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 600)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
point = sd.get_point(100, 100)
color = sd.random_color()
radius = 50
coordinate_x = sd.get_point(60, 90)
coordinate_y = sd.get_point(90, 110)
x = sd.get_point(100, 90)
y = sd.get_point(130, 120)
side = 10
q = sd.get_point(80, 80)
w = sd.get_point(100, 80)

def smile(coordinate_x, coordinate_y, color):
    sd.circle(center_position=point, radius=radius, color=color, width=2)
    sd.ellipse(left_bottom=coordinate_x, right_top=coordinate_y, color=color, width=0)
    sd.ellipse(left_bottom=x, right_top=y, color=color, width=0)
    sd.line(start_point=q, end_point=w, color=color, width=1)



smile(coordinate_x, coordinate_y, color)
sd.pause()
