def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = float(dollars) * float(percent)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = d.replace("$", "")
    dollars = float(dollars)
    return (f"{dollars:.1f}")


def percent_to_float(p):
    percent = p.replace("%", "")
    percent = float(percent) 
    return (f"{percent / 100}")


main()