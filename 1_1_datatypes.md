## Data Types

We don't have to declare any data types. Python does that automatically for us. So we can write

```
my_number = 1
my_float = 1.2
my_boolean = True #or False
my_string = "Hello, World!"
None #Yes it is a datatype with value null
```

Lists
```
my_list = [1, 2, 3]
```

Set
```
my_set = {1, 2, 3}
```

Dictionaries
```
my_dict = {"a": 1, "b": 2}
```

### Important methods

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
