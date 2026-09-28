# EMPLOYEE SALARY USING ABSTRACT CLASS

from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):
    def salary(self):
        print("Developer Salary = 50000")

class Manager(Employee):
    def salary(self):
        print("Manager Salary = 80000")

d = Developer()
m = Manager()

d.salary()
m.salary()