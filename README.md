# my-python-scripts
Some python scripts I wrote during study that I found useful for me.

## Shuffle/
This folder contains a simple python script shuffle.py that performs a random shuffle process of a .txt file that contains English vocabulary, one at a line. 
### Usecase
I use it when memorizing English words for tests, after completing memorizing an amount for a day, say stored in in1.txt file, I would shuffle this file to see if I can still remeber them. The script also provides other functions like combined shuffle (input multiple files, seperate by ',', and shuffle them together, you can also set limits to control the size of output file you want. Besides, you can store in a file called case.txt some of the words you stuck and got wrong and use --withcase/--nocase flag to indicate whether you want to add them into the shuffle pool)
### How to run
#### case1: simply input several files, shuffle and output
```Bash
python shuffle.py --infile in1.txt,in2.txt,in3.txt --outfile out.txt
```
This inputs 3 files: int1.txt, int2.txt, int3.txt and output out.txt, with no limit and no case involved.
#### case2: set output size limit and import words from case.txt
```Bash
python shuffle.py --infile in1.txt,in2.txt,in3.txt --outfile out.txt --limit 30 --hascase
```
This inputs 3 files: int1.txt, int2.txt, int3.txt and output out.txt, with size of 30 words and case involved.



