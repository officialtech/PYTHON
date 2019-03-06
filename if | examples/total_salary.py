
print(15 * "*", " m for MANAGER ", 15 * "*")
print(15 * "*", " a for ANALYST ", 15 * "*")
print(15 * "*", " c for CLERK ", 15 * "*")


name = input("Name: ")
salary = float(input("Salary: "))
designation = input("Designation: ")


def employee(designation):
    if designation == 'm':
        print("Total Salary", ((salary * 20)/100 + salary))
    elif designation == 'a':
        print("Total Salary", ((salary * 10)/100 + salary))
    else:
        print("Total Salary", ((salary * 5)/100 + salary))

    return "Have a Nice Time!"


print(employee(designation))
