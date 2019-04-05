import pandas as pd

#The TSV file you wish to drop columns from
file = 'data/CCES16_Common_OUTPUT_Feb2018_VV.tab.tsv'
print("Reading in ",  file)
df = pd.read_csv(file, sep='\t')

#Name of columns you wish to drop
cols_to_drop = ['V101', 'commonweight_vv']
if cols_to_drop:
    print("Dropping the following columns: ", cols_to_drop)
    for col in cols_to_drop:
        df.drop(col, axis=1, inplace=True)
else:
    print("Didn't drop anything")

#print(df)

#Files to save our TSV to
outputFile = 'data/output.tsv'
print("Saving as ", outputFile)
df.to_csv('data/output.tsv',sep='\t')
