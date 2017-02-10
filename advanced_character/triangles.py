def triangles():
    a = [1]
    while(1):
        yield a
        a.append(0)
        a = [a[index - 1] + a[index] for(index, value) in enumerate(a)]
# def triangles():
#     L = [1]
#     while(1):
#         yield L
#         L.append(0)
#         L = [L[i-1] + L[i] for i in range(len(L))]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
