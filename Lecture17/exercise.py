import subprocess, os, sys
import pandas as pd
df = pd.read_csv('eukaryotes.txt',sep="\t")




#how many fungal species have genomes bigger than 100Mb? What are their names?
#有多少真菌物种的基因组大于 100Mb？他们的名字是什么？
#数量
df[(df['Size (Mb)'] > 100) & (df['Group'] == 'fungal')].values_counts()
len( df[ (df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100) ] )
len(df[df.apply(lambda x : x['Group'] == 'Fungi' and x['Size (Mb)'] > 100, axis=1)])
#名字
big_fungi = df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)]
list(big_fungi['#Organism/Name'])
sorted(list(big_fungi['#Organism/Name']))

# How many genomes of each major group (plants, animals, fungi and protists) have been sequenced, and how many unique organisms?
# 每个主要类群（植物、动物、真菌和原生生物）有多少个基因组被测序，以及有多少个独特的生物？
for Group in ['Plants', 'Animals', 'Fungi', 'Protists']:
    count = len(df[df['Group'] == Group])
    count_unique = len(set(df[df['Group'] == Group]['#Organism/Name']))
    count_unique = len(df[df['Group'] == Group].drop_duplicates('#Organism/Name'))
    print("{} genomes for {} ({} unique)".format(count, Group, count_unique))

# Which Heliconius species genomes have been sequenced, and how many scaffolds is each assembly in?
# 已经对哪些 Heliconius 物种基因组进行了测序，每个组装在多少个支架中？  
hel = df[df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'), axis=1)]
hel[ ['#Organism/Name', 'Scaffolds'] ]

# Which center has sequenced the most plant genomes?
# 哪个中心对植物基因组进行了最多的测序？
df[df['Group'] == 'Plants']['Center'].value_counts().head()

# Which center has sequenced the most insect genomes?
# 哪个中心对昆虫基因组进行了最多的测序？
df[df['SubGroup'] == 'Insects']['Center'].value_counts().head()

# Add a column giving the number of proteins per gene
# 添加一列，给出每个基因的蛋白质数量
df['Proteins'] / df['Genes']
df['Proteins per gene'] = df['Proteins'] / df['Genes']
df[ ['#Organism/Name', 'Group', 'Proteins per gene'] ].head()

# Which genomes have at least 10% more proteins than genes?
# 哪些基因组的蛋白质比基因至少多 10%？
df[df['Proteins per gene'] >= 1.1][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ].head()
df[df['Proteins per gene'] >= 1.1][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ]
len(df[ df['Proteins per gene'] >= 1.1])

# More than 2.5 proteins per gene...
# 每个基因超过 2.5 种蛋白质...
df[df['Proteins per gene'] >= 2.5][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ]