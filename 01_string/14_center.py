###############################################Hello################################################

original_string = " - Брои файлове в директории - "
width = 100
fillchar = "#"

centered_string = original_string.center(width, fillchar)
modified_string = centered_string.replace(" ", "*")

print(modified_string)
