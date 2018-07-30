#!/usr/bin/env python3


def is_lower_case(char):
    return ord(char) >= 97 and ord(char) <= 122

def is_upper_case(char):
    return ord(char) >= 65 and ord(char) <= 90

def swap_case(string):
    for index, char in enumerate(string):
        if is_lower_case(char):
            string = string[0:index] + char.upper() + string[index+1:]

        elif is_upper_case(char):
            string = string[0:index] + char.lower() + string[index+1:]

    return string


if __name__ == "__main__":
    string = input()

    print(swap_case(string))