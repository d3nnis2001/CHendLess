

def print_donut(radius):
    # Print the outer circle
    for i in range(radius * 2 + 1):
        for j in range(radius * 2 + 1):
            distance = (i - radius) ** 2 + (j - radius) ** 2
            if distance > radius ** 2:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    # Print the inner circle
    for i in range(radius * 2, 0, -1):
        for j in range(radius * 2 + 1):
            distance = (i - radius) ** 2 + (j - radius) ** 2
            if distance > radius ** 2:
                print(' ', end='')
            else:
                print('*', end='')
        print()

print_donut(100)