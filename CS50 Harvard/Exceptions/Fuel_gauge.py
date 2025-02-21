from fractions import Fraction
def main():
    while True:
        try:
            n = input("Fraction: ")
            x = int(Fraction(n) * 100)
        except ValueError:
            continue

        try:
            if x >= 99:
                return "F"
            elif x <= 1:
                return "E"
            else:
                return f"{x}%"
        except ZeroDivisionError:
            continue

print(main())
        

    