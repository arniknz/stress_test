import sys
import random

sys.stdout = open("testcases.txt", "w")


class RandomGenerator():
    def __init__(self):
        pass


    def integer(self, s, e):
        res = random.randint(s, e)
        return res
    

    def array(self, n, s, e):
        a = [0] *  n
        for i, e in enumerate(a):
            a[i] = self.integer(s, e)
        return a
    

class ListOperation():
    def __init__(self):
        pass


    def print_space(self, a):
        for c in a:
            print(c, end=" ")
        print()


    def print_csv(self, a):
        for c in a:
            print(c, end=", ")
        print()


r = RandomGenerator()
t = 10
m = 10
print(t)
for _ in range(t):
    n = r.integer(1, m)
    s = r.integer(0, m)
    k = r.integer(0, m)

    a = r.array(n, -1, 1)
    print(n, s, k)
    print(*a)