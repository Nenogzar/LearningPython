##########################################*-*FROM*TAMER*-*##########################################
# Ако текущият файл има директория, пропуск (continue).
# Извлича се разширението на файла.
# Ако разширението не се съдържа в списъка с разширения , пропуска се итерацията .extensions
# Създава се път към директорията за съответното разширение.
# Ако тази директория не съществува, се създава.
# Файлът се премества в новосъздадената директория.

##########################################*-*FROM*TAMER*-*##########################################

# import os
# import shutil
#
# def main():
#
#     pass
#
#
# if __name__ == "__main__":
#     main()
#
#     base_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
#
#     all_files = os.listdir(base_path)
#     for file in all_files:
#         current_file_path = os.path.join(base_path, file)
#         print(current_file_path)
#         if os.path.isdir(current_file_path):
#             continue
#
#         file_extension = file.split(".")[-1]
#
#
#         directory_path = os.path.join(base_path, file_extension)
#         if not os.path.exists(directory_path):
#             os.mkdir(directory_path)
#
#
#         if not os.path.samefile(current_file_path, directory_path):
#             shutil.move(src=current_file_path, dst=os.path.join(directory_path, file))



import os
import shutil


def main():

    pass


def process_user_downloads(user_path):
    downloads_path = os.path.join(user_path, 'Downloads')

    if os.path.exists(downloads_path):
        process_downloads(downloads_path)


def process_downloads(base_path):
    all_files = os.listdir(base_path)
    for file in all_files:
        current_file_path = os.path.join(base_path, file)
        print(current_file_path)
        if os.path.isdir(current_file_path):
            continue

        file_extension = file.split(".")[-1]

        # Folders whit files extension
        directory_path = os.path.join(base_path, file_extension)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

        # chek for curent folder is not a same
        if not os.path.samefile(current_file_path, directory_path):
            shutil.move(src=current_file_path, dst=os.path.join(directory_path, file))


if __name__ == "__main__":
    main()

    users_path = 'C:\\Users\\'

    # Users on activdir
    for user_name in os.listdir(users_path):
        user_path = os.path.join(users_path, user_name)
        if os.path.isdir(user_path):
            process_user_downloads(user_path)
