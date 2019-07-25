# suppose a function called main() and
# all the operations are performed
from sys import stdin


def main():
    for line in stdin:
        h_len = int(line.strip())
        if h_len:
            highway = input()

            if 'Z' in highway:
                print(0)
            else:
                is_sort_asc(highway)


def is_sort_asc(highway):
    r_pos = 0
    r_flag = 0
    d_pos = 0
    d_flag = 0
    dis = []
    for pos, item in enumerate(highway):
        if item == 'R':
            r_pos = pos
            r_flag = 1
            if d_flag != 0:
                dis.append(abs(r_pos - d_pos))
        elif item == 'D':
            d_pos = pos
            d_flag = 1
            if r_flag != 0:
                dis.append(abs(r_pos - d_pos))
    if len(dis):
        print(min(dis))
    else:
        print(1)


if __name__ == "__main__":
    main()
