def bruteforce(operations, offset):
    global mn, a
    if offset == len(a):
        cnt = start
        good = True
        for el in a:
            cnt += el
            if cnt > maximum or cnt < 0:
                good = False
                break
        if good:
            mn = min(mn, operations)
        return

    bruteforce(operations, offset + 1)
    prev = a[offset]
    a[offset] = 0
    bruteforce(operations + 1, offset + 1)
    a[offset] = prev


for _ in range(int(input())):
    mn = 20
    n, maximum, start = map(int, input().split())
    a = list(map(int, input().split()))

    bruteforce(0, 0)
    print(mn)