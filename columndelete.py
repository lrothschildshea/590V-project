import pandas as pd
import tarfile
import sys

#The TSV file you wish to drop columns from
file = 'data/CCES16_Common_OUTPUT_Feb2018_VV'

import os.path
if not (os.path.isfile(file+'.tab.tsv') or os.path.isfile(file+'.tab')):
    tar = tarfile.open('data.tar.gz', "r:gz")
    tar.extractall()
    tar.close()

if os.path.isfile(file+'.tab.tsv'):
    path = '.tab.tsv'
elif os.path.isfile(file+'.tab'):
    path = '.tab'
else:
    sys.exit("Missing CCES file or not in data folder")

print("Reading in ",  file+path)
df = pd.read_csv(file+path, sep='\t')

headers = list(df)
#Name of columns you wish to keep
cols_to_keep = ['inputstate', 'countyfips', 'countyname', 'birthyr', 'gender', 'sexuality', 'trans', 'educ', 'race', 'employ', 'marstat', 'pid3', 'religpew', 'faminc', 'CC16_326', 'CC16_410a']
if cols_to_keep:
    print("Keeping the following columns: ", cols_to_keep)
    for col in headers:
        if col not in cols_to_keep:
            df.drop(col, axis=1, inplace=True)
else:
    print("Not dropping everything")

#print(df)

#Files to save our TSV to
outputFile = 'data/output.tsv'
print("Saving as ", outputFile)
df.to_csv('data/output.tsv',sep='\t')
