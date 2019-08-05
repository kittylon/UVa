# suppose a function called main() and
# all the operations are performed
from sys import stdin


def main():
    for line in stdin:
        a, b = line.strip().split()
        if a != '0' and b != '0':
            a_cards = set((input().strip().split()))
            b_cards = set(input().strip().split())

            max_cards = get_max_cards(a_cards, b_cards)
            print(max_cards)
        else:
            return False


def get_s_xl_hand(a_cards, b_cards):
    if len(a_cards) > len(b_cards):
        big_hand = a_cards
        small_hand = b_cards
    else:
        big_hand = b_cards
        small_hand = a_cards
    return small_hand, big_hand


def get_max_cards(a_cards, b_cards):
    small_hand, big_hand = get_s_xl_hand(a_cards, b_cards)

    cards = small_hand.difference(big_hand)
    return len(cards)


if __name__ == "__main__":
    main()
