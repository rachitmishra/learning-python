class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print("%d/%d" % (self.num, self.den))

    # Overriding a method
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den

        return Fraction(new_num, new_den)

    def gcf(self, fraction):
        return self.get_gcf(fraction.num, fraction.den)

    def get_gcf(self, num1, num2):
        if num1 < num2:
            temp = num1
            num1 = num2
            num2 = temp

        if num2 == 0:
            return num1

        if num1 == 0:
            return num2

        rem = num1 % num2
        if rem == 0:
            return num2
        else:
            return self.get_gcf(num2, rem)

    def reduce(self, fraction):
        return str(int(fraction.num / self.gcf(fraction))) + "/" + str(int(fraction.den / self.gcf(fraction)))


f1 = Fraction(3, 8)
f2 = Fraction(7, 10)
print(f1)
print(f1 + f2)
print(f1.reduce(f1 + f2))
