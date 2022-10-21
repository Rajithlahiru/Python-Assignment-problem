print('Press 1 to get calculations for circle')
print('Press 2 to get calculations for rectangle')
print('Press 3 to get calculations for rectangle')
inp1 = input('Enter:')
if inp1 == '1':
    print('Press A to calculate diameter')
    print('Press B to calculate circumference')
    print('Press C to calculate area')

    inp2 = input('Enter: ')

    PI = 3.14
    if inp2 == 'C':
        r = float(input("Enter the radius of a circle:"))
        area = PI * r * r
        print("Area of a circle = %.2f" % area)
    elif inp2 == 'B':
        r = float(input("Enter the radius of a circle:"))
        circumference = 2 * PI * r
        print("circumference of a circle = %.2f" % circumference)
    else:
        r = float(input("Enter the radius of a circle:"))
        diameter = 2 * r
        print("Diamter of a circle = %.2f" %diameter)

elif inp1 == '2':
    print('Press A to calculate perimeter')
    print('Press B to calculate area')

    inp2 = input('Enter: ')

    if inp2 == 'A':
        d = float(input("Enter the width of a square: "))

        perimeter = 4 * d
        print("perimeter of a rectangle = %.2f" % perimeter)

    else:
        d = float(input("Enter the width of a square: "))

        area = d * d
        print("perimeter of a rectangle = %.2f" % area)


else:
    print('Press A to calculate perimeter')
    print('Press B to calculate area')

    inp2 = input('Enter: ')

    if inp2 == 'A':
        d = float(input("Enter the width of a rectangle: "))
        w = float(input("Enter the height of a rectangle: "))

        perimeter = (w + d) * 2
        print("perimeter of a rectangle = %.2f" %perimeter)

    else:
        d = float(input("Enter the width of a rectangle: "))
        w = float(input("Enter the height of a rectangle: "))

        area = d * w
        print("area of a rectangle = %.2f" %area)



        
