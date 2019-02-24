
************************************* DIFFERENT WAY TO CALL FUNCTIONS FROM ONE MODULE **********************************

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:28:45 2019

@author: official-tech
"""

a = 1010  # CODE IS STARATING FROM HERE
def fun1():
    print("First block of function")
    
def fun2(x, y = 10):
    global a
    a = 90
    print(x + y + a)
    print("Second block of function")
    
def fun3():
    b = 50
    fun1()
    print(a + b)
    print("Third block of function")
    
    
*********************************************** SAVE THIS ABOVE MODULE AS A 'sample1.py' ************************************
    
**************************************************** calling global variable only ******************************************
    
    
# calling global variable only

from sample1 import a
print(a)


********************************************** calling one function **********************************************************


# calling one function

from sample1 import fun1
fun1()


********************************************* calling one function with alias name ******************************************


# calling one function with alias name

from sample1 import fun3 as f
f()


**************************************************** calling two functions *************************************************


# calling two functions

from sample1 import fun1, fun2

fun1()
print("------------------------")

fun2(10)
print("------------------------")

fun1()
print("------------------------")

fun2(y = 980, x = 320)


******************************************* calling one function and one variable ******************************************

# calling one function and one variable

from sample1 import fun1, a
print(a)
fun1()


******************************************************* calling all *******************************************************

# calling all

from sample1 import *

print(a)

fun1()

fun2(540)

fun3()


----------------------------------------- OR calling all using import ----------------------------------------------------

import sample1
print(sample1.a)
sample1.fun3()
