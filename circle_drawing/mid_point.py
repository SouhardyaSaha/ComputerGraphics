from draw import draw_figure

points = []


def eight_way_symmetric_plot(xc, yc, x, y):
    points.append((x + xc, y + yc))
    points.append((x + xc, -y + yc))
    points.append((-x + xc, -y + yc))
    points.append((-x + xc, y + yc))
    points.append((y + xc, x + yc))
    points.append((y + xc, -x + yc))
    points.append((-y + xc, -x + yc))
    points.append((-y + xc, x + yc))


def draw_midpoint_circle(xc=200, yc=200, r=100):
    x = 0
    y = r
    d = 1 - r
    eight_way_symmetric_plot(xc, yc, x, y)

    while x <= y:
        if d <= 0:
            d = d + (2 * x) + 3
        else:
            d = d + 2 * (x - y) + 5
            y = y - 1
        x = x + 1
        eight_way_symmetric_plot(xc, yc, x, y)

    draw_figure(points)
