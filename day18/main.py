n = int(input())
X = []
Y = []
Z = []
for i in range(n):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

print(min(X), max(X))
print(min(Y), max(Y))
print(min(Z), max(Z))
