import sys

a=1

while a != 0:
    rl = lambda: sys.stdin.readline()
    n = int(rl())
    if 1<= n <=50:
        a = 0



A = []

for i in range(n):
  A.append(raw_input())


i=0

for i in range(n):
  print "Hello, %s!" % A[i]#[:5]