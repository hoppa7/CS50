def main():
    x = input("Greeting:")
    return value(x)
    
def value(x):
    x = x.lower()
    money = 0
    if x == "hello":
        money = 0
    elif x.startswith("h"):
        money = 20
    else:
        money = 100
    return f"${money}"

answer = main()
print(answer)