x = input("")
while x == "":
    x = input()
    mx = int(input("Enter the x coordinate of the midpoint: "))
    my = int(input("Enter the y coordinate of the midpoint: "))
    ax = int(input("Enter the x coordinate of point A: "))
    ay = int(input("Enter the y coordinate of point A: "))
    bx = 2 * mx - ax
    by = 2 * my - ay
    print(f"({bx}, {by})")