from functools import reduce
import math

c1 = [(1, 2), (3, 4), (5, 6)]
c2 = [(6, 2), (2, 4), (8, 6)]
a = [c1, c2]

cols = max(map(lambda x: x[0], reduce(lambda x, y: x + y, a))) + 1

a1 = []
for t in a:
    dest = [0] * cols
    a1.append(dest)
    for e in t:
        dest[e[0]] = e[1]

for l in a1:
    print(l)

a = [1, 2, 3]
b = [1, 1, 1]
k = math.sqrt(reduce(lambda m, n: m ** 2 + n ** 2, map(lambda x, y: x - y, a, b)))
print(k)

print([x * 2 for x in range(1, 6) if x % 2 == 0])
