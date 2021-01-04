import heapq
t = int(str(input()).strip())
for _ in range(t):
    n,m = (map(int,str(input()).strip().split(' ')))
    a = list(map(int, str(input()).strip().split(' ')))
    b = list(map(lambda x: -1*int(x), str(input()).strip().split(' ')))
    heapq.heapify(a)
    heapq.heapify(b)
    a_sum = sum(a)
    b_sum = -1*sum(b)
    steps = 0
    for _ in range(min(n,m)):
        if a_sum > b_sum:
            break
        a_min = heapq.heappop(a)
        b_max = -1*heapq.heappop(b)
        a_sum = a_sum + b_max - a_min
        b_sum = b_sum - b_max + a_min
        heapq.heappush(a, b_max)
        heapq.heappush(b, -1*a_min)
        steps += 1
    if a_sum <= b_sum:
        steps = -1
    print(steps)
