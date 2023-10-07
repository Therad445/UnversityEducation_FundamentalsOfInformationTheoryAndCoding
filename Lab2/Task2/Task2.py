import collections
import math
import unicodedata

# Функция для расчета информации в символе
def calculate_information(probability):
    if probability == 0:
        return 0
    return -math.log2(probability)

# Открываем файл для анализа
file_path = 'путь_к_вашему_файлу.txt'  # Замените на путь к вашему файлу
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Рассчитываем длину файла в символах Unicode
file_length = len(file_content)

# Считаем частоту вхождения каждого символа Unicode
char_frequencies = collections.Counter(file_content)

# Рассчитываем вероятность и информацию для каждого символа
char_probabilities = {char: freq / file_length for char, freq in char_frequencies.items()}
char_information = {char: calculate_information(prob) for char, prob in char_probabilities.items()}

# Сортируем таблицу характеристик символов по алфавиту и по убыванию частоты
sorted_char_probabilities = sorted(char_probabilities.items(), key=lambda x: x[0])
sorted_char_probabilities_by_freq = sorted(char_probabilities.items(), key=lambda x: x[1], reverse=True)

# Рассчитываем суммарное количество информации в файле
total_information = sum(freq * char_information[char] for char, freq in char_frequencies.items())

# Выводим результаты
print(f"Длина файла в символах Unicode: {file_length}")
print("Таблица характеристик символов по алфавиту:")
for char, prob in sorted_char_probabilities:
    print(f"Символ: {char}, Вероятность: {prob:.6f}, Информация: {char_information[char]:.6f}")
print("\nТаблица характеристик символов по убыванию частоты:")
for char, prob in sorted_char_probabilities_by_freq:
    print(f"Символ: {char}, Вероятность: {prob:.6f}, Информация: {char_information[char]:.6f}")
print(f"\nСуммарное количество информации в файле: {total_information:.6f} бит")
print(f"Суммарное количество информации в файле: {total_information / 8:.6f} байт")
