import argparse
import pandas as pd

# contstants
BYTES = 128
ALLOWED = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,'?! \n"

# get inputs
parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("split", type=int)
args = parser.parse_args()

# read file
with open(args.filename, "rb") as file:
    byte_array = file.read()

# iterate on every offset
results = []
for offset in range(args.split):
    # get byte split
    byte_split = byte_array[offset::args.split]
    # test all possible decryption bytes
    tests = []
    keys = []
    for key_byte in range(BYTES):
        test = []
        for cipher_byte in byte_split:
            test_byte = cipher_byte ^ key_byte
            if test_byte in ALLOWED:
                test_char = bytearray([test_byte]).decode("utf-8")
                test.append(test_char)
        if len(test) == len(byte_split):
            keys.append(key_byte)
            tests.append(test)

    # convert into csv
    results.append(pd.DataFrame(tests, index=keys))

excel = f"TEST_{args.filename}_{args.split}.xlsx"
with pd.ExcelWriter(excel, engine="openpyxl") as writer:
    for i, result in enumerate(results):
        result.to_excel(writer, sheet_name=f"Offset {i + 1}")
