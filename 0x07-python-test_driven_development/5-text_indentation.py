#!/usr/bin/python3

"""this function define text-indentation."""

def text_indentation(text):
    """ function prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to be printed.
    Raises:
        TypeError: If text is not a string.
    """

    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Skip any whitespace
    e = 0
    while e < len(text) and text[e] == ' ':
        e += 1

    # Loop characters in input string
    while e < len(text):
        # Print current char with no newline
        print(text[e], end="")

        # Check if we need to add newlines
        if text[e] == "\n" or text[e] in ".?:":
            # If the character is one of '.', '?', or ':', add two newlines
            if text[e] in ".?:":
                print("\n")
            print("\n")

            # Skip over any leading whitespace
            e += 1
            while e < len(text) and text[e] == ' ':
                e += 1

            # Continue
            continue

        # Increment character index
        e += 1
