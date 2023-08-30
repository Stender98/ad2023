T = int(input())

for _ in range(T):
    n = int(input())
    cities = []
    for _ in range(n):
        cities.add(input().strip())
    print(len(set(cities)))