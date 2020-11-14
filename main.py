import xml.etree.ElementTree as Elements
import argparse

levels = []


def get_level(elem, level=0):
    for child in elem:
        get_level(child, level+1)
    levels.append(level)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?')
    get_name = parser.parse_args()
    file = get_name.file
    root = Elements.parse(file)
    get_level(root.getroot())
    print(max(levels))
