#!/usr/bin/env python3
import  urllib.request, csv, sys, warnings, re,os
from urllib.error import HTTPError
import codecs
urlbase="https://www.uniprot.org/uniprot/?query={}&sort=score&columns=id,entry%20name,reviewed,organism,genes(PREFERRED),genes,protein%20names&format=tab&limit=1"
if len(sys.argv) < 2:
    print("No file argument")
    sys.exit(2)

infile = sys.argv[1]
newfile = infile + ".updated"
seen = {}
if os.path.exists(newfile):
    with open(newfile,'rU') as fh:
        d = csv.reader(fh,delimiter="\t")
        for r in d:
            if r[0].startswith("#"):
                continue
            seen[r[0]] = r[1]

pat = re.compile(r'^(.+?)\s+\(')
with open(infile,'r') as genes, open(newfile,'w') as output:
    dat = csv.reader(genes,delimiter="\t")
    out = csv.writer(output,delimiter="\t")
    for line in dat:
        if line[0].startswith("#"):
            continue
        if line[0] in seen:
            newdesc = seen[line[0]]
            newdesc = re.sub(r'\[Includes:.+','',newdesc)
            out.writerow([line[0],newdesc])
            output.flush()
            continue
        url=urlbase.format(line[0])
        #        warnings.warn("url is {}".format(url))
        try:
            with urllib.request.urlopen(url) as uniprot:
                uniprotdat = csv.reader(codecs.iterdecode(uniprot,'utf-8'),delimiter="\t")
                header = 0
                for row in uniprotdat:
                    if header == 0:
                        header = 1
                        continue
                    newdesc = row[6]
                    m = pat.match(newdesc)
                    if m:
                        newdesc = m.group(1)
                    newdesc = re.sub(r'\[Includes:.+','',newdesc)
                    out.writerow([line[0],newdesc])
                    output.flush()
        except urllib.error.HTTPError as err:
            print("Error is ",err.code,err.reason," for ",line[0])
            continue
