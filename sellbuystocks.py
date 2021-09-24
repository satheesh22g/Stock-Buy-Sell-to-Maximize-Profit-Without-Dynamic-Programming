
def maxprofit(lst):
    profit=0
    current=lst[0]
    for i in range(len(lst)):
        if current>lst[i]:
            profit+=lst[i-1]-current
            current=lst[i]
    profit+=lst[-1]-current
    return profit

lst1= [100, 180, 260, 310, 40, 535, 695]
lst2= [100, 180, 260, 310, 40, 535, 695, 20, 388, 490]
print(maxprofit(lst1))
print(maxprofit(lst2))


'''
Output:
865
1335
'''
