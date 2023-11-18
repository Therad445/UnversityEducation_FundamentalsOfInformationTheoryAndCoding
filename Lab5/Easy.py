import libhamming as hamming

# Создание экземпляра класса HammingCodec
hamming = hammingcode

# Закодированные данные
encoded_data = hamming.encode('1010')

# Декодирование с одной ошибкой
decoded_data_1 = hamming.decode('1000')

# Декодирование с двумя ошибками
decoded_data_2 = hamming.decode('1110')

print(encoded_data, decoded_data_1, decoded_data_2)