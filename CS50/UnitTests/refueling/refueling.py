from fractions import Fraction
import sys

def main():
    while True:
        try:
            n = input("Fraction: ")
            validate_fraction(n)
            percentage = convert(n)
            print(gauge(percentage))
            sys.exit()
        except (ValueError, ZeroDivisionError):
            print("Invalid")

def validate_fraction(fraction):
    fraction_obj = Fraction(fraction)
    if fraction_obj.numerator > fraction_obj.denominator:
        raise ValueError("Invalid")

def convert(fraction):
        x = int(Fraction(fraction) * 100)
        return x

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
        

    