#!/usr/bin/env python

i = 0
with open('ncbi_cleaned_gene_products.txt', 'rU') as input:
    for line in input:
        i = i + 1
        line = line.strip()
        if line.startswith('#'):
            continue
        if "\t" not in line:
            print("Line [%d] is not tab delimited\n%s"%(i,line))
            exit()
        ID, product = line.split('\t')
