###########################################################################################################################
#                                      There are four ways to define functions                                            #
###########################################################################################################################




That are:-

###########################################################################################################################
#                                     1. Function without argument and without return                                     #
###########################################################################################################################


###########################################################################################################################
#                                     2. Function with argument and without return                                        #
###########################################################################################################################


###########################################################################################################################
#                                     3. Function without argument and with return                                        #
###########################################################################################################################


###########################################################################################################################
#                                     4. Function with argument and with return                                           #
###########################################################################################################################



************************************* argument = any number of times *****************************************************
*************************************** return = will be only one ********************************************************


_________________________________________EXAMPLES_________________________________________________________________________

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# FUNCTION WITHOUT ARGUMENTS AND WITHOUT RETURN

def sum():
    a = 540
    b = 404
    print("Sum is", a + b)
sum()


###########################################################################################################################
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# FUNCTION WITH ARGUMENTS AND WITHOUT RETURN 

def sum(x, y, z = 980):      # x and y are required arg's z is default arg.
    print("Total", x + y + z)
    
sum(320, 540)  # x = 320  y = 540

sum(98, 32, 54)   # x = 98  y = 32  z = 54

sum(y = 4, x = 101)   # z get default value

sum(x = 100, z = 10, y = 10)



ororororororororororororororororororororororororororororororororororororororororororororororororororororororororororororor


def sum(x, y, z = 100):
    print("TOTAL", x + y + z)
    
n_1 = int(input("Enter Number:"))
n_2 = int(input("Enter Number:"))

sum(n_1, n_2)         # n_1 assign to x and n_2 assign to y


#########################################################################################################################
#                                                RETURN KEYWORD                                                         #              
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


                    RETURN IS A KEYWORD WHICH IS USED TO RETURN ONE OBJECT FROM A FUNCTION/METHOD.
RETURN KEYWORD MUST BE THE LAST STATEMENT IN A FUNCTION/METHOD, BECAUSE ONCE RETURN KEYWORD IS EXECUTED THE CONTROLLER
                                                WILL EXIT THE FUNCTION.


##########################################################################################################################

# FUNCTION WITHOUT ARGUMENTS AND WITH RETURN

def sum():
    a = 1010
    b = 100
    c = a + b
    return c

s = sum()
print(s)


ororororororororororororororororororororororororororororororororororororororororororororororororororororororororororororor


def sum():
    ab = int(input("Enter Number:"))
    ba = int(input("Enter Number:"))
    return ab + ba
    
s = sum()
print("SUM WITH VARIABLE =", s)
print("ADDITION WITHOUT ASSIGINMENT =", sum())



ororororororororororororororororororororororororororororororororororororororororororororororororororororororororororororor


def sample():
    return 10,20,30
    
a = sample()
print(a)
print(type(a))

