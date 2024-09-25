def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    num_words = get_word_count(text)
    char_dict = get_char_count(text)

    print_formatted_analysis(path, num_words, char_dict)


def get_text(path):
    f = open(path, "r")
    return f.read()


def get_word_count(str):
    return len(str.split())


def get_char_count(str):
    char_count_dict = {}

    for char in str:
        if char.lower() in char_count_dict:
            char_count_dict[char.lower()] += 1
        else:
            char_count_dict[char.lower()] = 1

    return char_count_dict


def filter_char_dict(char_dict):
    alphabet = {
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    }

    # filter out non-letter chars
    letter_count = [
        (char, count) for (char, count) in char_dict.items() if char in alphabet
    ]

    return letter_count


def print_formatted_analysis(path_to_text, word_count, char_count_dict):
    print(f"--- Begin report of {path_to_text} ---")

    print(f"{word_count} words found in the document\n")

    filtered_letter_count = filter_char_dict(char_count_dict)

    sorted_letter_count = sorted(
        filtered_letter_count, key=lambda n: n[1], reverse=True
    )

    for tup in sorted_letter_count:
        char = tup[0]
        count = tup[1]
        print(f"The '{char}' character was found {count} times")


main()
