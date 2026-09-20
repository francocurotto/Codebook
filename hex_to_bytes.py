import argparse

# get inputs
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

# read file
with open(args.filename, "r") as file:
    byte_string = file.read()

# create byte array
byte_array = bytearray.fromhex(byte_string)

# write to file
with open("CIPHER", "wb") as file:
    file.write(byte_array)
