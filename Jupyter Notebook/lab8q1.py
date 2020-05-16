#!/usr/bin/env python
# coding: utf-8

# # Ticket Machine

# In[37]:


class ticketMachine:
    """ticketMachine class, which models a ticket machine that issues flat-fare tickets"""
    
    # class attribute 
    balance = 0
    
    # instance attribute
    def __init__(self):
        
        self.price_of_ticket = 200
        
        
    def insertMoney(self):
        
        self.amount = int(input("Enter Amount Want to Deposit: "))
        if self.amount <= 0:
            print("Please Enter a valid amount.")
        
        self.balance += self.amount
        print("\nAmount deposited successfully!")
        
        
    def getPrice(self):
        
        print("The Price of one ticket is ${}".format(self.price_of_ticket) + ".")
        return self.price_of_ticket
        
        
    def getBalance(self):
        
        print("Your Balance is ${}".format(self.balance) + ".")
        return self.balance
    
    
    def printTicket(self):
        
        if self.balance >= self.price_of_ticket:
            print("You've successfully printed your ticket.")
            self.balance -= self.price_of_ticket
        
        elif self.balance < self.price_of_ticket:
            print("Insufficient funds to print the ticket, Please insert money.")
        
        else:
            print("Something went wrong!")
        


# In[38]:


object_of_class = ticketMachine()


# In[39]:


object_of_class.insertMoney()


# In[40]:


object_of_class.getBalance()


# # If you not want to return balance or that 400 just commet the return line in getBalance() method

# In[41]:


object_of_class.printTicket()


# ### Now again going to check the balance

# In[42]:


object_of_class.getBalance()


# In[ ]:




