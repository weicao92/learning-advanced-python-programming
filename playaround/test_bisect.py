import bisect

l  = [1,2,4]

r = l.insert(bisect.bisect_left(l, 3), 3)
print(l)