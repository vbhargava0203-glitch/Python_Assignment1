#Take input from the user: annual salary
annual_salary = int(input("Enter your annual salary: "))

#Percentage of salary the user wants to save (in decimal form)
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

#Cost of the dream home
total_cost = int(input("Enter the cost your dream home: "))

#Semi-annual raise percentage (in decimal form)
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#Initialize number of months to 0
no_of_months = 0

#Initialize current savings to 0
initial_savings = 0

#Calculate required down payment (25% of total cost)
down_payment = total_cost * 0.25

# Annual rate of return on investments (4%)
return_on_investment = 0.04

#Calculate monthly salary
monthly_salary = annual_salary / 12

#Calculate monthly return rate from annual return
monthly_return_rate = return_on_investment / 12

#Loop until savings reach the required down payment
while initial_savings < down_payment:
#Add monthly savings and monthly investment return
    initial_savings += (portion_saved * monthly_salary) + (initial_savings * monthly_return_rate)
#Increase month count
    no_of_months += 1

#Every 6 months, apply the semi-annual raise
    if no_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

#Print the total number of months needed
print("Number of months: ", no_of_months)
