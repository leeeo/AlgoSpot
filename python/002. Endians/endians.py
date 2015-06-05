import sys

def covn_endian(x):
    y=x
    x = ((x>>8) | (x & 0x000000ff) << 24) & 0xff00ff00
    y = ((y<<8) | (y & 0xff000000) >> 24) & 0x00ff00ff
    return (x | y)

a=1

while a != 0:
    rl = lambda: sys.stdin.readline()
    n = int(rl())
    if 1<= n <=10000:
        a = 0

A = []

for i in range(n):
  A.append(int(raw_input()))

i=0

for i in range(n):
    print covn_endian(A[i])