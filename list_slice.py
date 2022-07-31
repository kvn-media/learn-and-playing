Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: D:/Enigma-Course/Vengeance_Playgroud/Python/vowels.py ========
i
i
a
>>> found = []
>>> len(found)
0
>>> found.append('a')
>>> len(found)
1
>>> found
['a']
>>> found.append('e')
>>> found.append('i')
>>> found.append('o')
>>> len(found)
4
>>> found
['a', 'e', 'i', 'o']
>>> 
======== RESTART: D:/Enigma-Course/Vengeance_Playgroud/Python/vowels2.py =======
Provide a word to search for vowels:Milliways
i
a
>>> Hitch-hiker
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Hitch-hiker
NameError: name 'Hitch' is not defined
>>> 
======== RESTART: D:/Enigma-Course/Vengeance_Playgroud/Python/vowels2.py =======
Provide a word to search for vowels:Milliways
i
a
>>> 
======== RESTART: D:/Enigma-Course/Vengeance_Playgroud/Python/vowels2.py =======
Provide a word to search for vowels:Hitch-hiker
i
e
>>> 
======== RESTART: D:/Enigma-Course/Vengeance_Playgroud/Python/vowels2.py =======
Provide a word to search for vowels:Galaxy
a
>>> 
======== RESTART: D:/Enigma-Course/Vengeance_Playgroud/Python/vowels2.py =======
Provide a word to search for vowels:Sky
>>> nums = [1,2,3,4]
>>> nums
[1, 2, 3, 4]
>>> nums.remove(3)
>>> nums
[1, 2, 4]
>>> nums.pop()
4
>>> nums
[1, 2]
>>> nums.pop()
2
>>> nums
[1]
>>> nums.extend([2,3,4])
>>> nums
[1, 2, 3, 4]
>>> nums.pop(0)
1
>>> nums
[2, 3, 4]
>>> nums.extend([])
>>> nums.insert(0,1)
>>> nums
[1, 2, 3, 4]
>>> nums.insert(2, "two-and-a-half")
>>> nums
[1, 2, 'two-and-a-half', 3, 4]
>>> 
========= RESTART: D:/Enigma-Course/Vengeance_Playgroud/Python/panic.py ========
Don't panic!
['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
['o', 'n', ' ', 't', 'a', 'p']
on tap
>>> 
>>> 
>>> 
>>> 
>>> 
>>> plist
['o', 'n', ' ', 't', 'a', 'p']
>>> phrase
"Don't panic!"
>>> plist
['o', 'n', ' ', 't', 'a', 'p']
>>> first = [1,2,3,4,5]
>>> first
[1, 2, 3, 4, 5]
>>> second = first
>>> second
[1, 2, 3, 4, 5]
>>> second.append(6)
>>> second
[1, 2, 3, 4, 5, 6]
>>> first
[1, 2, 3, 4, 5, 6]
>>> third = second.copy()
>>> third
[1, 2, 3, 4, 5, 6]
>>> third.append(7)
>>> third
[1, 2, 3, 4, 5, 6, 7]
>>> second
[1, 2, 3, 4, 5, 6]
>>> 
================================ RESTART: Shell ================================
>>> saying = "Don't panic!"
>>> letters = list(saying)
>>> letters
['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
>>> letters[0]
'D'
>>> letters[3]
"'"
>>> letters[6]
'p'
>>> letters[-1]
'!'
>>> letters[-3]
'i'
>>> letters[-6]
'p'
>>> first = letters[0]
>>> last = letters[-1]
>>> first
'D'
>>> last
'!'
>>> letters
['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
>>> letters[0:10:3]
['D', "'", 'p', 'i']
>>> letters[3:]
["'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
>>> letters[:10]
['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i']
>>> letters[::2]
['D', 'n', 't', 'p', 'n', 'c']
>>> 