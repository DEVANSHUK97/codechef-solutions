text = str(input()).strip().split('\n')
t = int(text[0])
array = [chr(97 + i) for i in range(16)]
for i in range(t):
    length = int(text[i*2 + 1])
    arr =  list(map(int, text[i*2 + 2]).strip().split(','))
    ans = ''
    for j in range(0,length,4):
        left = 0
        right  =15
        focus = arr[j:j+4]
        for f in focus:
            if f  == 0:
                right = (left+right)//2
            if f == 1:
                left = (left + right)//2
        ans.append(array[(left+right)//2])
        