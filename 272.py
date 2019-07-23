# import inbuilt standard input output
from sys import stdin, stdout

FIRST_TYPE = "``"
SECOND_TYPE = "''"
MATCH = '"'
FLAG = 0


# suppose a function called main() and
# all the operations are performed
def main():
    # for read and iterate all the lines
    for line in stdin:
        # print with stdout.write method the string parsed line
        stdout.write(format_text(line))
    # call the main method


def format_text(text):
    global FLAG
    new_text = ''
    for c in text:
        if c == MATCH:
            if FLAG == 0:
                c = FIRST_TYPE
                FLAG = 1
            else:
                c = SECOND_TYPE
                FLAG = 0
        new_text += c
    return new_text


if __name__ == "__main__":
    main()

