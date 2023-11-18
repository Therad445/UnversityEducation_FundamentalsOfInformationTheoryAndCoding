from shannonfano import ShannonFanoCoding

# Create an instance of ShannonFanoCoding
sfc = ShannonFanoCoding()

# Compress a sample text file
input_file = 'sample.txt'
output_file = 'sample_compressed.bin'
sfc.compress(input_file, output_file)

# Decompress the compressed file
decompressed_file = 'sample_decompressed.txt'
sfc.decompress(output_file, decompressed_file)