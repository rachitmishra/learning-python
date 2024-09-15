"""
Lists


indexing	    [ ]	    Access an element of a sequence
concatenation	+	    Combine sequences together
repetition	    *	    Concatenate a repeated number of times
membership	    in	    Ask whether an item is in a sequence
length	        len	    Ask the number of items in the sequence
slicing	        [ : ]	Extract a part of a sequence

append	    alist.append(item)	    Adds a new item to the end of a list
insert	    alist.insert(i,item)	Inserts an item at the ith position in a list
pop	        alist.pop()	            Removes and returns the last item in a list
pop	        alist.pop(i)	        Removes and returns the ith item in a list
sort	    alist.sort()	        Modifies a list to be sorted
reverse	    alist.reverse()	        Modifies a list to be in reverse order
del	        del alist[i]	        Deletes the item in the ith position
index	    alist.index(item)	    Returns the index of the first occurrence of item
count	    alist.count(item)	    Returns the number of occurrences of item
remove	    alist.remove(item)	    Removes the first occurrence of item

"""
import timeit

def test1():
    l = []
    for i in range(1000):
        l += [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")
x = list(range(2000000))
popzero.timeit(number=1000)
x = list(range(2000000))
popend.timeit(number=1000)

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")
print("pop(0)   pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz,pt))

"""
index []	        O(1)
index assignment	O(1)
append	            O(1)
pop()	            O(1)
pop(i)	            O(n)
insert(i,item)	    O(n)
del operator	    O(n)
iteration	        O(n)
contains (in)	    O(n)
get slice [x:y]	    O(k)
del slice	        O(n)
set slice	        O(n+k)
reverse	            O(n)
concatenate	        O(k)
sort	            O(n log n)
multiply	        O(nk)
"""
