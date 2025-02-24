def main():
    names = []
    while True:
        try:
            n = input("Name: ")
            names.append(n)

        except EOFError:
            if len(names) == "":
                break
            if len(names) == 1:
                print(f"Adieu, adieu, to {names[0]}")
            elif len(names) == 2:
                print(f"Adieu, adieu, to {names[0]} and {names[1]}")
            else:
                print("Adieu, adieu, to " + ", ".join(names[:-1]) + ", and " + names.pop())
            break

if __name__ == "__main__":
    main()