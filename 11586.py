# suppose a function called main() and
# all the operations are performed


def main():
    # for read and iterate all the lines
    t_cases = int(input())
    for line in range(t_cases):
        # print with stdout.write method the string parsed line
        tracks = list(input().split())
        if is_loop(tracks):
            print('LOOP')
        else:
            print('NO LOOP')


def is_loop(tracks):
    m = 0
    f = 0
    for track in tracks:
        for letter in track:
            if letter == 'M':
                m += 1
            elif letter == 'F':
                f += 1
    if m == f and len(tracks) > 1:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

