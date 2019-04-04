def test(a):
    b = int(a)
    return b+1
a = [1,2,3]
b = map(test,a)
for a in b:
    print(a)