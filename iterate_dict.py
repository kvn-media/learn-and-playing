Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> found = {}
>>> fount
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    fount
NameError: name 'fount' is not defined
>>> found
{}
>>> found['a'] = 0
>>> found['e'] = 0
>>> found['i'] = 0
>>> found['o'] = 0
>>> found['u'] = 0
>>> found
{'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
>>> found['e'] = found['e'] + 1
>>> found
{'a': 0, 'e': 1, 'i': 0, 'o': 0, 'u': 0}
>>> found['e'] += 1
>>> found
{'a': 0, 'e': 2, 'i': 0, 'o': 0, 'u': 0}
>>> for kv in found:
	print(kv)

	
a
e
i
o
u
>>> for k in found:
	print(k, 'was found', found[k], 'time(s).')

	
a was found 0 time(s).
e was found 2 time(s).
i was found 0 time(s).
o was found 0 time(s).
u was found 0 time(s).
>>> 