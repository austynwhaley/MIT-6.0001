# house hunting

# Write a program to calculate how many months it will take you to save up enough money for a down
# payment. You will want your main variables to be floats, so you should cast user inputs to floats.


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04

monthly_income = annual_salary / 12

months = 0

while current_savings < portion_down_payment:
    monthly_return = current_savings * r / 12
    monthly_savings = monthly_income * portion_saved
    current_savings += monthly_savings + monthly_return 
    months += 1



print("Number of months: ", months)


