import os
from task1 import parse_file_size


def get_directory_size(directory):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def get_top_10_largest_directories(directory):
    directory_sizes = [(os.path.join(directory, d), get_directory_size(os.path.join(directory, d)))
                       for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    sorted_directories = sorted(directory_sizes, key=lambda x: x[1], reverse=True)

    return sorted_directories[:10]


directory_path = input("Введите путь к каталогу: ")

if os.path.exists(directory_path):
    top_10_directories = get_top_10_largest_directories(directory_path)

    print("TOP-10 самых 'замусоренных' каталогов:")
    for i, (dir_path, size) in enumerate(top_10_directories, start=1):
        print(f"{i}. {dir_path} - {parse_file_size(size)}")
else:
    print("Указанный путь не существует.")
