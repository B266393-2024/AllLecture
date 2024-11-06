def find_my_kmers(dna,ksize=2,minkfreq=3) :
   if ksize > len(dna) :
     return "Sorry, your kmer length is longer than your DNA (" + str(len(dna)) +" bases)." 
   if ksize < 2 or ksize > 50 :
     return "Sorry, inappropriate kmer length, only 2 to 50 accepted here."
   print("Processing sequence of length",len(dna),"for kmers longer than",ksize,"and frequency greater than",minkfreq)
   kmersfound = []
   kmerstarts = list(range(0,len(dna)))
   for base in kmerstarts:
       if (base+ksize) < len(dna)+1:
           seqout = (dna)[base:base+ksize]
           kmersfound = kmersfound + [seqout] 
   nrset = list(set(kmersfound))
   returnstuff = []
   for kfreqfind in nrset:
       if kmersfound.count(kfreqfind) > minkfreq :
           returnstuff.append(kfreqfind.upper()+": "+str(kmersfound.count(kfreqfind)))
   return print(returnstuff)