# This file is used to delete the repeated dialogues of the game Planescape: Torment: Enhanced Edition.

import re
from pprint import pprint

FILENAME = "planescape_dialogue.txt"
MODIFIED_FILENAME = "planescape_dialogue_without_duplication.txt"
NUMBER_REGEX = r"^\d+:$"

def are_elements_not_blank(temp):
    for temp_index, temp_text in enumerate(temp):
        if temp_index != 0 and temp_text != "":
            return True
    return False

def is_last_element():
    return index == len(lines) - 1

def is_double_line_break(index,texts):
    return index > 0 and texts[index - 1] == "" and texts[index] == ""

def main():
    with open(FILENAME, encoding="utf-8", mode="r") as f:
        lines = f.readlines()



    temp = []
    texts = []

    for index, line in enumerate(lines):
        try:
            number_text = re.compile(NUMBER_REGEX).search(line).group()
            pprint(number_text)

            if len(temp) == 0: # first line of the file.
                temp.append(number_text)

            else:
                if are_elements_not_blank(temp):
                    for temp_text in temp:
                        texts.append(temp_text.strip())

                elif is_last_element(index,lines):
                    for temp_text in temp:
                        texts.append(temp_text.strip())

                temp = []
                temp.append(number_text)

        except AttributeError:
            if line.strip() == "":
                temp.append("")

            elif line.strip() in texts:
                continue

            else:
                temp.append(line.strip())


    with open(MODIFIED_FILENAME, encoding="utf-8", mode="w") as f:
        for index, line in enumerate(texts):

            if is_double_line_break(index,texts):
                continue

        else:
            f.write(line + "\n")

main()