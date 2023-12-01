import shannon_fano

# Compress a sample text file
input_file = 'beep.wav'
output_file = 'beep.wav_fano.bin'
data = ''
with open(input_file, "rb") as file:
    data = file.read()

print(len(data), data)

encoded, smap = shannon_fano.getEncoded(data)

print(len(encoded), encoded)

# Decompress the compressed file
decompressed_file = 'beep.wav_fano.wav'
decoded = shannon_fano.decode(encoded, smap)

with open(decompressed_file, "wb+") as file:
    file.write(decoded)
