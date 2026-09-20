import argparse
import pandas as pd

# get inputs
parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("max_length", type=int)
args = parser.parse_args()

# ic computation
def compute_ic(byte_array):
    NBYTES = 256
    ic = 0
    for byte in bytes(range(NBYTES)):
        count = byte_array.count(byte)
        ic += count * (count - 1)
    ic /= (NBYTES * (NBYTES - 1))
    return ic

# read file
with open(args.filename, "rb") as file:
    byte_array = file.read()

# compute Index of Coincidence for different lengths
ics = []
lengths = range(1, args.max_length+1)
for length in lengths:
    partial_ics = []
    for i in range(0, length):
        byte_division = byte_array[i::length]
        ic = compute_ic(byte_division)
        partial_ics.append(ic)
    ics.append(sum(partial_ics))

# print results
results = pd.DataFrame(data={"length":lengths, "IC":ics})
print(results)
