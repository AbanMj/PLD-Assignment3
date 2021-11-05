def moneyfunc():
    cash = int(input("Enter how much money you have: "))
    return cash

def pricefunc():
    apple_price = int(input("Enter the price of apple: "))
    return apple_price

def apple_maxfunc():
    print("Maximum number of apple you can buy: 50")

def number_of():
    apple = int(input("Enter how many apple you want to buy: " ))
    return apple

def payfunc(apple_price, apple):
    bill = apple_price*apple
    return bill

def changefunc(cash, bill):
    change = cash - bill 
    return change

def output(apple, change):
    print(f"You can buy {apple} apples and your change is {change} pesos.")

cash = moneyfunc()
apple_price = pricefunc()
max = apple_maxfunc()
apple = number_of()
bill = payfunc(apple_price, apple)
change = changefunc(cash, bill)
output(apple, change) 