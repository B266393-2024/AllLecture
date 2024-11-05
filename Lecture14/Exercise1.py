# -*- coding: utf-8 -*-
#Print out the gene names for all genes from the speciesDrosophila melanogaster or Drosophila simulans.
with open('data.csv') as data:
    for line in data:
        fields=line.strip().split('\t')
        species = fields[0]  # 物种名称
        sequence = fields[1]  # DNA 序列
        name = fields[2]  # 基因名称
        expression = int(fields[3]) 
        print(name)

#Print out the gene names for all genes that are between 90 and 110 bases long.
        
        if 90<=len(sequence)<=110:
            print (name)
    
#Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200.
        
        acount=sequence.count('a')
        tcount=sequence.count('t')
        seqcount=len(sequence)
        if (acount+tcount)/seqcount<0.5 and expression>200:
            print(name)
    
#Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster.
        
        if (name.startswith('k') or name.startswith('h')) and species != 'Drosophila melanogaster':
            print(name)