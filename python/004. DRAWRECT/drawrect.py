import sys

x = []
y = []
threePoint = 3

a = 1
while a != 0:
    rl = lambda: sys.stdin.readline()
    n = int(rl())
    if 1 <= n <= 1000:
        a = 0

for i in range(n) * threePoint:
    tempX, tempY = map(int, raw_input().split())
    x.append(tempX)
    y.append(tempY)

for i in range(0, n):
    if x[i] == x[i+1]:
        del (x[i])
        del (x[i])
    elif x[i] == x[i+2]:
        del (x[i])
        del (x[i+1])
    elif x[i+1] == x[i+2]:
        del (x[i+1])
        del (x[i+1])

for i in range(0, n):
    if y[i] == y[i+1]:
        del (y[i])
        del (y[i])
    elif y[i] == y[i+2]:
        del (y[i])
        del (y[i+1])
    elif y[i+1] == y[i+2]:
        del (y[i+1])
        del (y[i+1])

for i in range(0, n):
    print x[i], y[i]

