# Implement a program that demonstrates polymorphism by creating a base class and derived classes with overridden methods.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        raise NotImplementedError("Subclasses must implement this method.")

class FullTimeEmployee(Employee):
    def calculate_pay(self):
        return self.salary  # Full-time employees receive their fixed monthly salary.

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, hourly_rate)
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.salary * self.hours_worked  # Part-time employees are paid based on hours worked.

# Function to demonstrate polymorphism
def print_employee_pay(employee):
    print(f"{employee.name}'s Pay: ${employee.calculate_pay()}")

# Example usage:
john = FullTimeEmployee("John Doe", 4000)
jane = PartTimeEmployee("Jane Smith", 20, 80)

# Polymorphism in action
print_employee_pay(john)  # Outputs: John Doe's Pay: $4000
print_employee_pay(jane)  # Outputs: Jane Smith's Pay: $1600
