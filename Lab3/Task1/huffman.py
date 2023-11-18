from huffman import HuffmanCoding

# Create an instance of HuffmanCoding
h = HuffmanCoding()

# Compress a sample text file
input_file = 'sample.txt'
output_file = 'sample_compressed.bin'
h.compress(input_file, output_file)

# Decompress the compressed file
decompressed_file = 'sample_decompressed.txt'
h.decompress(output_file, decompressed_file)