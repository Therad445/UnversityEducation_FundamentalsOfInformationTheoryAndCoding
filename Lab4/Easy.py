def rle_encode(data):
    encoded = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded += data[i - 1] + str(count)
            count = 1
    encoded += data[-1] + str(count)
    return encoded

def rle_decode(data):
    decoded = ""
    count = ""
    for char in data:
        if char.isdigit():
            count += char
        elif count:
            decoded += char * int(count)
            count = ""
    return decoded

original_data = "AAABBBCCCC"
encoded_data = rle_encode(original_data)
decoded_data = rle_decode(encoded_data)

print("Исходные данные:", original_data)
print("Закодированные данные:", encoded_data)
print("Декодированные данные:", decoded_data)