def main():
    x, y, z = input("Expression:").split(" ")
    match y:
        case "+":
            return float(x) + float(z)
        case "-":
            return float(x) - float(z)
        case "/":
            return float(x) / float(z)
        case "*":
            return float(x) * float(z)
        case _:
            return
        
answer = main()
print(answer)