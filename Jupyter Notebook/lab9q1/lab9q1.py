#!/usr/bin/env python
# coding: utf-8

# # Understanding Inheritance in Python
# <img style="float: left "src="inheritance.png">

# In[71]:


class Person:
    print("Person")
    def __init__(self, name, age):
        
        self.name = name
        self.age = age

        print(self.name, "is", self.age)
    
    def birthday(self):
        print("Happy birthday you were", self.age)

# Sample Input
p = Person('Kevin', 45)


# In[73]:


class Employee(Person):
    
    pay = 400
    print("Employee")
    
    def __init__(self, name, age, idno):
        Person.__init__(self, name, age)
        
        self.birthday()
        
        print("you are now", self.age + 1)
        print("Your Pay:", float(self.pay))
        
    def calculatePay(self, working_hour):
        base_pay = 7.5
        extra = 2.50
        
        if self.age < 21:
            return "Your Pay:", self.base_pay * self.working_hour
        
        elif self.age > 21:
            return "Your Pay:", (self.base_pay * self.working_hour) + extra
        
        else:
            return "Please enter valid age."

# Sample Input
e = Employee('Den', 21, 7468)    


# In[75]:


class SalesPerson(Employee):
    print("SalesPerson")
    
    def __init__(self, name, age, idno, region, total_sale):
        Employee.__init__(self, name, age, idno)        
        print("Bonus:",total_sale * 0.5)
    def bonus(self):
        return "Bonus:",total_sale * 0.5
    
s = SalesPerson('Phoebe',21, 4712, 'AUS', 30000.0)


# In[ ]:




