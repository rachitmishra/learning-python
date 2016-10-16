# Data Types

We don't have to declare any data types. Python does that automatically for us. So we can write


### Basics

```Python
>>>my_number = 1
>>>my_float = 1.2
>>>my_boolean = True # or False
>>>my_string = "Hello, World!"
>>>my_none = None # Yes it is a special constant with value null
```
Booleans are subclass of int and so True = 1 and False = 0

### Working with strings

```Python
my_string = "Hello!"
>>>len(my_string) # Will print length of string, can be also used on lists, sets, tuples and dicts
>>>6
```

```Python
>>>my_string.count(l) # Will print count of particular string/character in a string
>>>2
>>>my_string.count(ll)
>>>1
```

```Python
>>>my_string.index(l) # Will print position of particular string/character in a string
>>>2
```

```Python
>>>my_string.split(" ") # Will split a string at delimiter provided as argument
>>>2
```

```Python
>>>my_string.split(index1:index2) # Will print a sub-string from index1, to index2
>>>2
```

### Lists, are like arrays

```Python
my_list = [1, 2, 3]
>>>bool([]) # Will print false, an empty list is always False
```

#### Accessing list items
```Python
>>>my_list = [1, 2, 3]
>>>my_list[0] # Will print item at first position, as list index start from 0
>>>1
>>>my_list[-1] # Will print item at last position (negative index start from the end of the list)
>>>3
>>>my_list.index(1) # Will print index of of the first occurrence of item in list
>>>0
>>>my_list = [1, 2, 3]
>>>my_list.index(3, 1, 2) # Will print index of of the first occurrence of item in list, with second param being the start index and third param being end index
>>>0
```

#### Slicing a list, or creating sublists

We can slice a list by following format `my_list[start, end, step]` where start is starting index, end is end index and step is the increment value for each step
The negative values for these indexes start the list from end.
If we give no value for start or end, they default to zero
```Python
>>>my_list = [1, 2, 3, 4]
>>>my_list[1:3] # Will print sub list from start index 1 to end index 3
>>>my_list[1:3:1] # Will print sub list from index 1 to index 3 with step value as 1
>>>my_list[1:] # Will print [2, 3, 4] sub list from index 0 to end of list
>>>my_list[:1] # Will print [1] sub list from index 0 to index 1
>>>my_list[:-1] # Will print [1, 2, 3] sub list from last index(-1) to index 0
>>>my_list[-1:] # Will print [4] sub list from last index(-1) to end of list, P.S the negative index always start from the end of the list
>>>my_list[-2:] # Will print [3, 4] sub list from last index(-2) to end of list
>>>my_list[:1:1] # Will print [1] sub list from index 0 to index 1 with step 1
>>>my_list[::2] # Will print [1, 3] starting from first index to last with step value 2
>>>s = slice(1, None, 2) # Slice using the inbuilt method, this is equal to my_list[1::2]
>>>my_list[s] # Will print [2, 4], we applied slice ([1::2]) on our list 
```

#### Adding items to list
```Python
>>>my_list = [1, 2, 3]
>>>my_list + [4] # Will print the joined list (Note: this won't add [4] to my_list)
>>>[1, 2, 3, 4]
>>>my_list.append(True) # Will add True (or any param given by us of any datatype to my_list)
>>>my_list # Will print [1, 2, 3, True]
>>>my_list.extend([4]) # Will add each item in param list to my_list
>>>my_list # Will print [1, 2, 3, True, 4]
>>>my_list.insert(1, 7) # Will add 7 to my_list after position 1 (index 0)
>>>my_list # Will print [1, 7, 2, 3, True, 4]
>>>my_list.reverse() # Reverses all items in the my_list
```

#### Finding items to list
```Python
>>>my_list = [1, 2, 3]
>>>my_list.count(2) # Will give us number of items with value of 4 in my_list, it's more like counting number of 4's in the my_list
>>>1
>>>3 in my_list # Will print True or False based on if item is in my_list
>>>True
```

#### Removing items to list
```Python
>>>my_list = [1, 2, 3]
>>>my_list.pop() # Will remove an item from end of list
>>>3
>>>my_list.remove(3) # Will remove 3 from the list, if there are more than one occurrence of 3 it will remove the one found first (i.e the smallest index)
>>>3
>>>my_list.pop(0) # Will remove an item from index specified
>>>3
>>>del my_list[0] # Will remove an item from index specified
>>>my_list # Will print [1, 2]
>>>my_list.clear() # Will remove all items from my_list
>>>my_list # Will print []
```

### Tuple, is immutable list, once created it can't be changed

```Python
>>>my_tuple = (1, 2, 3)
>>>my_tuple[0] # Will print 1, works same as lists
```

Why tuples, well if our items are constants better declare them as tuples as they are fast.

Assigning multiple values using tuples
```Python
>>>('One', 'Two', 'Three') = range(3) # Will assign the values in tuple with value from range in order they are in tuple
>>>One # Will print 1
```

### Set
```Python
>>>my_set = {1, 2, 3}
>>>my_list = [4, 5, 6]
>>>my_set_from_list = set(my_list)
>>>my_empty_set = ()
```

#### Adding items to a set
```Python
>>>my_set = {1, 2, 3}
>>>my_set.add(4) # Will add 4 to my_set, Remember sets can only have unique values, it won't add 4 if it already exists in my_set
>>>my_set # Will print {1, 2, 3, 4}
>>>my_set.update({4, 5, 6, 7}) # Will add 5, 6, 7 to our set, and drop 4 as it already exists in my_set
>>>my_set # Will print {1, 2, 3, 4}
```

#### Removing items from a set
```Python
>>>my_set = {1, 2, 3, 4}
>>>my_set.discard(4) # Will remove 4 to my_set, won't raise any error if value doesn't exist
>>>my_set # Will print {1, 2, 3}
>>>my_set.remove(3) # Will remove 3 to my_set, but it raises an error when value doesn't exist in set
>>>my_set # Will print {1, 2}
>>>my_set.pop() # Will remove an item from any position in my_set
>>>my_set.clear() # Will remove all items from my_set
```

#### Set operations
```Python
>>>my_set = {1, 2, 3, 4}
>>>my_another_set = {4, 5, 6, 7}
>>>my_set.union(my_another_set) # Will print {1, 2, 3, 4, 5, 6, 7} i.e the all item of both sets
>>>my_set.intersection(my_another_set) # Will print {4} i.e the items common of both sets
>>>my_set.intersection(my_another_set) # Will print {1, 2, 3} i.e the items which are part of my_set but not in my_another_set
>>>my_set.symmetric_difference(my_another_set) # Will print {1, 2, 3, 5, 6, 7} i.e the items unique of both sets
>>>my_set.issubset(my_another_set) # Will return False as all the values in my_set are not in my_another_set
```

### Dictionaries
```Python
>>>my_dict = {"a": 1, "b": 2}
>>>my_dict = {"a": 1, "b": True} # Dictionaries can have mixed values
```
Dictionaries don't allow duplicate keys, keys are case-sensitive.

#### Modifying dictionaries
```Python
>>>my_dict = {"a": 1, "b": 2}
>>>my_dict[a] = 5
>>>my_dict # Will print {"a": 5, "b": 2}
```

## Important methods

```Python
>>>type(my_number) # Will print type of any variable
>>>int
```

```Python
>>>isinstance(my_number, int) # Will check if variable is of type
>>>True
```

```Python
>>>id(my_number) # Will return unique id of any variable (That means every variable is an object in python)
>>>4297546560
```
