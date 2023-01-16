from draw import draw_figure


def dda(x1=300, y1=200, x2=400, y2=400):
    # x1 = int(input("Enter X1: "))
    # y1 = int(input("Enter Y1: "))
    # x2 = int(input("Enter X2: "))
    # y2 = int(input("Enter Y2: "))

    # find absolute differences
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    # check the start & end point
    if x1 > x2:
        x, y = x2, y2
        x_end = x1
    else:
        x, y = x1, y1
        x_end = x2

    # find maximum difference
    step_size = max(dx, dy)

    # calculate the increment in x and y
    x_inc = dx / step_size
    y_inc = dy / step_size

    points = []
    while x < x_end:
        points.append((x, y))

        # increment the values
        x = x + x_inc
        y = y + y_inc

    for point in points:
        print(point)

    draw_figure(points)
