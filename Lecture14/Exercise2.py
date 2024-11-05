# ����һ����������
sequencein = "atatatatatcgcgtatatatacgactatatgcattaattatagcatatcgatatatatatcgatattatatcgcattatacgcgcgtaattatatc"

# ����һ����С�� k-mer ����
possible_kmer_sizes = list(range(2, 7))
kmerfound_minimum = 3

# ѭ������ÿһ�����ܵ� k-mer ��С
for window in possible_kmer_sizes:
    kmersfound = []
    kmerrange = list(range(0, len(sequencein)))
    
    # ��ȡ������ʼλ�õ� k-mer
    for startingbase in kmerrange:
        if (startingbase + window) < len(sequencein) + 1:
            seqout = sequencein[startingbase:startingbase + window]
            kmersfound.append(seqout)
    
    # ȥ������� k-mer ��ͳ�Ƴ���Ƶ��
    nonredundantset = list(set(kmersfound))
    for kmerfrequencies in nonredundantset:
        if kmersfound.count(kmerfrequencies) > kmerfound_minimum:
            print("Lots! " + str(kmerfrequencies) + " " + str(kmersfound.count(kmerfrequencies)))
        else:
            print(str(kmerfrequencies) + " " + str(kmersfound.count(kmerfrequencies)))
