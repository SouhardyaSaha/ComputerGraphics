from draw import draw_figure


def bresenham_line_draw():
    # x1 = int(input("Enter X1: "))
    # y1 = int(input("Enter Y1: "))
    # x2 = int(input("Enter X2: "))
    # y2 = int(input("Enter Y2: "))

    x1 = 20
    y1 = 20
    x2 = 400
    y2 = 400

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy / float(dx)

    x, y = x1, y1

    # checking the slope if slope > 1 then interchange the role of x and y
    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # initialization of the initial decision parameter
    p = 2 * dy - dx

    points = []
    for k in range(2, dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy
        x = x + 1 if x < x2 else x - 1

        # delay for 0.01 secs
        # time.sleep(0.01)
        print(x, y)
        points.append((x, y))

    draw_figure(points)
