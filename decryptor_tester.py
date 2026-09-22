import argparse
import pandas as pd

# get inputs
parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("split", type=int)
parser.add_argument("offset", type=int)
args = parser.parse_args()

# read file
with open(args.filename, "rb") as file:
    byte_array = file.read()

# get byte split
byte_split = byte_array[args.offset::args.split]

# test all possible decryption bytes
BYTES = 256
tests = []
for key_byte in range(BYTES):
    test = []
    for cipher_byte in byte_split:
        test_byte = cipher_byte ^ key_byte
        if test_byte < 0x20 or test_byte > 0x7e:
            test_char = "❌"
        else:
            test_char = bytearray([test_byte]).decode("utf-8")
        test.append(test_char)
    tests.append(test)

# convert into csv
result = pd.DataFrame(tests)
result.to_csv(f"TEST_{args.filename}_{args.split}_{args.offset}.csv")
