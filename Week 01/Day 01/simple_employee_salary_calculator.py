print("===== Employee Salary Calculator =====")

name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10
tax = basic_salary * 0.05

gross_salary = basic_salary + hra + da
net_salary = gross_salary - tax

print("\nEmployee Name:", name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Tax:", tax)
print("Net Salary:", net_salary)