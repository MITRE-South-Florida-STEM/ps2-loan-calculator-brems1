starting_salary = float(input("Enter your starting salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25*total_cost
r = 0.04

h = 10000
l = 0
portion_saved = int((h+l)/2)
steps = 0
current_savings = 0
months = 0
salary_increase_months = 0

while(months <= 36):
    portion_saved = portion_saved/1000
  
    if(salary_increase_months == 6):
        starting_salary += starting_salary*semi_annual_raise
        salary_increase_months = 0
    current_savings += current_savings*(r/12) + portion_saved*(starting_salary/12)
    salary_increase_months += 1
    months += 1

    if(months == 36):
        if current_savings < portion_down_payment:
            l = portion_saved
            months = 0
        elif current_savings > portion_down_payment:
            h = portion_saved
            print('Best savings rate:', portion_saved)
            print('Steps in bisection search:', steps)
            break
        else:
            print('It is not possible to pay the down payment in three years.')
            break
        