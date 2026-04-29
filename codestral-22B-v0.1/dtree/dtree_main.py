import os

def draw_directory_tree(path, indent=""):
    print(indent + os.path.basename(path) + "/")
    indent += "|  "
    items = os.listdir(path)
    for i, item in enumerate(items):
        item_path = os.path.join(path, item)
        if i == len(items) - 1:
            prefix = "└──"
        else:
            prefix = "├──"
        if os.path.isdir(item_path):
            print(indent[:-2] + prefix, end="")
            draw_directory_tree(item_path, indent)
        else:
            print(indent + prefix, item)

if __name__ == '__main__':
    draw_directory_tree(".")
