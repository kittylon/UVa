# suppose a function called main() and
# all the operations are performed


def main():
    # for read and iterate all the lines
    test_amount = int(input())
    for test in range(test_amount):
        n, m = map(int, input().split(" "))
        # print result
        print(get_sonars_amount(n, m))


def get_sonars_amount(n, m):
    # We do not need the border to be covered
    n = n - 2
    m = m - 2

    while n % 3 != 0:
        n += 1

    while m % 3 != 0:
        m += 1

    n_slot = n / 3
    m_slot = m / 3

    return int(n_slot * m_slot)


if __name__ == "__main__":
    main()
