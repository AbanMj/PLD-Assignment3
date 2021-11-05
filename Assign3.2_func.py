#apple_item = int(input("How many apples you want to buy?: "))
#orange_item = int(input("How many oranges you want to buy?: "))
#price_apple = 20
#price_orange = 25
#total = (apple_item*price_apple) + (orange_item*price_orange)
#print(f"The total amount you should pay is {total}.")

def o_piecesf():
    orange = int(input("How many orange you want to buy?: "))
    return orange

def a_piecesf():
    apple = int(input("How many apple you want to buy?: "))
    return apple

def priceOf():
    priceO = 25
    return priceO

def priceAf():
    priceA = 20
    return priceA
    
def totalOf(orange, priceO):
    total_orange = orange * priceO
    return total_orange

def totalAf(apple, priceA):
    total_apple = apple * priceA
    return total_apple

def payf(total_apple, total_orange):
    bill = total_apple + total_orange
    return bill

def displayoutput(bill):
    print(f"The total amount you will pay is {bill}")

orange = o_piecesf()
apple = a_piecesf()
priceO = priceOf()
priceA = priceAf()
total_orange = totalOf(orange, priceO)
total_apple = totalAf(apple, priceA)
bill = payf(total_apple, total_orange)
displayoutput(bill)