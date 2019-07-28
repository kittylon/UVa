# suppose a function called main() and
# all the operations are performed
import string
from sys import stdin

abd_dict = dict()

for num, char in enumerate(string.ascii_lowercase, 1):
    abd_dict[char] = num


def main():
    for line in stdin:
        f_name = line.strip()
        s_name = input().strip()

        f_name_total = get_name_number(f_name)
        s_name_total = get_name_number(s_name)

        while f_name_total > 9:
            f_name_total = get_one_digit(f_name_total)

        while s_name_total > 9:
            s_name_total = get_one_digit(s_name_total)

        percentage = (min(f_name_total, s_name_total) / max(f_name_total, s_name_total)) * 100
        print("{:.2f} %".format(percentage))


def get_one_digit(number):
    str_num = str(number)
    sum = 0

    for num in str_num:
        sum += int(num)
    return sum


def get_name_number(name):
    name_sum = 0

    for letter in name:
        if letter.isalpha():
            name_sum += abd_dict[letter.lower()]

    return name_sum


if __name__ == "__main__":
    main()
