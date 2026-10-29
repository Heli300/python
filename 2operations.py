'''Task 1 — Number Classification
   Take a number and determine whether it is:
   Positive
   Negative
   Zero'''

number=int(input("Enter A Number:"))
if number > 0:
    print("positive")
elif number < 0:
    print("nagative")
else:
    print("zero")

'''Task 2 — Even or Odd
   Take a number and determine whether it is even or odd. Use %.'''

number=int(input("Enter A Number:"))
if number % 2 == 0:
    print("even")
else:
    print("odd")

'''Task 3 — Sales Classification
   Sales	Category
   >= 100000	Excellent
   >= 75000	Good
   >= 50000	Average
   < 50000	Poor'''

sales=int(input("Enter Sales Amount:"))
if sales >= 100000:
    print("Excellent")
elif sales >= 75000:
    print("Good")
elif sales >= 50000:
    print("Average")
else:
    print("Poor") 

'''Task 4 — Profit or Loss
   Take sales and cost and determine profit or loss'''

sales = 50000
cost = 40000
if sales > cost:
    profit = sales - cost
    print("Profit =", profit)
elif sales < cost:
    loss = cost - sales
    print("Loss =", loss)
else:
    print("No Profit, No Loss")

'''Task 5 — Customer Segmentation
Purchase	Customer Type
>= 100000	Premium
>= 50000	Gold
>= 25000	Silver
< 25000	Regular'''

purchase = 75000
if purchase >= 100000:
    print("Customer Type: Premium")
elif purchase >= 50000:
    print("Customer Type: Gold")
elif purchase >= 25000:
    print("Customer Type: Silver")
else:
    print("Customer Type: Regular").

'''Task 6 — Discount Calculator
Amount	Discount
>= 100000	20%
>= 50000	10%
>= 25000	5%
< 25000	0%
Calculate the final amount.'''

amount = 75000
if amount >= 100000:
    discount = amount * 20 / 100
elif amount >= 50000:
    discount = amount * 10 / 100
elif amount >= 25000:
    discount = amount * 5 / 100
else:
    discount = 0
final_amount = amount - discount
print("Purchase Amount =", amount)
print("Discount =", discount)
print("Final Amount =", final_amount)


'''Task 7 — Employee Bonus
Take employee sales and profit.
Sales >= 100000 AND Profit >= 20000
→ Bonus Eligible
Otherwise
→ Not Eligible'''

sales = 150000
profit = 25000
if sales >= 100000 and profit >= 20000:
    print("Bonus Eligible")
else:
    print("Not Eligible")

'''Task 8 — Data Validation
Take customer age.
18 to 100 → Valid
Otherwise → Invalid'''

age = 25
if age >= 18 and age <= 100:
    print("Valid")
else:
    print("Invalid")

'''Task 9 — Student Result
90+ → A
75–89 → B
60–74 → C
35–59 → D
Below 35 → Fail'''

marks = 82
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")

'''Task 10 — Order Validation
Take quantity and unit price.
Both must be greater than 0.
Display Valid Order or Invalid Order.'''

quantity = 5
unit_price = 1200
if quantity > 0 and unit_price > 0:
    print("Valid Order")
else:
    print("Invalid Order")

'''Challenge Task — Customer Classification
Take:
Customer Name
Purchase Amount
Number of Orders
Rules
Premium:
Purchase >= 100000 AND Orders >= 10
Gold:
Purchase >= 50000 AND Orders >= 5
Silver:
Purchase >= 25000
Regular:
Everything else

Display:
Customer Name
Purchase Amount
Number of Orders
Customer Segment'''

customer_name = "Heli"
purchase_amount = 120000
number_of_orders = 12
if purchase_amount >= 100000 and number_of_orders >= 10:
    customer_segment = "Premium"
elif purchase_amount >= 50000 and number_of_orders >= 5:
    customer_segment = "Gold"
elif purchase_amount >= 25000:
    customer_segment = "Silver"
else:
    customer_segment = "Regular"

print("Customer Name:", customer_name)
print("Purchase Amount:", purchase_amount)
print("Number of Orders:", number_of_orders)
print("Customer Segment:", customer_segment)