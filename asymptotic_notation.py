s = 0
for x in seq:
    s += x

squares = [x**2 for in seq]

s = 0
for x in seq:
    for y in seq:
        s += x*y

s = 0
for x in seq:
    for y in seq:
        s += x*y
        for z in seq:
            for w in seq:
                s += x-w

s = 0
for x in seq1:
    for y in seq2:
        s += x*y

seq1 = [[0, 1], [2], [3, 4, 5]]
s = 0
for seq2 in seq1:
    for x in seq2:
        s += x

s = 0
n = len(seq)
for i in range(n-1)
    for j in range(i+1, n)
    s += seq[i] * seq[j]
