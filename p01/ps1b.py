# Write a program to calculate how many months it will take you save up enough money for a down
# payment.  Like before, assume that your investments earn a return of r = 0.04 (or 4%) and the
# required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
# 4. The semi­annual salary raise (semi_annual_raise)


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04
months = 0


while current_savings < portion_down_payment:
        
    monthly_income = annual_salary / 12
    monthly_return = current_savings * r / 12
    monthly_savings = monthly_income * portion_saved
    current_savings += monthly_savings + monthly_return 
    months += 1
    
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise



print("Number of months: ", months)