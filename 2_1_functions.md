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
Methods can have default argument values

```
def my_function(a, b = 2):
    return a + b #Returning a value from function

sum = my_function(1) #Oh! We just one argument, the method will use the default value now

print(sum)

>>> 3
```

We can also pass functions as *arguments*

```
def my_function(a, b):
    return a+b

def my_function_with_function_args(a, b, my_function_arg):
    my_function_arg(a, b)

print(my_function_with_function_args(1, 2, my_function)) # Remember not to pass function as my_function(), that will instead call the function
```

We can define function inside functions as well as return functions

```
def my_function():

    def my_inner_function():
        print("I am in my_function")

    return my_inner_function

print(my_function()())
```

```
def my_function():
    def my_inner_function():
        print("I am in my_function")
    my_inner_function()

my_function()

```

Using global keyword we can set global variable to be used in future


```
def my_function():
    def my_inner_function():
        global n
        n = 1
        print("I am in my_function")
    my_inner_function()

my_function()
print(n)

```
Although this is not allowed and we should use lists and dicts to return multiple values

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
def my_decorator_function(function_to_be_decorated):
    def my_function():
        print("Starting decor")
        function_to_be_decorated(1, 2)
        print("Ending decor")
    return my_function

def sum(a, b):
    print(a+b)

decor = my_decorator_function(sum)

decor()
```

This can also be written as

```
def my_decorator_function(function_to_be_decorated):
    def my_function():
        print("Starting decor")
        function_to_be_decorated(1, 2)
        print("Ending decor")
    return my_function

@my_decorator_function #Remember this has to be defined
def sum(a, b):
    print(a+b)

sum()
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
