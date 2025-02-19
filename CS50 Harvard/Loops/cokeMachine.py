def main():
    coke_cost = 50
    change_owed = 0
    print(f"Amount Due: {coke_cost}")
    while coke_cost > 0:
        insert_coin = int(input("Insert Coin:"))
        if insert_coin  in {5, 10, 25}:
            coke_cost -= insert_coin
            if coke_cost < 0:
                break
            print(f"Amount Due: {coke_cost}")
        else:
            print(f"Amount Due: {coke_cost}")
            continue
    if coke_cost < 0:
        change_owed = abs(coke_cost)
        print(f"Change owed:{change_owed}")
    return change_owed
            
    
answer = main()