def main():
    money = 0
    x = input("Greeting:")
    if x == "Hello":
        money = 0
    elif x.startswith("H"):
        money = 20
    else:
        money = 100
    return f"${money}"

answer = main()
print(answer)