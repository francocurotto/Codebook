import argparse

# get inputs
parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("key")
args = parser.parse_args()

# read file
with open(args.filename, "rb") as file:
    plain_bytes = file.read()

# encode key into bytes and expand
key_bytes = args.key.encode("utf-8")
multiplier = (len(plain_bytes) // len(key_bytes)) + 1
exkey_bytes = (multiplier * key_bytes)[:len(plain_bytes)]

# encrypt
cipher_bytes_list = []
for plain_byte, exkey_byte in zip(plain_bytes, exkey_bytes):
    cipher_bytes_list.append(plain_byte ^ exkey_byte)

# write into a file
cipher = bytes(cipher_bytes_list)
with open("CIPHER", "wb") as file:
    file.write(cipher)
