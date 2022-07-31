Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> todos = open('todos.txt', 'a')
>>> open
<built-in function open>
>>> print('Put out the trash.', file=todos)
>>> print('Feed the cat', file=todos)
>>> print('Prepare tax return.', file=todos)
>>> tods.close()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tods.close()
NameError: name 'tods' is not defined
>>> todos.close()
>>> tasks = open('todos.txt')
>>> open
<built-in function open>
>>> for chore in tasks:
	print(chore)

	
Put out the trash.

Feed the cat

Prepare tax return.

>>> tasks.close()
>>> 