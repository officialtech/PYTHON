########################################   OPERATORS  #####################################


Operators will perform operation on operands
In python, Arithmetic Operators follow BODMAS rule

B #------ Brackets
O #------ Orders
D #------- Division
M #------- Multiplication
A #------- Addition
S #------- Subtraction

In Python, we have below given operators

>>>1. Arithmetic Operators <<<
>>>2. Relational Operators <<<
>>>3. Logical Operators <<<
>>>4. Assignment Operator <<<
>>>5. ShortHand Assignment Operators <<<
>>>6. Bitwise Operators <<<
>>>7. Membership Operators <<<
>>>8. Identity Operator <<<


#**************************************** Arithmetic Operators *****************************

# Addition
>>> 100 + 200 
300
#----------------------
# Subtraction
>>> 250 - 145
105
#------------------------
# Multiplication
>>> 25 * 2
50
#-----------------------------
# Division
>>> 25 / 3
8.333333333333334
#-----------------------------------
# Modulus
>>> 10 % 3
1
#-------------------------------------------
# Floor Division
>>> 25 // 4
6
#------------------------------------------------------
# Exponential
>>> 5 ** 4
625
#--------------------------------------------------------------

#-##########################################################1######################################################################1#
TO DO                     45 + 2 - 8 * 9 + 5 / 2 + 16 - 8 * 2 / 2 + 6 + 4 / 2 - 5
#.###########################################################0#####################################################################5#




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RELATIONAL OPERATORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The relational Operators will find the relation between two(2) operands and results True and False.

>>> 10 > 10
False
#-----------------------------------^ Greater than
>>> 10 >= 10
True
#------------------------------------^ Greater than or equall to
>>> 10 < 5
False
#-------------------------------------^ Less than
>>> 10 != 5
True
#-------------------------------------^ Is Not Equall to
>>> 10 == 6
False
#-------------------------------------^ Is Equall to
>>> 808 <= 944
False
#-------------------------------------^ Less than or equall to



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ASCII <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

American Standard Code for Information Interchange
The ASCII values are 256 that are from 0 to 255.

#--------------- type this on your python interpreter ---------- ord('A')

#------------------ type this on your python interpreter -------- chr(65)




>>> "a" > "A"
True
.........................
>>> "a" > "z"
False
.........................
>>> 'A' < 'j'
True
..........................
>>> 'jb' > 'jin'
False
.........................
>>> 'jb' > 'jb'
False
.........................
>>> 'jin' >= 'jin'
True
.........................



#----------------------------------------------------------# Logical Operators #---------------------------------------------------

  logical and
  logical or
  logical not
  

  #-----------------------------------------------------# Logical and #--------------------------------------------------------
  
  logical and is working from left side to right side
  
  it first check left side condition if left side condition is True than only controller will check right side
  
  if left side condition is False, controller will skip right side condition and results False
  

age = int(input("Age: "))
print(age >= 20 and age <= 60)

# output

Age: 23
True

  
>>> 10 > 20 and 20 < 10
False

>>> 20 > 4 and 12 > 8
True
>>>   
  

>>> 10  and 10
10

>>> 20 and 10
10

>>> 10 and 20
20

>>> 23 and 2 # it always give last executed value
2

>>> 0 and 1
0

>>> 1 and 0
0

>>> 1 and 00
0

>>> 0 and 199
0  



# ------------------------------------------------------- Logical or ----------------------------------------------------------------- #

The 'logical or' will execute left to right

if left side condition is True controller never check right side and returns True

if Left side condition is Flase than only controller will check right side


>>> 11 > 12 or 21 > 11
True

>>> 12 < 12 or 11 > 11
False

>>> 1 > 0 or 40 < 10
True

>>> 808 and 944
944

>>> 944 or 0
944

>>> 0 or 0
0

>>> 1 or 45 # it's checking first condition only if it's True
1

>>> 45 or 0
45



#---------------------------------------------------- # Logical not # -------------------------------------------------------

Logical not will inverse the result

'not' operator will have only one operand that is right side to the operator


>>> not True
False

>>> not False
True

>>> not 10 > 10
True

>>> not 944 >= 944
False

>>> not "official tech"
False

>>> not 0
True

>>> not 1010
False

>>> not 'a'
False






########################################################################################################################################
                                                    Assignment Operator (=)
########################################################################################################################################


The assignment operator will work from right to left

left side must be variable only

right side must be variable, value, expression, method/function, onject

Value --- a = 10
variable --- b = a
expression --- c = a * b
function/method --- j = len('officially me')



######################################################################################################################################
                                              ShortHand assignment operators
#######################################################################################################################################
+=
-=
*=
/=
%=
**=
<<=
>>=
//=

>>> j = 944
>>> j += 808
>>> j
1752


>>> j = 944
>>> j += 808
>>> j
1752


>>> j *= 2
>>> j
3504


>>> r = 99
>>> r -= 9
>>> r
90


>>> r %= 8
>>> r
2


>>> r **= 3
>>> r
8




####################################################################################################################################
                                                  Membership Operators
####################################################################################################################################


in
not in


#---------------------------- in

It evaluates to True if it finds a value in specified sequence or False otherwise

#---------------------------- not in

It evaluates to True if it does not finds a value in the specified sequence or False otherwise


>>> lst = ['jb', 1, 3, 6, 944, 1010, 'jin', 'chao']
>>> 'jb' in lst
True

>>> 'jb' not in lst
False

>>> 4 in lst
False



my_friends = ['shadow', 'dark', 'hell', 'peak']
print('dark' in my_friends)  # True 
print('you' in my_friends)  # False
print(944 in my_friends)  # False



#------------------------------------------------- Identity Operators ------------------------------------------------

is
is not


#------------------------------------------------ is
True if the operands are identical (refer to same object)

#------------------------------------------------ is not
True if the operands are not identical (do not refer to the same object)


>>> a = 10
>>> b = 10
>>> a is b
True

>>> print(a is b)
True
 
>>> print(a is not b)
False






x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)




#----------------------------------------------- Bitwise Operator ----------------------------------------------------------


Bits stands for Binary Digit
Binary means 2 they are 0 & 1
0 - Flase
1 - True


Bitwise operators will perform operators on Bits that is 0 and 1


Bitwise operators are

Bitwise and (&)
Bitwise or (|)
Bitwise xor (^)
Bitwise leftshift (<<)
Bitwise rightshift (>>)




#--------------------------------------------------- Bitwise and (&) ----------------------------------------------------------

0 & 0 = 0
1 & 0 = 0
0 & 1 = 0
1 & 1 = 1

In bitwise and (&) the both operands must be True than only result will be True

print(10 & 20)
# 0

# ------------------------------------  512  256  128  64  32  16  8  4  2  1  -------------------------------------------------                                         
                                                          

print(89 & 90)
# 16


##################################################################################################################################

--------------------------------------------  Bitwise or (|)  ---------------------------------------------

0 | 0 = 0
0 | 1 = 1
1 | 0 = 1
1 | 1 = 1


print(23|15)
# 31

print(2|3)
# 3

print(493|16)
# 509


####################################################################################################################################
----------------------------------------------- Bitwise xor (^) --------------------------------------------------

0 ^ 0 = 0
1 ^ 0 = 1
0 ^ 1 = 1
1 ^ 1 = 1

print(10^15)
# 5


print(23 ^ 15)
# 24


######################################################################################################################################
---------------------------------------------- Bitwise leftshift (<<) -----------------------------------------------

print(10 << 3)
# 80

print(23 << 2)
# 92



#####################################################################################################################################
------------------------------------------------ Bitwise rightshift (>>) --------------------------------------------------

print(10 >> 3) # operator to be shifted is 10 and 3 is number of places to shift that is 3
# 1

print(23 >> 2)
# 5



_________________________________________________________________________________________________________________________
---------------------------------------------- NOTE ----------------------------------------------------------------------
_________________________________________________________________________________________________________________________

For Bitwise leftshift (<<) multiply(*)  with 2 , for number of shift times
means
print(23 << 3)
# 96

23 * 2 = 46 # first
46 * 2 = 92 # second






For Bitwise rightshift (>>) floor divide(//) with 2, for number of shift times

print(23 >> 2)
# 5

23 // 2 = 11
11 // 2 = 5






https://www.programiz.com/python-programming/operators
