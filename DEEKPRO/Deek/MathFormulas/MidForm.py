while True:
    ax = float(input("Enter the x coordinate of point A: "))
    ay = float(input("Enter the y coordinate of point A: "))
    bx = float(input("Enter the x coordinate of point B: "))
    by = float(input("Enter the y coordinate of point B: "))
    if ax == bx == ay == by:
        break
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    print(f"The midpoint is ({mx}, {my})")