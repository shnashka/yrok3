# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

coord_in = [50, 50]
coord_out = [350, 450]
for i in range(7):

    point_out = sd.get_point(coord_in[0], coord_in[1])
    point_in = sd.get_point(coord_out[0], coord_out[1])
    coord_in[1] += 5
    coord_out[1] += 5
    sd.line(point_out, point_in, rainbow_colors[i], 4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

coord = [500, -100]

for i in range(7):
    point = sd.get_point(coord[0], coord[1])
    R = 200
    sd.circle(point, R + i*20, rainbow_colors[i], 20)

sd.pause()
