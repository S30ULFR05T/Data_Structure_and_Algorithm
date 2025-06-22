def buy_sell_stock(arr):
    n = len(arr)

    min_purchase = arr[0]
    max_profit = 0

    for i in range(0, n):
        temp = i -min_purchase
        print("temp value:", temp)

        if temp > max_profit:
            max_profit = temp
            print("max profit temp", max_profit)

        if i < min_purchase:
            min_purchase = i
            print("min purchase", min_purchase)

    return max_profit

arr = [7, 1, 5, 3, 6, 4]

stocks = buy_sell_stock(arr)
print("Max Profit: ", stocks)