# import inbuilt standard input output
from sys import stdin, stdout


# suppose a function called main() and
# all the operations are performed
def main():
    # for read and iterate all the lines
    for line in stdin:
        # print with stdout.write method the string parsed line
        stdout.write(return_equation(line))
    # call the main method


def return_equation(text):
    return text


if __name__ == "__main__":
    main()

