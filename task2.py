from zipfile import ZipFile
import task1


with ZipFile(r'C:\Универ\3 Курс\Разработка приложений\2 Семестр\Лаб 1\1 OS.zip') as myzip:
    for name in myzip.namelist():
        items = name.rstrip("/").split("/")
        file_size = myzip.getinfo(name).file_size
        print("  "*(len(items)-1) + items[-1], task1.parse_file_size(file_size))
