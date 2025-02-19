def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    y = x.lower()
    match y:
        case "42":
            return "Yes"
        case "forty-two":
            return "Yes"
        case "forty two":
            return "Yes"
        case _:
            return "No"
        
answer = main()
print(answer)