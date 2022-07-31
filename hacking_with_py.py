Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello, world!")
Hello, world!
The Spanish Inquisition
SyntaxError: invalid syntax
SPAM with SPAM, SPAM, Eggs, and SPAM: First, take some SPAM.
SyntaxError: invalid syntax
2 + 2
4
53672 + 235253
288925
1 / 2
0.5
1 / 1
1.0
1 // 2
0
1 // 1
1
5.0 // 2.4
2.0
from __future__ import division
1 % 2
1
10 // 3
3
10 % 3
1
9 // 3
3
9 % 3
0
2.75 % 0.5
0.25
10 % 3
1
10 % -3
-2
-10 % -3
-1
10 // 3
3
10 // -3
-4
-10 // 3
-4
-10 // -3
3
2 ** 3
8
-3 ** 2
-9
(-3) ** 2
9
0xAF
175
010
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
o1o
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    o1o
NameError: name 'o1o' is not defined
010
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
o10
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    o10
NameError: name 'o10' is not defined
0lo
SyntaxError: invalid decimal literal
olo
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    olo
NameError: name 'olo' is not defined
0b1011010010
722
010
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
x = 3
x * 2
6
2 * 2
4
print(2 * 2)
4
x = 3
input("The meaning of life: ")
The meaning of life: 42
'42'
x = input("x: ")
x: 34
y = input("y: ")
y: 42
print(int(x) * int(y))
1428
if 1 == 2: print('One equals two')

if 1 == 1: print('One equals one')

One equals one
if time % 60 == 0: print('On the hour!')

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    if time % 60 == 0: print('On the hour!')
NameError: name 'time' is not defined
2 ** 3
8
pow(2, 3)
8
10 + pow(2, 3 * 5) / 3.0
10932.666666666666
abs(-10)
10
2 // 3
0
round(2 / 3)
1
import math
math.floor(32.9)
32
int(32.9)
32
math.ceil(32.3)
33
math.ceil(32)
32
from math import sqrt
sqrt(9)
3.0
sqrt(-1)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    sqrt(-1)
ValueError: math domain error
sqrt(-1)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    sqrt(-1)
ValueError: math domain error
import cmath
cmath.sqrt(-1)
1j
(1 + 3j) * (9 + 4j)
(-3+31j)
