#Basic programming kattis
N, t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
    print(7)
elif t == 2:
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else: 
        print("Smaller")
elif t == 3:
    Amarked = sorted(A[:3])
    print(Amarked[1])
elif t == 4:
    print(sum(A))
elif t == 5:
    sum = 0
    for i in A:
        if i % 2 == 0:
            sum += i
    print(sum)
elif t == 6:
    Amarked = map(lambda x: chr(x % 26 + 97), A) 
    print("".join(Amarked))
elif t == 7:
    i = 0
    visited = set()
    while True:
        i = A[i]
        if i > N-1 or i < 0:
            print("Out")
            break
        elif i == N-1:
            print("Done")
            break
        elif i in visited:
            print("Cyclic")
            break
        else:
            visited.add(i)