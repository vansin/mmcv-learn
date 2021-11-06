import bisect

a = bisect.bisect_left([5,7,7,8,8,10],8)
b = bisect.bisect_right([5,7,7,8,8,10],8)

print(a, b)