import shutil
import os
from datetime import datetime, timedelta

source_directory = "R:"
destination_directory_q = "Q:"
destination_directory_p = "P:"
backup_age_limit_q = 14  # Брой дни след които да се изтриват бекъпите в Q:
backup_age_limit_p = 14  # Брой дни след които да се изтриват бекъпите в P:
backup_age_limit_r = 7   # Брой дни след които да се изтриват бекъпите в R:

# Функция за проверка за съществуващи файлове
def check_existing_files(source_directory, destination_directory):
    for root, _, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination_directory, file)
            if not os.path.exists(destination_file_path):
                # Файлът не съществува в целевия директория, копирайте го
                shutil.copy(file_path, destination_file_path)

# Функция за изтриване на стари файлове
def delete_old_files(directory, age_limit):
    current_time = datetime.now()
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if current_time - file_modified_time > timedelta(days=age_limit):
                os.remove(file_path)

# Копиране на бекъпите
try:
    check_existing_files(source_directory, destination_directory_q)
    # Копирайте само файлове и директории, които не съществуват в целевия директория
    for root, _, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination_directory_p, file)
            if not os.path.exists(destination_file_path):
                # Файлът не съществува в целевия директория, копирайте го
                shutil.copy(file_path, destination_file_path)

    # Изтриване на стари бекъпи
    delete_old_files(destination_directory_q, backup_age_limit_q)
    delete_old_files(destination_directory_p, backup_age_limit_p)
    delete_old_files(source_directory, backup_age_limit_r)

    print(f"Старите бекъпи са успешно изтрити след {backup_age_limit_q} дни в Q: и {backup_age_limit_p} дни в P:.")
    print(f"Старите бекъпи са успешно изтрити след {backup_age_limit_r} дни в R:.")
except Exception as e:
    print(f"Грешка при копирането на бекъп файловете: {str(e)}")
