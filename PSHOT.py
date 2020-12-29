t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = []
    arr2 = []
    arr = list(map(int,list(str(input()))))
    count1 = 0
    count2 = 0
    remaining1 = n
    remaining2 = n
    for idx in range(0,2*n,1):
        result = arr[idx]
        if idx%2 == 0:  
            remaining1 -= 1
            if result == 1:
                count1 += 1
            arr1.append(result)
        else:
            remaining2 -= 1
            if result == 1:
                count2 += 1
            arr2.append(result)
            
        if count2 > count1 + remaining1 or count1 > count2 + remaining2:
            break
            
    print(idx+1)