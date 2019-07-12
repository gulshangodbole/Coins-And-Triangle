t = int(input())
for i in range(t):
    n = int(input())
    i = 1
    j = 0
    while True:
        j += i
        if j > n:
            break
        i += 1
    print(i - 1)
