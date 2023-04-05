class Person:
    def __init__(self,name,gender,age,salary):
        self.name = name
        self.gender = gender
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"სახელი {self.name},სქესი {self.gender},წლოვანება{self.age},ხელფასი{self.salary}"
    def monthly_salary(self):
        shemosavali = self.salary / 5
        pensia = self.salary / 100
        return shemosavali + pensia
    def danazogi(self):
        danazogi =(self.salary/100)*12
        if danazogi = "female"
           return self.age * 30
        if danazogi = "male"
           return self.age * 35


























