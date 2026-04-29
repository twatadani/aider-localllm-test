import os

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def print_directory_structure(start_path):
    for dirpath, dirnames, filenames in os.walk(start_path):
        level = dirpath.replace(start_path, '').count(os.sep)
        indent = '    ' * (level - 1) + '|-- ' if level > 0 else ''
        print('{}{}/'.format(indent, os.path.basename(dirpath)))
        subindent = '    ' * level + '|-- ' if level > 0 else ''
        for f in filenames:
            fp = os.path.join(dirpath, f)
            file_size = os.path.getsize(fp)
            print('{}{} ({:.2f} KB)'.format(subindent, f, file_size / 1024))
