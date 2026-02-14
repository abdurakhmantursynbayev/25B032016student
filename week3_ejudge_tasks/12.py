class employee:
    def __init__(self,name,  base_salary):
        self.name = name
        self.base_salary = base_salary
    def total_salary(self):
        return self.base_salary
class manager(employee):
    def __init__(self,name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent
    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)
class developer(employee):
    def __init__(self,name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects
    def total_salary(self):
        return self.base_salary + self.completed_projects * 500
class intern(employee):
    def __init__(self,name,  base_salary):
        super().__init__(name, base_salary)
    def total_salary(self):
        return super().total_salary()

typeworker, name, *left = map(str, input().split()) 
if typeworker == "Manager":
    x = manager(name, int(left[0]), int(left[1]))
    print(f"Name: {x.name}, Total: {x.total_salary():.2f}")
if typeworker == "Developer":
    x = developer(name, int(left[0]), int(left[1]))
    print(f"Name: {x.name}, Total: {x.total_salary():.2f}")
if typeworker == "Intern":
    x = intern(name, int(left[0]))
    print(f"Name: {x.name}, Total: {x.total_salary():.2f}")