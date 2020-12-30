t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,str(input()).split(' ')))
    ans = 0
    idx = 0
    prev_min = arr[0]
    for idx in range(n):
        if arr[idx] < prev_min:
            prev_min = arr[idx]
        ans += prev_min
    print(ans)