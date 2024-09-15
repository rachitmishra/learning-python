# n_input = input("Please enter your name:")
# a_input = input("Please enter your age:")
# print(n_input)
# print("Hello", "World", sep="***")
# print(n_input, "is", a_input, "years old.")
# print("%s is %d years old." % (n_input, int(a_input)))

counter = 0
while counter <= 5:
    print("Hello, world")
    counter += 1

counter = 0
done = False
while counter <= 10 and not done:
    print("Hello, world")
    counter += 1

for item in [1, 3, 6, 2, 5]:
    print(item)

for item in range(5):
    print(item ** 2)

score = 10
if score >= 90:
    print('A')
else:
    if score >= 80:
        print('B')
    else:
        if score >= 70:
            print('C')
        else:
            if score >= 60:
                print('D')
            else:
                print('F')

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

"""
list comprehension
"""
sqlist = [x * x for x in range(1, 11)]
print(sqlist)
sqlist = [x * x for x in range(1, 11) if x % 2 == 0]
print(sqlist)
