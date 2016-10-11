## Functions

Function are the basic building blocks of code which do a specific operation on a set of arguments.
They can be defined

```
def my_function(a, b):
    print(a + b)
```

Then call it simply as

`my_function(1,2)`

```
def my_function(a, b):
    return a + b #Returning a value from function

sum = my_function(1,2)

print(sum)

>>> 3
```

We can also functions as *arguments*

```
def my_function(a, b):
    return a+b

def my_function_with_function_args(a, b, my_function_arg):
    my_function_arg(a, b)

print(my_function_with_function_args(1, 2, my_function)) # Remember not to pass function as my_function(), that will instead call the function
```

## `fargs, *args, **kargs`

fargs or formal arguments are the simple arguments we supply to our methods

Interesting part is `*args`

If we aren't not sure about of number of arguments to a method we can define our method as

```
def my_function(*args):
    for a in args:
        print(a)

my_function(1, 2, 3, 4)

>>> 1 2 3 4
```

`**kargs` or key-value arguments can also be defined as

```
def my_function(**args):
    for a, b in args.item(): #a is the key and b is the value
        print(a, b)

my_function(1="a", 2="b")

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

## Modules and `import`

You may create a set of methods in your `utils.py`, in easy words we may call it our Utils module

```
from utils import my_function #import a single method from utils

#or

import utils #import all methods of the module
```

## Generators
Every time you call a `generator` function with it will store it's result of the operation performed on the params using `yield` keyword. Using a loop we can get the results. Point to note, we can loop only once

```
def my_function():
    for i in range(5):
        yield i

>>>my_function()

for a in my_function():
    print(a)

>>>0 1 2 3 4
```

## Decoraters
Suppose you want to print something before and after a some method call. Decoraters to the rescue.
Decoraters allow us wrapping our method result inside other method calls


```
def my_decorator_function(function_to_be_decorated)
```

## Important other methods

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
    from functools import reduce
    my_array = [1, 2, 3]
    reduce(lambda x, y: x/2, my_array)
```

`next()` Return next value in the iterators(generators, or any object which has next method)

```
    my_array = [1, 2, 3]
    print(my_array.next())
```
