x = input()
while x == "":
    x = input()
    ax = float(input("Enter the x coordinate of point A: "))
    ay = float(input("Enter the y coordinate of point A: "))
    bx = float(input("Enter the x coordinate of point B: "))
    by = float(input("Enter the y coordinate of point B: "))
    d = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
    rd = (bx - ax) ** 2 + (by - ay) ** 2
    print(d)
    print(f"root {rd}")
