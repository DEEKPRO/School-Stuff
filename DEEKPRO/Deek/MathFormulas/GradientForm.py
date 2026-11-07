while True:
    ax = float(input("Enter the x coordinate of point A: "))
    ay = float(input("Enter the y coordinate of point A: "))
    bx = float(input("Enter the x coordinate of point B: "))
    by = float(input("Enter the y coordinate of point B: "))
    if ax == bx == ay == by:
        break
    g = (ay - by) / (ax - bx)
    print(g)