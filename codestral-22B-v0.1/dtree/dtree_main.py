import os
import sys
from directory_traversal import print_directory_structure

def draw_directory_tree(path, indent=""):
    print("%s%s/" % (indent, path.split('/')[-1]))
    for sub_path in [os.path.join(path, p) for p in os.listdir(path) if os.path.isdir(os.path.join(path, p))]:
        draw_directory_tree(sub_path, indent + "    ")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        start_path = sys.argv[1]
    else:
        start_path = '.'
    print_directory_structure(start_path)
