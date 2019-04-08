import pandas as pd

#The TSV file you wish to drop columns from
file = 'data/CCES16_Common_OUTPUT_Feb2018_VV.tab.tsv'
print("Reading in ",  file)
df = pd.read_csv(file, sep='\t')

headers = list(df)
#Name of columns you wish to keep
cols_to_keep = ['V101', 'commonweight_vv']
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
