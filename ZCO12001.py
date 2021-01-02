import collections
n = int(input())
arr = list(map(int,str(input()).split(' ')))
check = collections.deque()
max_depth = 0
first_max_depth = 0
first_max_seq = 0
max_len = 0
idx = 0
for idx in range(n):
    if arr[idx] == 1:
        check.append((idx))
        if max_depth < len(check):
            max_depth += 1
            first_max_depth = idx + 1

    elif arr[idx] == 2:
        top = check.pop()
        if len(check) == 0:
            if max_len < idx-top:
                max_len = idx - top + 1
                first_max_seq = top + 1
print(max_depth, first_max_depth, max_len, first_max_seq)
