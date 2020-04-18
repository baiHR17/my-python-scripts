import random
import argparse
from time import *
import sys

# python shuffle --infile in1.txt,in2.txt --outfile out.txt
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--infile", type=str, default="in1.txt")
parser.add_argument("--outfile", type=str, default="out.txt")
parser.add_argument("--limit", type=int, default=sys.maxsize)
parser.add_argument('--addstumble', dest='stumble', action='store_true')
parser.add_argument('--nostumble', dest='stumble', action='store_false')
parser.set_defaults(stumble=False)
args = parser.parse_args()

infile = args.infile.split(",")
result, extra_case = [], []

print(args.stumble)
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
if args.limit != sys.maxsize:
    result = result[:args.limit]
if args.stumble:
    result.extend(extra_case)
random.shuffle(result)


print("Shuffling done! Writing to " + args.outfile)
# write into file
file_handle = open(args.outfile,mode='w')

for i, item in enumerate(result):
    file_handle.write(item)

file_handle.close()

end_time = time()
print("Writing done! Now closing.")
print(50*'=')
print("Time elapsed: {:.4f}".format(end_time + start_time))

