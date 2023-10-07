import collections
import math

# Функция для расчета информации в символе
def calculate_information(probability):
    if probability == 0:
        return 0
    return -math.log2(probability)

# Открываем файл для анализа (замените "file.txt" на имя вашего файла)
file_path = "file.txt"
with open(file_path, 'rb') as file:
    file_content = file.read()

# Рассчитываем длину файла в байтах
file_length = len(file_content)

# Считаем частоту вхождения каждого байта
byte_frequencies = collections.Counter(file_content)

# Рассчитываем вероятность и информацию для каждого байта
byte_probabilities = {byte: freq / file_length for byte, freq in byte_frequencies.items()}
byte_information = {byte: calculate_information(prob) for byte, prob in byte_probabilities.items()}

# Сортируем таблицу характеристик символов по алфавиту и по убыванию частоты
sorted_byte_probabilities = sorted(byte_probabilities.items(), key=lambda x: x[0])
sorted_byte_probabilities_by_freq = sorted(byte_probabilities.items(), key=lambda x: x[1], reverse=True)

# Рассчитываем суммарное количество информации в файле
total_information = sum(freq * byte_information[byte] for byte, freq in byte_frequencies.items())

# Выводим результаты
print(f"Длина файла в байтах: {file_length}")
print("Таблица характеристик символов по алфавиту:")
for byte, prob in sorted_byte_probabilities:
    print(f"Символ: {byte}, Вероятность: {prob:.6f}, Информация: {byte_information[byte]:.6f}")
print("\nТаблица характеристик символов по убыванию частоты:")
for byte, prob in sorted_byte_probabilities_by_freq:
    print(f"Символ: {byte}, Вероятность: {prob:.6f}, Информация: {byte_information[byte]:.6f}")
print(f"\nСуммарное количество информации в файле: {total_information:.6f} бит")
print(f"Суммарное количество информации в файле: {total_information / 8:.6f} байт")
