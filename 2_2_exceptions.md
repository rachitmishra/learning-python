## Exception

Using try, Exception we can handle possible errors in our code

```
try:
    n = 1/0
except ZeroDivisionError as e:
    print("Error n/0")

try:
    n = 1/0
except (ZeroDivisionError, Exception) as e:
    print("Error n/0")
    raise e #Raises system exception

try:
    n = 1/0
except ZeroDivisionError as e:
    print("Error n/0")
except Exception:
    print("Error")
```

We can use finally to perform anything after try-except is finished

```
try:
    n = 1/0
except (ZeroDivisionError, Exception) as e:
    print("Error n/0")
finally:
    print("Finally")
```

We can also use try-else, else runs only if no exceptions occur

```
try:
    n = 1/0
except (ZeroDivisionError, Exception) as e:
    print("Error n/0")
    raise e #Raises system exception
else:
    print("Ok what, else!")
finally:
    print("Finally")
