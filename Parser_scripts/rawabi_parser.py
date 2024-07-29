import json
import os
import re

DATE_LINE = 1

def read_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data.txt")

    with open(file_path, "r") as file:
        lines = file.readlines()

    lines.pop()  # to remove the last line
    lines.pop(DATE_LINE)
    return lines


def information_split(lines, my_dict):
    lines.pop()
    # to remove itme count line
    new_lines = []
    for line in lines:
        if re.search(r':', line):
            key, value = line.split(":", 1)
            my_dict[key.strip()] = value.strip()
        else:
            new_lines.append(line)
    return new_lines


def item_split(lines, my_dict):
    list_of_items = []
    while (lines):
        item_dict = {}
        item_name = lines.pop(0)
        item_dict["name"] = item_name.strip()
        line = re.split(r'[x ]+', lines.pop(0).strip())
        item_dict["quantity"] = line[0]
        item_dict["price"] = line[1]
        item_dict["total_price"] = line[2]
        list_of_items.append(item_dict)

    my_dict["list_of_item"] = list_of_items


def conv_to_json(my_dict):
    invoice_json = json.dumps(my_dict, indent=6)

    with open("sample.json", "w") as outfile:
        outfile.write(invoice_json)


def rawabi_parser():
    my_dict = {}
    lines = read_file()
    lines= information_split(lines, my_dict)
    item_split(lines, my_dict)
    conv_to_json(my_dict)
