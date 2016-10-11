## Comprehensions

One may define a function as

```
def myFunction(a, b):
    print(a + b)
```

Then call it simply as

`myFunction(1,2)`

```
def myFunction(a, b):
    return a + b #Returning a value from function

sum = myFunction(1,2)

print(sum)

>>> 3
```

#### `fargs, *args, **kargs`

fargs or formal arguments are the simple arguments we supply to our methods

Interesting part is `*args`

If we aren't not sure about of number of arguments to a method we can define our method as

```
def myFunction(*args):
    for a in args:
        print(a)

myFunction(1, 2, 3, 4)

>>> 1 2 3 4
```

`**kargs` or key-value arguments can also be defined as

```
def myFunction(**args):
    for a, b in args.item(): #a is the key and b is the value
        print(a, b)

myFunction(1="a", 2="b")

>>> 1 2 3 4
```

## Lambda methods
Lambda methods are one line based methods used for operations limited to one line

They are define as `lambda x: x**2`

```
  my_array = [1, 2, 3]
  square_array = lambda x: x**2
  print(square_array)
```

## Interesting Methods

`map()` It is used to map the values of a list to a new result.

```
    my_array = [1, 2, 3]
    list(map(lambda x: x+1, my_array))
```

`filter()` It is used to filter list elements based on a condition

```
    my_array = [1, 2, 3]
    list(filter(lambda x: x/2, my_array))
```

`reduce()` It is used to get a single operation result from all elements ex. sum of list

```
    my_array = [1, 2, 3]
    list(reduce(lambda x, y: x/2, my_array))
```
