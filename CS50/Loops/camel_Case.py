def main():
    n = input("camelCase:")
    new_str = ""
    for i in n:
        if i.isupper():
            new_str += "_" + i
        else:
            new_str += i
    return new_str.lower()
answer = main()
print(answer)