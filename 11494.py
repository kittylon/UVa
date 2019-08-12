# suppose a function called main() and
# all the operations are performed
from sys import stdin


def main():
    for line in stdin:
        x1, y1, x2, y2 = map(int, line.strip().split())

        if x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
            n_moves = get_n_moves(x1, y1, x2, y2)
            print(n_moves)


def get_n_moves(x1, y1, x2, y2):
    # Same point
    if x1 == x2 and y1 == y2:
        return 0

    # Same row or column
    elif x1 == x2 or y1 == y2:
        return 1
    else:
        x_dif = abs(x1 - x2)
        y_dif = abs(y1 - y2)

        # diagonal
        if x_dif == y_dif:
            return 1
        else:
            return 2


if __name__ == "__main__":
    main()
