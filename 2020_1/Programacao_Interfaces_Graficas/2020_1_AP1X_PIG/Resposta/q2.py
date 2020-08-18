def g(a,b):
    if len(a)<b:
        return[a]
    return[a[:b]]+g(a[b:len(a)],b)

print(g(list(range(10)),3))
print(g("*" * 10,4))