#Take the starting annual salary from the user
starting_salary = float(input("Enter the starting salary: "))

#Given constants
total_cost = 1000000 #Total cost of the house

portion_down_payment = 0.25 #25% down payment

down_payment = total_cost * portion_down_payment 

annual_return = 0.04 #4% annual investment return

semi_annual_raise = 0.07 #7% raise every 6 months

months = 36 #Total time period (36 months)

#Bisection search parameters
low = 0 #Lower bound of savings rate (0%)
high = 10000 #Upper bound (100% represented as 10000)
steps = 0 #Count number of bisection steps
best_rate = None #To store the final best rate

#Perform bisection search
while low <= high:
    steps += 1 #Increase step count
    mid = (low + high) // 2 #Find midpoint

    portion_saved = mid / 10000 #Convert to decimal savings rate

    initial_savings = 0 #Initialize savings

    annual_salary = starting_salary #Reset salary for simulation

#Simulate 36 months
    for month in range(1, months + 1):
        monthly_salary = annual_salary / 12  #Monthly salary
        
        #Add monthly investment return
        initial_savings += initial_savings * (annual_return / 12)
        #Add monthly savings from salary
        initial_savings += monthly_salary * portion_saved
        
        #Apply semi-annual raise every 6 months
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    #Check if within $100 
    if (initial_savings >= down_payment - 100) and (initial_savings <= down_payment + 100):
        best_rate = portion_saved #Store best savings rate
        break

    #If savings are too low, increase rate
    elif initial_savings < down_payment - 100:
        low = mid + 1

    #If savings are too high, decrease rate
    else:
        high = mid - 1

#Final Output
if best_rate is None:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)