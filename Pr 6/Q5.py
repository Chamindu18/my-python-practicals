item1 = "Apple"
amount1 = 2.3
price1 = "5.99"

item2 = "Orange"
amount2 = "3"
price2 = 3.50

item3 = "Mango"
amount3 = 5
price3 = 2

price1 = float(price1)
amount1 = int(amount1)
amount2 = int(amount2)

no_item = amount1 + amount2 + amount3
total_price = (amount1*price1) + (amount2*price2) + (amount3*price3)

print(f"total number of items: {no_item}")
print(f"Total price : {round(total_price,2)}")


