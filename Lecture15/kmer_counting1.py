def kmer_counting(DNA,kmersize,minfrequency):
    kmer_found=[]
    DNA_length=len(DNA)
    kmer_range=list(range(0,DNA_length))
    for start_base in kmer_range:
        if (start_base+kmersize) <= DNA_length:
            kmer = DNA[start_base:start_base + kmersize]
            kmer_found.append(kmer)
    result=[]
    for kmer in set(kmer_found):
        kmer_count=kmer_found.count(kmer)
        if kmer_count > minfrequency:
            result.append(kmer)
    return result
            
assert kmer_counting(DNA="ATGCATCATG",kmersize=2,minfrequency=2)==['AT']