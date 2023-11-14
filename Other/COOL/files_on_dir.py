#__________________________________*-*Брои*файлове*в*директории*-*___________________________________

import os

count_files = 0
PATH = 'F:\C#'
file_list = []

for root, dirs, files in os.walk(PATH):
    for directories in dirs:
        for file in files:
            count_files += 1

        file_list.append([directories, count_files])
        count_files = 0

for item in file_list:
    print(item)

# import os
#
# count_files = 0
# PATH = r'F:\C#'
# file_list = []
#
# for root, dirs, files in os.walk(PATH):
#
#     count_files = len(files)
#
#     folder_name = root.replace(PATH, '').count(os.path.sep) * '-' + os.path.basename(root)
#
#     file_list.append([folder_name, count_files])
#
# for item in file_list:
#     print(item)


##########################################*-*FROM*TAMER*-*##########################################
# Ако текущият файл има директория, пропуск (continue).
# Извлича се разширението на файла.
# Ако разширението не се съдържа в списъка с разширения , пропуска се итерацията .extensions
# Създава се път към директорията за съответното разширение.
# Ако тази директория не съществува, се създава.
# Файлът се премества в новосъздадената директория.

##########################################*-*FROM*TAMER*-*##########################################

