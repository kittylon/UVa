# suppose a function called main() and
# all the operations are performed


def main():
    groups = int(input())

    print('Lumberjacks:')

    for _ in range(groups):
        group = list(map(int,input().split()))

        if is_sort_asc(group) or is_sort_desc(group):
            print('Ordered')
        else:
            print('Unordered')


def is_sort_asc(lumbers):
    asc_lumbers = lumbers.copy()
    asc_lumbers.sort()

    if asc_lumbers == lumbers:
        return True
    else:
        return False


def is_sort_desc(lumbers):
    desc_lumbers = lumbers.copy()
    desc_lumbers.sort(reverse=True)

    if desc_lumbers == lumbers:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
