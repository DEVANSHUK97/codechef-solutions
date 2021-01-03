t = int(input())
for _ in range(t):
    n,k,d = tuple(map(int,str(input()).strip().split(' ')))
    arr = sum(list(map(int,str(input()).strip().split(' '))))
    print(min(arr//k, d))
    