from io import StringIO
print("one:")
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue())
print("two:")
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
print("three:")
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())