monthly_income = float(input("Enter your monthly income: "))

monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

annual_interest_rate = 0.05

projected_annual_savings = monthly_savings * 12 * (1 + annual_interest_rate)

print(f"Your monthly savings are: ${monthly_savings:.2f}")

print(f"Your projected annual savings after including interest are: ${projected_annual_savings:.2f}")
