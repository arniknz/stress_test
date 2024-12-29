def check_validity(s, k, ai):
    if ai == 1:
        return s + ai <= k
    elif ai == -1:
        return s + ai >= 0
    

for _ in range(int(input())):
    n, k, s = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if check_validity(s, k, a[i]) or a[i] == 0:
            s += a[i]
        else:
            cnt += 1

    print(cnt)