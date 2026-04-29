import os

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def print_directory_structure(start_path = '.'):
    for dirpath, dirnames, filenames in os.walk(start_path):
        level = dirpath.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(dirpath)))
        subindent = ' ' * 4 * (level + 1)
        for f in filenames:
            print('{}{}'.format(subindent, f))
