## Data Types

We don't have to declare any data types. Python does that automatically for us. So we can write

```Python
my_number = 1
my_float = 1.2
my_boolean = True #or False
my_string = "Hello, World!"
None #Yes it is a datatype with value null
```

Lists
```Python
my_list = [1, 2, 3]
```

Set
```Python
my_set = {1, 2, 3}
```

Dictionaries
```Python
my_dict = {"a": 1, "b": 2}
```

### Important methods

```Python
>>>type(my_number) #Prints type of any variable
>>>int
```

```Python
>>>isinstance(my_number, int) #Check if variable is of type
>>>True
```

```Python
>>>type(my_number) #Prints attributes of a variable
>>>['__abs__',
 '__add__',
 '__and__',
 '__bool__',
 '__ceil__',

```

```Python
>>>id(my_number) #Return unique id of any variable (That means every variable is an object in python)
>>>4297546560
```

```Python
>>>import inspect #import module also let's us inspect a python variable
>>>inspect.getmembers(my_number) #Return unique id of any variable (That means every variable is an object in python)
>>>4297546560
```


## String operations


```Python
my_string = "Hello!"
>>>len(my_string) #Returns length of string
>>>6
```

```Python
>>>my_string.count(l) #Returns count of particular string/character in a string
>>>2
>>>my_string.count(ll)
>>>1
```

```Python
>>>my_string.index(l) #Returns position of particular string/character in a string
>>>2
```

```Python
>>>my_string.split(" ") #Split a string at any delimiter
>>>2
```

```Python
>>>my_string.split(index1:index2) #Returns a sub-string from index1, to index2
>>>2
```

## List operations
