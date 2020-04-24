import random
import argparse
from time import *
import sys

# python shuffle --infile 1,2 --outfile out.txt
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--infile", type=str, default="1")
parser.add_argument("--outfile", type=str, default="out")
parser.add_argument("--limit", type=int, default=sys.maxsize)
parser.add_argument('--addstumble', dest='stumble', action='store_true')
parser.add_argument('--nostumble', dest='stumble', action='store_false')
parser.set_defaults(stumble=False)
args = parser.parse_args()

infile = args.infile.split(",")
# infile = ["in" + num + ".txt" for num in  infile]
# outfile = args.outfile + ".txt"
outfile = args.outfile
result, extra_case = [], []
limit = args.limit

if args.stumble is True:
    print("Reading {} input files with extra stumbled words appended.....".format(len(infile)))
    with open("stumble.txt", "r") as fin:
        for line in fin:
            extra_case.append(line)
else:
    print("Reading {} input files.....".format(len(infile)))


start_time = -1 * time()
# read words, store each one in an entry in result
for file in infile:
    with open(file, "r") as fin:
        for line in fin:
            result.append(line)

# shuffle the result
print("Shuffling.....")
random.shuffle(result)

if limit != sys.maxsize:
    result = result[:limit]
if args.stumble:
    result.extend(extra_case)


print("Shuffling done! Writing to " + outfile)
# write into file
file_handle = open(outfile,mode='w')

for i, item in enumerate(result):
    file_handle.write(item)

file_handle.close()

end_time = time()
print("Writing done! Now closing.")
print(50*'=')
print("Time elapsed: {:.4f}".format(end_time + start_time))

