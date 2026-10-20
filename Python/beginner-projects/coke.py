price = 50
amount_due = 0
cent_coins = [10, 25, 5]
change = 0

while amount_due < price:
    
    coin = int(input("Insert Coin: "))
    
    for i in cent_coins:
        if coin == i:
            amount_due+=i
            print(f"Amount Due: {price-amount_due}")
        
        elif amount_due >= price:
            print(f"Change Owed: {change}")
            break
        change= price-amount_due