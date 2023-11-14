import os

count_files = 0
PATH = 'F:\Python\Project\LearningPython\softuni_pb\02_python_fundamentals'
file_list = []

for root, dirs, files in os.walk(PATH):
    for directories in dirs:
        for file in files:
            count_files += 1

        file_list.append([directories, count_files])
        count_files = 0

for item in file_list:
    print(item)

