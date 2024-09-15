"""
https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
"""


def find_flavors(t, m, n, x):
    # t = int(input().strip())
    for a0 in range(t):
        # m = int(input().strip())
        # n = int(input().strip())
        a = list(map(int, x.strip().split(' ')))

        m = n // 2
        l = 0
        u = n - 1
        for i in range(n):
            if a[i] < m:
                f1 = a[i]
                f2 = a[i]


if __name__ == '__main__':
    trips = 2
    money = 4
    total_flavors = 5
    flavors = "1 4 5 3 2"
    find_flavors(trips, money, total_flavors, flavors)
