FixedSalary = 1000000000

days = int(input("Enter the days :: "))

VariableSalary = 0

for i in range(1, days+1):
    VariableSalary = VariableSalary + 2**(i-1)

if VariableSalary > FixedSalary:
    print("I will accept the Variable Salary. And the Amount is $", VariableSalary)
else:
    print("I will accept the Fixed Salary. And the Amount is $", FixedSalary)

print("\nTotal Length :: ", len(str(VariableSalary)))
