# suppose a function called main() and
# all the operations are performed
from itertools import islice
from sys import stdin


def main():
    for _ in stdin:
        h_len = islice(stdin, None, None, 2)
        highway = next(h_len)

        if 'Z' in highway:
            print(0)
        else:
            is_sort_asc(highway)


def is_sort_asc(highway):
    r_pos = 0
    d_pos = 0
    dis = []
    for pos, item in enumerate(highway):
        if item == 'R':
            r_pos = pos
            if d_pos != 0:
                dis.append(abs(r_pos - d_pos))
        elif item == 'D':
            d_pos = pos
            if r_pos != 0:
                dis.append(abs(r_pos - d_pos))
    if len(dis):
        print(min(dis))
    else:
        print(1)


if __name__ == "__main__":
    main()
