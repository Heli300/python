'''Task 1 — Personal Information
Create variables for:
Name
Age
City
Qualification
Experience
Display all information.'''

name = "Heli"
age = 22
city = "Ahmedabad"
qualification = "BCA"
experience = "Fresher"
print(name,age,city,qualification,experience)

'''Task 2 — Employee Salary
Create:
basic_salary = 30000
allowance = 5000
bonus = 3000
Calculate:
Total Salary = Basic Salary + Allowance + Bonus'''

basic_salary = 30000
allowance = 5000
bonus = 3000

Total_Salary = basic_salary + allowance + bonus

print(Total_Salary)

'''Task 3 — Sales Calculation
Create:
quantity = 10
unit_price = 2500
Calculate total sales.'''

quantity = 10
unit_price = 2500

total_sales = quantity * unit_price

print(total_sales)

'''Task 4 — Profit Calculation
Create:
sales = 100000
cost = 75000
Calculate:
Profit
Profit Percentage'''

sales = 100000
cost = 75000

Profit = sales - cost
Profit_percentage = (Profit / sales) * 100

print(Profit)
print(Profit_percentage)

'''Task 5 — Average Marks
Create marks for five subjects:
Python
SQL
Excel
Power BI
Statistics
Calculate:
Total marks
Average marks'''

python = 80
sql = 75
excel = 85
power_bi = 90
statistics = 70

total_marks = python + sql + excel + power_bi + statistics
average_marks = total_marks / 5

print(total_marks)
print(average_marks)

'''Task 6 — Customer Bill
Take the following from the user:
Product name
Quantity
Unit price
Calculate and display:
Product
Quantity
Unit Price
Total Amount'''

product = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
unit_price = float(input("Enter Unit Price: "))

total_amount = quantity * unit_price

print(product)
print(quantity)
print(unit_price)
print(total_amount)

'''Task 7 — Discount Calculation
Given:
price = 50000
discount = 10
Calculate:
Discount Amount
Final Price'''

price = 50000
discount = 10

Discount_Amount = price * discount / 100
Final_Price = price - Discount_Amount

print(Discount_Amount)
print(Final_Price)

'''Task 8 — Data Analyst Salary
Take the following inputs:
Employee Name
Monthly Salary
Calculate:
Annual Salary'''

employee_name = input("Enter Employee Name: ")
monthly_salary = float(input("Enter Monthly Salary: "))

annual_salary = monthly_salary * 12

print(employee_name)
print(monthly_salary)
print(annual_salary)

'''Problem 1
Create a program that accepts:
Employee name
Monthly salary
Bonus
Calculate annual income.'''

employee_name = input("Enter Employee Name: ")
monthly_salary = float(input("Enter Monthly Salary: "))
bonus = float(input("Enter Bonus: "))

annual_income = (monthly_salary * 12) + bonus

print(employee_name)
print(monthly_salary)
print(bonus)
print(annual_income)

'''Problem 2
Create a program that accepts:
Product name
Quantity
Price
Discount %
Calculate the final bill amount.'''

product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price: "))
discount_percent = float(input("Enter Discount %: "))

total_amount = quantity * price
discount_amount = (total_amount * discount_percent) / 100
final_bill = total_amount - discount_amount

print(product_name)
print(quantity)
print(price)
print(discount_percent)
print(total_amount)
print(discount_amount)
print(final_bill)

'''Problem 3
A company has:
January Sales = ₹50,000
February Sales = ₹65,000
March Sales = ₹75,000
Calculate:
Total Sales
Average Sales
Highest Sales   
Lowest Sales'''

january_sales = 50000
february_sales = 65000
march_sales = 75000

total_sales = january_sales + february_sales + march_sales
average_sales = total_sales / 3
highest_sales = max(january_sales, february_sales, march_sales)
lowest_sales = min(january_sales, february_sales, march_sales)

print(total_sales)
print(average_sales)
print(highest_sales)
print(lowest_sales)

'''Problem 4
A company sold 150 laptops at ₹45,000 each. The cost of each laptop was ₹38,000.
Calculate:
Total Revenue
Total Cost
Total Profit
You should identify:
Quantity = 150
Selling Price = 45000
Cost Price = 38000'''

quantity = 150
selling_price = 45000
cost_price = 38000

total_revenue = quantity * selling_price
total_cost = quantity * cost_price
total_profit = total_revenue - total_cost

print(total_revenue)
print(total_cost)
print(total_profit)