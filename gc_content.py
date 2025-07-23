#!/usr/bin/env python3
import sys

def gc_content(seq):
    g = seq.count('G')
    c = seq.count('C')
    return round((g + c) / len(seq) * 100, 2) if seq else 0

def parse_fasta(filename):
    with open(filename) as f:
        seq_id = None
        seq = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq_id:
                    print(f"{seq_id}\t{gc_content(seq)}")
                seq_id = line[1:]
                seq = ''
            else:
                seq += line
        if seq_id:
            print(f"{seq_id}\t{gc_content(seq)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: gc_content.py <input_fasta>")
        sys.exit(1)
    parse_fasta(sys.argv[1])
