import os


def parse_file_size(size):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{round(size)}{units[unit_index]}"


def main():
    files = [f for f in os.listdir() if os.path.isfile(f)]

    for file in files:
        file_size = os.path.getsize(file)
        print(f"{file} {parse_file_size(file_size)}")
