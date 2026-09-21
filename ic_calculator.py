import argparse
import numpy as np
import pandas as pd

# get inputs
parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("max_length", type=int)
args = parser.parse_args()

# ic computation
def compute_ic(byte_array):
    BYTES = 256
    ic = 0
    nbytes = len(byte_array)
    for byte in bytes(range(BYTES)):
        count = byte_array.count(byte)
        ic += count * (count - 1)
    ic /= (nbytes * (nbytes - 1))
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
        byte_split = byte_array[i::length]
        ic = compute_ic(byte_split)
        partial_ics.append(ic)
    #ics.append(sum(partial_ics))
    ics.append(np.mean(partial_ics))

# print results
results = pd.DataFrame(data={"length":lengths, "IC":ics})
print(results)
