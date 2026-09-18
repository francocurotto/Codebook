import argparse

# get input
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

# read file
with open(args.filename, "r") as file:
    plaintext = file.read()

# clean
plaintext = plaintext.replace("\n", " ")
plaintext = plaintext.strip()

# rewrite file
with open(args.filename, "w") as file:
    file.write(plaintext)
