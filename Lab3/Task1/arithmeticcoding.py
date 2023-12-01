from arithmetic_compressor import AECompressor
from arithmetic_compressor.models import StaticModel


def calc_model(filename):
    data = dict()
    filedata = ''

    with open(filename, "rb") as file:
        for i in file.read():
            if chr(i) in data:
                data[chr(i)] += 1
            else:
                data[chr(i)] = 1

            filedata += chr(i)

    return data, filedata


def list2bytess(s):
    return b''.join([str(i).encode() for i in compressed])


def write_output(output_file, data):
    with open(output_file, "wb+") as file:
        file.write(data)


model, filedata = calc_model("sample.txt")
model = StaticModel(model)

# create an arithmetic coder
coder = AECompressor(model)

N = len(filedata)
compressed = coder.compress(filedata)
compressed_bytes = list2bytess(compressed)

write_output("sample_compressed_ar.bin", compressed_bytes)

decompressed = coder.decompress(compressed, len(compressed))
print(decompressed)

with open("sample_decompressed_ar.txt", "w+") as file:
    file.write("".join(decompressed))


