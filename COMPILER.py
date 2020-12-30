import collections
t = int(input())
for _ in range(t):
    ans = 0
    arr = list(str(input()))
    check = collections.deque()
    count = 0
    for i in arr:
        if i == '<':
            check.append('<')
        else:
            if len(check) == 0:
                break
            check.pop()
            count += 2
            if len(check) == 0:
                ans += count
                count = 0                
    print(ans)
    