# suppose a function called main() and
# all the operations are performed
from sys import stdin


def main():
    # for read and iterate all the lines
    for line in stdin:
        n, b, h, w = map(int, line.strip().split())
        minimum = []

        for _ in range(h):
            price = int(input())
            n_rooms = list(map(int, input().split()))

            for n_room in n_rooms:
                if n_room >= n:
                    cost = calc_price(n, price)
                    if cost <= b:
                        minimum.append(cost)

        if len(minimum):
            print(min(minimum))
        else:
            print('stay home')


def calc_price(n, price):
    return n * price


if __name__ == "__main__":
    main()
