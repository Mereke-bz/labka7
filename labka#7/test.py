import os

path_folder = r"C:\Users\merek\OneDrive\Рабочий стол\labka#7"
song1 = os.path.join(path_folder, "00046ed484682b33d3200651d856f2d0")

if os.path.exists(song1):
    print("Путь найден!")
else:
    print("Ошибка: путь не существует.")