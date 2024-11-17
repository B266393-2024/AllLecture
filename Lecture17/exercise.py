import subprocess, os, sys
import pandas as pd
df = pd.read_csv('eukaryotes.txt',sep="\t")




#how many fungal species have genomes bigger than 100Mb? What are their names?
#�ж���������ֵĻ�������� 100Mb�����ǵ�������ʲô��
#����
df[(df['Size (Mb)'] > 100) & (df['Group'] == 'fungal')].values_counts()
len( df[ (df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100) ] )
len(df[df.apply(lambda x : x['Group'] == 'Fungi' and x['Size (Mb)'] > 100, axis=1)])
#����
big_fungi = df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)]
list(big_fungi['#Organism/Name'])
sorted(list(big_fungi['#Organism/Name']))

# How many genomes of each major group (plants, animals, fungi and protists) have been sequenced, and how many unique organisms?
# ÿ����Ҫ��Ⱥ��ֲ���������ԭ������ж��ٸ������鱻�����Լ��ж��ٸ����ص����
for Group in ['Plants', 'Animals', 'Fungi', 'Protists']:
    count = len(df[df['Group'] == Group])
    count_unique = len(set(df[df['Group'] == Group]['#Organism/Name']))
    count_unique = len(df[df['Group'] == Group].drop_duplicates('#Organism/Name'))
    print("{} genomes for {} ({} unique)".format(count, Group, count_unique))

# Which Heliconius species genomes have been sequenced, and how many scaffolds is each assembly in?
# �Ѿ�����Щ Heliconius ���ֻ���������˲���ÿ����װ�ڶ��ٸ�֧���У�  
hel = df[df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'), axis=1)]
hel[ ['#Organism/Name', 'Scaffolds'] ]

# Which center has sequenced the most plant genomes?
# �ĸ����Ķ�ֲ���������������Ĳ���
df[df['Group'] == 'Plants']['Center'].value_counts().head()

# Which center has sequenced the most insect genomes?
# �ĸ����Ķ������������������Ĳ���
df[df['SubGroup'] == 'Insects']['Center'].value_counts().head()

# Add a column giving the number of proteins per gene
# ���һ�У�����ÿ������ĵ���������
df['Proteins'] / df['Genes']
df['Proteins per gene'] = df['Proteins'] / df['Genes']
df[ ['#Organism/Name', 'Group', 'Proteins per gene'] ].head()

# Which genomes have at least 10% more proteins than genes?
# ��Щ������ĵ����ʱȻ������ٶ� 10%��
df[df['Proteins per gene'] >= 1.1][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ].head()
df[df['Proteins per gene'] >= 1.1][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ]
len(df[ df['Proteins per gene'] >= 1.1])

# More than 2.5 proteins per gene...
# ÿ�����򳬹� 2.5 �ֵ�����...
df[df['Proteins per gene'] >= 2.5][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ]