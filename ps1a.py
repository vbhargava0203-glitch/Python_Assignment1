#Take annual salary input from the user
annual_salary = int(input("Enter your annual salary: "))

#Take the portion of salary to save, as a decimal)
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

#Take the total cost of the dream home
total_cost = int(input("Enter the cost of your dream home: "))

#Initialize number of months to 0
no_of_months = 0

#Initialize current savings to 0
initial_savings = 0

#Calculate down payment (25% of total cost)
down_payment = total_cost * 0.25

#Annual return rate on investment (4%)
return_on_investment = 0.04

#Calculate monthly salary
monthly_salary = annual_salary / 12

#Calculate monthly return rate
monthly_return_rate = return_on_investment / 12

#Loop until savings reach or exceed the down payment
while initial_savings < down_payment:

#Add monthly savings + monthly investment return
    initial_savings += (portion_saved * monthly_salary) + (initial_savings * monthly_return_rate)
#Increase month count
    no_of_months += 1

#Print the total number of months needed
print("Number of months: ", no_of_months)
