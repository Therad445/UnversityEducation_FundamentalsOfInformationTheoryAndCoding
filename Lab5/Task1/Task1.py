import library_name  # Замените на имя выбранной библиотеки

# Создайте объект для кодирования и декодирования (Хэмминг или Рида-Соломона)
coder = library_name.Coder()

# Задайте параметры (размер блока, количество исправляемых ошибок и т.д.)

# Создайте тестовые данные с E ошибками
data_with_errors = coder.encode(data_without_errors)  # Закодируйте данные

# Добавьте E ошибок в данные

# Попробуйте декодировать данные с E ошибками
decoded_data = coder.decode(data_with_errors)

# Попробуйте декодировать данные с E+1 ошибкой
decoded_data_with_extra_error = coder.decode(data_with_extra_error)

# Проверьте результаты декодирования
print("Декодированные данные с E ошибками:", decoded_data)
print("Декодированные данные с E+1 ошибкой:", decoded_data_with_extra_error)
