import barcode
from barcode import EAN13

# Името на продукта, което представлява числов код за EAN-13 баркода
product_code = "771011350611"  # 12-цифрен код (последната цифра е checksum)

# Създайте EAN-13 баркод
ean = EAN13(product_code)

# Задаване на името на файла за баркода
barcode_filename = 'product_barcode1'  # Променете разширението според желанието ви (например 'product_barcode.png')

# Запазване на баркода като изображение
barcode_file_path = ean.save(barcode_filename)
print(f"Barcode for product code '{product_code}' saved as '{barcode_file_path}'")
