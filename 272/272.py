FIRST_TYPE = "aaaa"
SECOND_TYPE = "'sssss'"
MATCH = '"'


def format_text(text):
    counter = 0
    new_text = ''
    for character in text:
        if character == MATCH:
            counter += 1
            if counter % 2 == 0:
                character = SECOND_TYPE
            else:
                character = FIRST_TYPE
        new_text += character
    return text


if __name__ == '__main__':
    s = input()
    result = format_text(s)
    print(result)
