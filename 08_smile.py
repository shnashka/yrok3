# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1000, 1000)

def smile(x, y, color):
    shar = sd.get_point(x, y)
    sd.circle(shar, 70, color)
    l_e = sd.get_point(x - 30, y + 10)
    sd.circle(l_e, 15, sd.COLOR_BLACK)
    p_e = sd.get_point(x + 30, y + 10)
    sd.circle(p_e, 15, sd.COLOR_BLACK)
    rot1 = sd.get_point(x - 20, y - 30)
    rot2 = sd.get_point(x + 20, y - 30)
    sd.line(rot1, rot2, color, 2)

for _ in range(10):
  point = sd.random_point()
  smile(point.x, point.y, sd.COLOR_YELLOW)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

sd.pause()
