#!/usr/bin/env python

#script to update gene2products database

import sys, os, inspect, datetime
from natsort import natsorted
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

if len(sys.argv) < 2:
    print('Usage: update-gene2product.py two-column-file.tsv')
    sys.exit(1)
    
#just going to do something simple here, must be run from gene2products directory
#input will be a two-column tsv file

today = datetime.datetime.today().strftime('%m-%d-%Y')

#first load existing DB
version = None
Data = {}
with open(os.path.join(currentdir, 'ncbi_cleaned_gene_products.txt'), 'rU') as db:
    for line in db:
        line = line.strip()
        if line.startswith('#version'):
            version = line.split(' ')[-1]
        elif line.startswith('#'):
            continue
        else:
            name, product = line.split('\t')
            #product = product[0].lower() + product[1:]
            #do some checks here of product name
            if product == 'protein '+name or product == name+' protein' or product == name.lower()+' protein':
                continue
            if len(product) > 100:
                print('Product too long: %s' % product)
                product = raw_input("Product for %s: " % name)
            if not name in Data:
                Data[name] = product
            else: #existing name, so warn
                print('%s duplicate gene name, skipping' % name)

#load updating text file, add to dictionary
with open(sys.argv[1], 'rU') as update:
    for line in update:
        line = line.strip()
        if line.startswith('#'):
            continue
        name, product = line.split('\t')
        #do some checks here of product name
        if product == 'protein '+name or product == name+' protein' or product == name.lower()+' protein':
            continue
        if len(product) > 100:
            print('Product too long: %s' % product)
            product = raw_input("Product for %s: " % name)
        if not name in Data:
            Data[name] = product
        else: #existing name, so warn
            print('%s duplicate gene name, skipping' % name)

#move old database and version
os.rename(os.path.join(currentdir, 'ncbi_cleaned_gene_products.txt'), os.path.join(currentdir, 'ncbi_cleaned_gene_products.v'+version+'.txt'))
versNum = int(version.split('.')[-1]) + 1
NewVersion = version.split('.')[0] + '.' + str(versNum)
with open(os.path.join(currentdir, 'ncbi_cleaned_gene_products.txt'), 'w') as output:
    output.write('#version %s\n' % NewVersion)
    output.write('#Date %s\n' % today)
    output.write('#Name\tDescription\n')
    for k,v in natsorted(Data.items()):
        output.write('%s\t%s\n' % (k,v))
