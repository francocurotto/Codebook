import argparse

# get inputs
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

# read cipher
with open(args.filename, "rb") as file:
    cipher = file.read()

NBYTES = 256
for key_byte in bytes(range(NBYTES)):
    test = []
    for cipher_byte in cipher:
        test.append(cipher_byte ^ key_byte)
    print(bytes(test).decode("utf-8"))
