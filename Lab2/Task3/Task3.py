import collections
import os
import chardet


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
plaintext_folder = 'files/plaintext/'

# Перебираем файлы в папке
for filename in os.listdir(plaintext_folder):
    file_path = os.path.join(plaintext_folder, filename)

    if os.path.isfile(file_path):
        octet_frequencies = calculate_octet_frequencies(file_path)
        print(f"\nАнализ файла: {filename}")
        print_top_octets(octet_frequencies, 4)
        
# Путь к файлу 𝑍 (замените на соответствующий путь)
file_z_path = 'files/2.txt'
if os.path.exists(file_z_path):
    # Определяем кодировку файла Z
    with open(file_z_path, 'rb') as file:
        data = file.read()
        result = chardet.detect(data)
        encoding = result['encoding']
        try:
            decoded_text = data.decode(encoding)
            print("Файл Z является русскоязычным текстом в кодировке", encoding)
        except UnicodeDecodeError:
            print("Файл Z не является русскоязычным текстом в стандартных кодировках")
