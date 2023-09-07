#!/usr/bin/python3

def text_indentation(text):
    '''
    Prints the given text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    prev_char = ""

    for char in text:
        if char in ['.', '?', ':']:
            new_text += char + "\n\n"
        else:
            new_text += char

    lines = new_text.split("\n")
    cleaned_lines = [line.strip() for line in lines]
    formatted_text = "\n".join(cleaned_lines)

    print(formatted_text)

