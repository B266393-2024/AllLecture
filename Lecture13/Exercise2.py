genomic_dna2 = open('genomic_dna2.txt').read().upper()
exons_v3 = open('exons.txt').read().rsplit()
counter=0
with open('Exercise_coding_seqence.fasta','w') as fullcoding:
    fullcoding.write('>Lecture13_exercise2_codingseq\n')
    for exons in exons_v3:
        counter+=1
        startexon=int(exons.split(',')[0])-1
        endexon=int(exons.split(',')[1])
        exonwanted=genomic_dna2[startexon:endexon]
        fullcoding.write(exonwanted)
        regionsummary = 'Exon'+str(counter)+' '+str(exons)+' runs from index position '+str(startexon)+' upto but not including '+str(endexon)+ '.'
        print(regionsummary,'\n\t',exonwanted)

