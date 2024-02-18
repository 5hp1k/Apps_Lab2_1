import zipfile
import json


def count_people_in_moscow(zip_file_path):
    moscow_residents = 0

    with zipfile.ZipFile(zip_file_path, 'r') as myzip:
        for file_name in myzip.namelist():
            with myzip.open(file_name) as file:
                if file_name.endswith('.json'):
                    data = json.load(file)
                    if 'city' in data and data['city'] == 'Moscow':
                        moscow_residents += 1

    return moscow_residents


zip_file_path = input("Введите путь к zip-архиву: ")
if zipfile.is_zipfile(zip_file_path):
    count = count_people_in_moscow(zip_file_path)
    print(f"Количество людей, проживающих в Москве: {count}")
else:
    print("Указанный файл не является zip-архивом или не найден.")
