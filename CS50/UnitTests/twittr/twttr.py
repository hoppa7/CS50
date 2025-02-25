def main():
    n = input("Input:")
    return shorten(n)

def shorten(n):
    vowels = ["a", "e", "i", "o", "u"]
    for i in n:
        if i.lower() in vowels:
            n = n.replace(i, "")
    return(n)

answer = main()
print(answer)