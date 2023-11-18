from arithmeticcoding import ArithmeticCoding

# Create an instance of ArithmeticCoding
ac = ArithmeticCoding()

# Compress a sample text file
input_file = 'sample.txt'
output_file = 'sample_compressed.bin'
ac.compress(input_file, output_file)

# Decompress the compressed file
decompressed_file = 'sample_decompressed.txt'
ac.decompress(output_file, decompressed_file)