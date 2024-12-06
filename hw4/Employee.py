# Dallin Moore

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary *= 1 + percent
        
employee_john = Employee("John", 5000)
employee_john.increase_salary(.1)
print("Increased salary:",employee_john.salary)