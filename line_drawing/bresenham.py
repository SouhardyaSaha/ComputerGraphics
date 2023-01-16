from draw import draw_figure


def bresenham_line_draw(x1=300, y1=200, x2=400, y2=400):
    # step 2 calculate difference
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    m = dy / dx

    # step 3 perform test to check if pk < 0
    flag = True

    points = [(x1, y1)]

    step = 1
    if x1 > x2 or y1 > y2:
        step = -1

    mm = False
    if m < 1:
        x1, x2, y1, y2 = y1, y2, x1, x2
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        mm = True

    p0 = 2 * dx - dy
    x = x1
    y = y1

    for i in range(abs(y2 - y1)):
        if flag:
            x_previous = x1
            p_previous = p0
            p = p0
            flag = False
        else:
            x_previous = x
            p_previous = p

        if p >= 0:
            x = x + step

        p = p_previous + 2 * dx - 2 * dy * (abs(x - x_previous))
        y = y + 1

        if mm:
            points.append((y, x))
        else:
            points.append((x, y))

    draw_figure(points)
