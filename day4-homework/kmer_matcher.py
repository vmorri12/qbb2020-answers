#!/usr/bin/env python3

import sys
from fasta_iterator_class import FASTAReader

k=int(sys.argv[3])
file_target = sys.argv[1]
target_reader = FASTAReader (open(file_target))
file_query = sys.argv[2]
reader = FASTAReader(open(file_query))

target_dict = {}
for seqid_target, seq_target in target_reader:
    for i in range(0, len(seq_target)-k+1):
        kmer = seq_target[i:i+k]
        if kmer in target_dict:
            target_dict[kmer].append((i,seqid_target))
        else:
            target_dict[kmer] = [(i,seqid_target)]
        
count =0
for seqid_query, seq_query in reader:
    for i in range(0, len(seq_query) - k +1):   
        query_kmer = seq_query[i:i + k]
        
        if query_kmer in target_dict:
            count += 1
            print([target_dict[query_kmer], i, query_kmer])
            if count >1000:
                break 
                