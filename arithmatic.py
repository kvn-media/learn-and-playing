# Integers in Python (+ plus, - subtract, * multiply, / divide)
2 + 3 # 5

3 - 2 # 1

2 * 3 # 6

3 / 2 # 1.5

# In a terminal session, Python simply returns the result of the operation. Python uses two multiplication symbols to represent exponents:
3 ** 2 # 9

3 ** 3 # 27

10 ** 6 # 1000000

# Python supports the order of operations too, so you can use multiple operations in one expression. You can also use parentheses to modify the order of operations so Python can evaluate your expression in the order you specify. For example:
2 + 3*4 # 14

(2 + 3) * 4 # 20

# Floats
# Python calls any number with a decimal point a float. This term is used in most programming languages, and it refers to the fact that a decimal point can appear at any position in a number. Every programming language must be carefully designed to properly manage decimal numbers so numbers behave appropriately no matter where the decimal point appears.

# you can use decimals without worrying about how they behave. Simply enter the numbers you want to use, and Python will most likely do what you expect:
0.1 + 0.1 # 0.2
0.2 + 0.2 # 0.4
2 * 0.1 # 0.2
2 * 0.2 # 0.4

# But be aware that you can sometimes get an arbitrary number of decimal places in your answer:

0.2 + 0.1 # 0.30000000000000004
3 * 0.1 # 0.30000000000000004

# Integers and floats
4/2 # 2.0

# If you mix an integer and a float in any other operation, you'll get float as well
1 + 2.0 # 3.0
2 * 3.0 # 6.0
3.0 * 2 # 9.0

# Python defaults to a float in any operation that uses a float, even if the output is a whole number

# Underscore in number
universe_age = 14_000_000_000
print(universe_age)
# When you print a number that was defined using underscore, Python prints only the digits

# Python ignores the underscore when storing these kinds of values. Even if you don't group the digits in three, the value will still be unaffected. To Python, 1000 is the same as 1_000, which is the same 10_00. This feature works for integers and floats, but it's only available in Python 3.6 and later

# Multiple Assignment
x, y, z = 0, 0, 0
# You need to separate the variable names with commas, and do the same with the values, and   Python will assign each value to its respectively positioned variable. As long as the       number of values matches the number of variables, Python will match them up correctly.

# Constant
# A constant is like a variable whose value stays the same throughout the life of a program. Python doesn’t have built in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed:

MAX_CONNECTIONS = 5000
# When you want to treat a variable as a constant in your code, make the name of the variable all capital letters.