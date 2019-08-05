# suppose a function called main() and
# all the operations are performed
from sys import stdin

POINTABLE = ['A', 'K', 'Q', 'J']
ACE = ('A', 4)
KING = ('K', 3)
QUEEN = ('Q', 2)
JACK = ('J', 1)


def main():
    for line in stdin:
        hand = list((line.strip().split()))
        get_points(hand)


def get_points(hand):
    suits = {'C': 0, 'H': 0, 'D': 0, 'S': 0}
    kqs_count = {'A': '', 'K': '', 'Q': '', 'J': ''}
    untier = {'C': '', 'H': '', 'D': '', 'S': ''}

    points = 0

    for card in hand:
        if card[0] in POINTABLE:
            points += get_cn_points(card[0])
            kqs_count[card[0]] += card[1]
            untier[card[1]] += card[0]
        suits[card[1]] += 1

    extra_points = get_extra_points(suits)
    nega_points = get_king_points(suits, kqs_count) + get_queen_points(suits, kqs_count) + get_jack_points(suits,
                                                                                                           kqs_count)
    points = points + extra_points - nega_points
    response = get_bet(points, suits, extra_points, untier)
    print(response)


def get_bet(points, suits, extra_points, untier):
    response = ''

    if points < 14:
        response = 'PASS'
    elif points >= 16 and extra_points == 0:
        response = 'BID NO-TRUMP'
    elif points >= 14:
        s = get_max_suit(suits, untier)
        response = 'BID ' + s
    return response


def get_max_suit(suits, untier):
    max_suit_v = 0
    max_suit_k = ''

    for k, v in suits.items():
        if v > max_suit_v:
            max_suit_v = v
            max_suit_k = k
        elif v == max_suit_v:
            if len(untier[k]) > len(untier[max_suit_k]):
                max_suit_v = v
                max_suit_k = k

    return max_suit_k


def get_cn_points(n_card):
    points = 0
    if n_card == ACE[0]:
        points = ACE[1]
    elif n_card == KING[0]:
        points = KING[1]
    elif n_card == QUEEN[0]:
        points = QUEEN[1]
    elif n_card == JACK[0]:
        points = JACK[1]
    return points


def get_king_points(suits, kqs_count):
    kings = set(kqs_count['K'])
    k_points = 0

    for king in kings:
        if suits[king] == 1:
            k_points += 1
    return k_points


def get_queen_points(suits, kqs_count):
    queens = set(kqs_count['Q'])
    q_points = 0

    for queen in queens:
        if suits[queen] == 0 or suits[queen] == 2:
            q_points += 1

    return q_points


def get_jack_points(suits, kqs_count):
    jacks = set(kqs_count['J'])
    j_points = 0

    for jack in jacks:
        if 0 <= suits[jack] <= 2:
            j_points += 1
    return j_points


def get_extra_points(suits):
    plus = 0

    for k, v in suits.items():
        if v == 2:
            plus += 1
        if v == 1 or v == 0:
            plus += 2

    return plus


if __name__ == "__main__":
    main()
