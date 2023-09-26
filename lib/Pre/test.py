pricess=[3,2,6,5,0,3]
def prof(prices):
    profit = 0
    i = 0
    j = len(prices) - 1
    while (i < j):
        if prices[i] > prices[j] and prices[i] > prices[i+1]:
            i += 1
        else:
            profit = max(profit, prices[j] - prices[i])
            if prices[j] < prices[j - 1]:
                # print(1)
                j -= 1
            else:
                # print(2)
                i += 1
    return profit
d=prof(pricess)
print(d)