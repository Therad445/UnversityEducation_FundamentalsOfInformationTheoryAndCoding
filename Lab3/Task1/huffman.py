from compression import huffman as h

# Compress a sample text file
input_file = 'beep.wav'
output_file = 'beep.wav_huffman.bin'
h.encode_file(input_file, output_file)

# Decompress the compressed file
decompressed_file = 'beep.wav_huffman.wav'
h.decode_file(output_file, decompressed_file)
