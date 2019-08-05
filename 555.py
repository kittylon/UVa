# suppose a function called main() and
# all the operations are performed
from sys import stdin

ORDER = ['S', 'W', 'N', 'E']
SUITS = {
            'C': 200,
            'D': 1000,
            'S': 10000,
            'H': 100000,
        }

PIECES = {
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }


def main():
    for line in stdin:
        dealer = line.strip()
        if dealer != '#':
            cards_1 = input().strip()
            cards_2 = input().strip()
            cards = cards_1 + cards_2
            s_cards = sort_cards(dealer, cards)
            for k, v in s_cards.items():
                print('{}: {}'.format(k, ' '.join(sorted(v, key=suit_order))))
        else:
            return False


def suit_order(card):
    if card[1] in PIECES.keys():
        w = PIECES[card[1]]
    else:
        w = int(card[1])
    return SUITS[card[0]] + w


def sort_cards(dealer, cards):
    hands_dict = {'S': [], 'W': [], 'N': [], 'E': []}
    dealer_index = ORDER.index(dealer) + 1

    for i in range(0, len(cards), 2):
        if dealer_index == len(ORDER):
            dealer_index = 0
        hands_dict[ORDER[dealer_index]] += [cards[i: i + 2]]
        dealer_index += 1
    return hands_dict


if __name__ == "__main__":
    main()
