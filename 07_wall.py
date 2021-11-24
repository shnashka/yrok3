# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (1000, 1000)
sd.background_color = sd.COLOR_RED
y = 100
x = 100
dlok_h = 50
blok_l = 100
for i in range(10):
    y += dlok_h
    Nachalo = sd.get_point(100, y)
    close = sd.get_point(600, y)
    sd.line(Nachalo, close, sd.COLOR_DARK_GREEN, 1)
    if i % 2 == 0:
        x = 100
        for _ in range(5):
            x += blok_l
            Nachalo = sd.get_point(x, y)
            close = sd.get_point(x, y + dlok_h)
            sd.line(Nachalo, close, sd.COLOR_BLUE, 1)
    if i % 2 != 0:
        x = 50
        for _ in range(5):
            x += blok_l
            Nachalo = sd.get_point(x, y)
            close = sd.get_point(x, y + dlok_h)
            sd.line(Nachalo, close, sd.COLOR_BLACK, 1)


sd.pause()