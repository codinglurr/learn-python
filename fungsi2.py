
def truncate(x):
    global val
    if x % val != 0:
        val = val - (val % x)
    print(val)


val = int(input())
den = int(input())

truncate(val)
truncate(den)
print(val, den)
