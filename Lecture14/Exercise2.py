# 创建一个虚拟序列
sequencein = "atatatatatcgcgtatatatacgactatatgcattaattatagcatatcgatatatatatcgatattatatcgcattatacgcgcgtaattatatc"

# 生成一个较小的 k-mer 集合
possible_kmer_sizes = list(range(2, 7))
kmerfound_minimum = 3

# 循环遍历每一个可能的 k-mer 大小
for window in possible_kmer_sizes:
    kmersfound = []
    kmerrange = list(range(0, len(sequencein)))
    
    # 提取所有起始位置的 k-mer
    for startingbase in kmerrange:
        if (startingbase + window) < len(sequencein) + 1:
            seqout = sequencein[startingbase:startingbase + window]
            kmersfound.append(seqout)
    
    # 去除冗余的 k-mer 并统计出现频率
    nonredundantset = list(set(kmersfound))
    for kmerfrequencies in nonredundantset:
        if kmersfound.count(kmerfrequencies) > kmerfound_minimum:
            print("Lots! " + str(kmerfrequencies) + " " + str(kmersfound.count(kmerfrequencies)))
        else:
            print(str(kmerfrequencies) + " " + str(kmersfound.count(kmerfrequencies)))
