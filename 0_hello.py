"""
int
float
string      (immutable)
list        (mutable) [Hello, 1, 2]
dictionary  {'Iowa':'DesMoines','Wisconsin':'Madison'}
tuple       (immutable) (2, 4.5, Hello)
set         (Doesn't allow dupes) {False, 3.5, Cat}
"""

"""
range
"""
print("---------------------------------")
print(range(10))
print(list(range(10)))
print(range(5, 10))
print(list(range(5, 10)))
print(list(range(5, 10, 2)))
print(list(range(10, 1, -1)))

"""
len
"""
print("---------------------------------")
print(len('hello'))

"""
string
center	astring.center(w)	    Returns a string centered in a field of size w
count	astring.count(item)	    Returns the number of occurrences of item in the string
ljust	astring.ljust(w)	    Returns a string left-justified in a field of size w
lower	astring.lower()	        Returns a string in all lowercase
rjust	astring.rjust(w)	    Returns a string right-justified in a field of size w
find	astring.find(item)	    Returns the index of the first occurrence of item
split	astring.split(schar)	Splits a string into substrings at schar
"""
print("---------------------------------")
my_name = "David"
print(my_name)
print(my_name[3])
print(my_name.upper())
print(my_name.lower())
print(my_name.center(10))
print(my_name.find('v'))
print(my_name.split('v'))

"""
set
membership	    in	                        Set membership
length	        len	                        Returns the cardinality of the set
|	            aset | otherset	            Returns a new set with all elements from both sets
&	            aset & otherset	            Returns a new set with only those elements common to both sets
-	            aset - otherset	            Returns a new set with all items from the first set not in second
<=	            aset <= otherset	        Asks whether all elements of the first set are in the second
union	        aset.union(otherset)	    Returns a new set with all elements from both sets
intersection	aset.intersection(otherset)	Returns a new set with only those elements common to both sets
difference	    aset.difference(otherset)	Returns a new set with all items from first set not in second
issubset	    aset.issubset(otherset)	    Asks whether all elements of one set are in the other
add	            aset.add(item)	            Adds item to the set
remove	        aset.remove(item)	        Removes item from the set
pop	            aset.pop()	                Removes an arbitrary element from the set
clear	        aset.clear()	            Removes all elements from the set
"""
print("---------------------------------")
my_set = {3, 6, "cat", 4.5, False}
print(my_set)
your_set = {99, 3, 100}
print(my_set.union(your_set))
print(my_set | your_set)
print(my_set.intersection(your_set))
print(my_set & your_set)
print(my_set.difference(your_set))
print(my_set - your_set)
print({3,100}.issubset(your_set))
print({3,100} <= your_set)
print(my_set.add("house"))
print({False, 4.5, 3, 6, 'house', 'cat'})
print(my_set.remove(4.5))
print(my_set)
print(my_set.pop())
print(my_set)
my_set.clear()
print(my_set)

"""
dict

[]	myDict[k]	    Returns the value associated with k, otherwise its an error
in	key in adict	Returns True if key is in the dictionary, False otherwise
del	del adict[key]	Removes the entry from the dictionary
keys	adict.keys()	Returns the keys of the dictionary in a dict_keys object
values	adict.values()	Returns the values of the dictionary in a dict_values object
items	adict.items()	Returns the key-value pairs in a dict_items object
get	adict.get(k)	Returns the value associated with k, None otherwise
get	adict.get(k,alt)	Returns the value associated with k, alt otherwise
"""

print("---------------------------------")
phone_ext = {'david': 1410, 'brad': 1137}
print(phone_ext)
print(phone_ext.keys())
print(list(phone_ext.keys()))
print(phone_ext.values())
print(list(phone_ext.values()))
print(phone_ext.items())
print(list(phone_ext.items()))
print(phone_ext.get("kent"))
print(phone_ext.get("kent", "NO ENTRY"))
