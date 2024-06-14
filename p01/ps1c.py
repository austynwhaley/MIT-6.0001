def calculate_savings_rate(starting_salary):
    semi_annual_raise = 0.07
    annual_return = 0.04
    house_cost = 1000000
    down_payment_percentage = 0.25
    total_months = 36
    required_down_payment = house_cost * down_payment_percentage
    
    # Bisection search range
    low = 0
    high = 10000
    steps = 0
    best_saving_rate = -1
    
    while low <= high:
        steps += 1
        guess = (low + high) // 2
        saving_rate = guess / 10000.0
        
        current_savings = 0.0
        monthly_salary = starting_salary / 12
        
        for month in range(1, total_months + 1):
            current_savings += current_savings * (annual_return / 12)
            current_savings += monthly_salary * saving_rate
            
            if month % 6 == 0:
                monthly_salary += monthly_salary * semi_annual_raise
        
        if abs(current_savings - required_down_payment) <= 100:
            best_saving_rate = saving_rate
            break
        elif current_savings < required_down_payment:
            low = guess + 1
        else:
            high = guess - 1
    
    if best_saving_rate == -1:
        print("It is not possible to save for the down payment in 36 months.")
    else:
        print(f"Best savings rate: {best_saving_rate:.4f}")
        print(f"Steps in bisection search: {steps}")

# Test case
starting_salary = float(input("Enter the starting salary: "))
calculate_savings_rate(starting_salary)
