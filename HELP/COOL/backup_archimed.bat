import shutil
import os
from datetime import datetime, timedelta

source_directory = "R:"
destination_directory_q = "Q:"
destination_directory_p = "P:"
backup_age_limit_q = 14  # Брой дни след които да се изтриват бекъпите в Q:
backup_age_limit_p = 14  # Брой дни след които да се изтриват бекъпите в P:
backup_age_limit_r = 7   # Брой дни след които да се изтриват бекъпите в R:

# Функция за изтриване на стари файлове
def delete_old_files(directory, age_limit):
    current_time = datetime.now()
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if current_time - file_modified_time > timedelta(days=age_limit):
                os.remove(file_path)
                print(f"Изтрит файл: {file_path}")

try:
    # Копиране на бекъпите
    shutil.copytree(source_directory, destination_directory_q)
    shutil.copytree(source_directory, destination_directory_p)
    print("Бекъп файловете са успешно копирани.")

    # Изтриване на стари бекъпи
    delete_old_files(destination_directory_q, backup_age_limit_q)
    delete_old_files(destination_directory_p, backup_age_limit_p)
    delete_old_files(source_directory, backup_age_limit_r)

    print(f"Старите бекъпи са успешно изтрити след {backup_age_limit_q} дни в Q: и {backup_age_limit_p} дни в P:.")
    print(f"Старите бекъпи са успешно изтрити след {backup_age_limit_r} дни в R:.")
except Exception as e:
    print(f"Грешка при копирането на бекъп файловете: {str(e)}")
