import collections
import os

def calculate_octet_frequencies(file_path):
    octet_frequencies = collections.Counter()

    with open(file_path, 'rb') as file:
        content = file.read()
        octet_frequencies.update(content)

    return octet_frequencies

def print_top_octets(octet_frequencies, n):
    print(f"Топ {n} октетов:")
    for octet, freq in octet_frequencies.most_common(n):
        print(f"Октет: 0x{octet:02X}, Частота: {freq}")

# Папка с файлами plaintext
plaintext_folder = 'labsfiles/files/plaintext/'

# Перебираем файлы в папке
for filename in os.listdir(plaintext_folder):
    file_path = os.path.join(plaintext_folder, filename)

    if os.path.isfile(file_path):
        octet_frequencies = calculate_octet_frequencies(file_path)
        print(f"\nАнализ файла: {filename}")
        print_top_octets(octet_frequencies, 4)
        
# Путь к файлу 𝑍 (замените на соответствующий путь)
file_z_path = 'путь_к_файлу_𝑍'
if os.path.exists(file_z_path):
    octet_frequencies_z = calculate_octet_frequencies(file_z_path)
    print("\nАнализ файла 𝑍:")
    print_top_octets(octet_frequencies_z, 4)

    # Проверка на кодировку русского текста
    # Проверяем наличие байтов, характерных для UTF-8 кодировки русского текста
    if b'\xd0\xb0' in octet_frequencies_z and b'\xd0\xb0' in octet_frequencies_z:
        print("Файл 𝑍 является русскоязычным текстом в кодировке UTF-8")
    elif b'\xd0\xb0' in octet_frequencies_z:
        print("Файл 𝑍 является русскоязычным текстом, но не в UTF-8")
    else:
        print("Файл 𝑍 не является русскоязычным текстом")


