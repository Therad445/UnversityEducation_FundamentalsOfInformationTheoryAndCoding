def encode_hamming(data):
    # Рассчитать контрольные биты
    parity_bits = []
    data_len = len(data)
    for i in range(data_len):
        if 2 ** i > data_len + i:
            break
        parity_bits.append(2 ** i)

    encoded_data = []
    j = 0
    for i in range(1, data_len + len(parity_bits) + 1):
        if i in parity_bits:
            encoded_data.append(0)  # Заполняем контрольные биты нулями
        else:
            encoded_data.append(int(data[j]))
            j += 1

    # Вычислить значения контрольных битов
    for p in parity_bits:
        parity_sum = 0
        for i in range(p - 1, len(encoded_data), p * 2):
            parity_sum += sum(encoded_data[i:i + p])
        encoded_data[p - 1] = parity_sum % 2

    return encoded_data


def decode_hamming(encoded_data):
    parity_bits = []
    data_len = len(encoded_data)
    decoded_data = []
    error_bit = 0

    # Рассчитать контрольные биты
    for i in range(data_len):
        if 2 ** i > data_len:
            break
        parity_bits.append(2 ** i)

    # Проверить контрольные биты
    for p in parity_bits:
        parity_sum = 0
        for i in range(p - 1, len(encoded_data), p * 2):
            parity_sum += sum(encoded_data[i:i + p])
        if parity_sum % 2 != encoded_data[p - 1]:
            error_bit += p

    if error_bit > 0:
        print(f"Ошибка в бите {error_bit}. Исправление...")
        encoded_data[error_bit - 1] = 1 - encoded_data[error_bit - 1]

    j = 0
    for i in range(1, data_len + 1):
        if i not in parity_bits:
            decoded_data.append(encoded_data[j])
            j += 1

    return decoded_data


# Пример использования
data = "1101001"  # Ваш блок данных
encoded_data = encode_hamming(data)
print("Закодированные данные:", encoded_data)
decoded_data = decode_hamming(encoded_data)
print("Декодированные данные:", decoded_data)

