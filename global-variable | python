
********************************************** Global Variable ****************************************************

The variable which are declared inside the python file and outside the function or class are called global variable.
                                The scope of global variable is anywhere.
                                

--------------------------------------------------------------------------------------------------------------------

a = 1010        # global declaration

def global_example():
    print("inside the function.")
    print(a)
    
print("I am Global: ",a)
global_example()
print("My Scope is everywhere: ",a)

------------------------------------------------------------------------------------------------------------------
 



************************************************************************************************************************

                    we can't modify global variable value inside a function.
                      The local variable will get memory on function call.
               The local memory will get deleted when controller exit the function.
                    The global variable will get memory at run-time.
          If the global variable is modified by one fuction, will affect to other function.
                    
 ************************************************************************************************************************
 
a = 1001010
def function_name():
    a = 1010
    print(a)
    
print(a)        # global a
function_name()     # function call
print(a)      #  print global 'a' because scope of function is only inside the function 

------------------------------------------------------------------------------------------------------------------------------

def official_tech():
    global a        # we can't assign value here ^^
    a = 1001010     # here 'a' is global
    print(a)
    
official_tech()
print(a)

-------------------------------------------------------------------------------------------------------------------------------

********************************* modify global variable inside function ******************************************************
    
a = 1001010
def __function():
     global a
     a = 1000010
     print(a)

print(a)           # a = 1001010 
__function()        # a = 1000010
print(a)       # now 'a' is modified by global a so a = 1000010 

