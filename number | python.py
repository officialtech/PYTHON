Numbers

The interpreter acts as a simple calculator: 
you can type an expression at it and it will write the value. 
Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages (for example, Pascal or C); 
parentheses (()) can be used for grouping.


>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6




The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float. 
We will see more about numeric types later in the tutorial.


Division (/) always returns a float. 
To do floor division and get an integer result (discarding any fractional result) you can use the // operator.



>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17




With Python, it is possible to use the ** operator to calculate powers 


>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128




The equal sign (=) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:


>>> width = 20
>>> height = 5 * 9
>>> width * height
900




If a variable is not “defined” (assigned a value), trying to use it will give you an error:


>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined





There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:


>>> 4 * 3.75 - 1
14.0




In interactive mode, the last printed expression is assigned to the variable _. 
This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, 

Here Intractive mode denotes this sign or environment   >>>

for example:


>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06


This variable should be treated as read-only by the user. 
Don’t explicitly assign a value to it 
you would create an independent local variable with the same name masking the built-in variable with its magic behavior.

In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction. 
Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).





