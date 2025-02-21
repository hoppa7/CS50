def main():
    groceries = {}
    while True:
        try:
            n = input()
            n = n.upper()
            if n not in groceries:
                groceries[n] = 1
            elif n in groceries:
                groceries[n] = groceries.get(n) + 1
                
        except EOFError:
            sorted_dic = dict(sorted(groceries.items()))
            for k, v in sorted_dic.items():
                print(f"{v} {k}")
            break
main()