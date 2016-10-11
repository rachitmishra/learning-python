## Data Types

We don't have to declare any data types. Python does that automatically for us. So we can write

```
my_number = 1
my_float = 1.2
my_boolean = True #or False
my_string = "Hello, World!"
my_list = [1, 2, 3]
my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}
```
### Interesting methods

```
>>>type(my_number) #Prints type of any variable
>>>int
```

```
>>>isinstance(my_number, int) #Check if variable is of type
>>>True
```

```
>>>type(my_number) #Prints attributes of a variable
>>>['__abs__',
 '__add__',
 '__and__',
 '__bool__',
 '__ceil__',

```

## String operations


```
my_string = "Hello!"
>>>len(my_string) #Returns length of string
>>>6
```

```
>>>my_string.count(l) #Returns count of particular string/character in a string
>>>2
>>>my_string.count(ll)
>>>1
```

```
>>>my_string.index(l) #Returns position of particular string/character in a string
>>>2
```

```
>>>my_string.split(" ") #Split a string at any delimiter
>>>2
```

```
>>>my_string.split(index1:index2) #Returns a sub-string from index1, to index2
>>>2
```

## Operators

```
+  (Plus),
-  (Minus),
*  (Multiply),
** (Power of),
/  (Float division), #Returns float division
// (Integer Division), #Return integer division(except if numerator or denominator is float)
%  (Modulus)
```

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
n = 10
for n in range(10):
    print(n)
```
```
>>>l = [1, 2, 3, 4]
>>>for n in l:
    print(n)
>>>1 2 3 4
```
