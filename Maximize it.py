# Maximize it
from itertools import product
K, M = map(int, input().split())
L = []
for _ in range(K):
    L.append(list(map(int, input().split()))[1:])
    
print(max(sum(x ** 2 for x in val) % M for val in product(*L)))
