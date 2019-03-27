
#!/bin/python

import sys
import random


def gen_random_nuc():
    """
     This generates random nucleotides.
    """
    nucleotide= ['A','T','C','G']
    return random.choice(nucleotide)

def gen_seq(lim):
    """
    This generates a string of lim characters.
    lim is the limit length of characters per line of the sequence.
    """
    sequence = ""
    i = 0
    while i <lim:
        sequence = sequence+gen_random_nuc()
        i = i + 1
    return sequence

def write_seq(read_length, outFile):
    """
    Takes read length and name of file to be created as input.
    Determines the number of full lines to print.
    With the length of the last line as read_length modulus 80.
    """
    full_lines=read_length//80
    length_of_last_line= read_length % 80
    with open(outFile,'a') as ourfile:
        full_line_no = 0
        while full_line_no < full_lines:
            line = gen_seq(80)
            print(line, file=ourfile)
            full_line_no = full_line_no + 1
        last_line = gen_seq(length_of_last_line)
        print(last_line,file=ourfile)
    
def writeFile(filename, num):
    """
    Prints sequence names to output file before writing sequence.
    """
    header = "> seq "+str(num+1)+'\n'
    with open(filename,'a') as ourfile:
        ourfile.write(header)
    
def no_seq(seq_no, r, z):
    """
    Writes to ouput file the headers and the sequence
    With number of sequence to be printed(seq_no), read_length(r) and output file(z),
    """
    for i in range(0,seq_no):
        writeFile(z,i)
        write_seq(r,z)


def main():
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = sys.argv[3]
    no_seq(x,y,z)

main()
# python random_req 5 417