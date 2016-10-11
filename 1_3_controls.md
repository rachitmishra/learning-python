## Control statements

#### if, elif, else

```
n = int(input())

if n == 1:
    print("Equal")
elif n > 1:
    print("Greater")
else:
    print("Smaller")

>>> 1
>>> Equal
```

```
s = "Hello"
c = "H"
if c in s:
    print("Yes")
else:
    print("No")
>>> Yes
```

#### for

```
n = 5
for k in range(n):
    print(k)
>>> 0 1 2 3 4
```
```
l = [1, 2, 3, 4]
for n in l:
    print(n)
>>>1 2 3 4
```

#### for-else

The else part executes only if the loop completed fine, i.e without any `break`
```
my_array  = [1, 2, 3]
for k in my_array:
    print(k)
else:
    print("oh! else!")
```
