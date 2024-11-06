# ����һ�����������Ҹ���DNA�����е�k-mers
def new_find_my_kmers(dna, ksize=2, minkfreq=2):
    kmersfound = []  # ��ʼ���б����洢�ҵ�������k-mers
    kmerstarts = list(range(0, len(dna)))  # ����һ���б�����DNA���������п��ܵ���ʼλ��

    # ����������ÿһ�����ܵ�k-mer��ʼλ��
    for base in kmerstarts:
        if (base + ksize) < len(dna) + 1:  # ���k-mer�Ƿ�ᳬ�����еĳ���
            seqout = (dna)[base:base + ksize]  # ��ȡk-mer
            kmersfound = kmersfound + [seqout]  # ��k-mer��ӵ�kmersfound�б���

    nrset = list(set(kmersfound))  # ͨ������ȥ�أ��õ�Ψһ��k-mers�б�
    returnstuff = []  # ��ʼ���б����ڴ洢����������k-mers��Ƶ��

    # ����ÿ��Ψһk-mer�������Ƶ���Ƿ����Ҫ��
    for kfreqfind in nrset:
        if kmersfound.count(kfreqfind) > minkfreq:  # Ƶ�ʴ���ָ������Сֵ
            returnstuff.append(kfreqfind.upper() + ": " + str(kmersfound.count(kfreqfind)))  # ��k-mer��Ƶ����ӵ�returnstuff

    return returnstuff  # ���ط���������k-mers����Ƶ��


# ѯ���û�����DNA���У�������ת��Ϊ��д
inputdna = input("What is your sequence?\n\t").upper()

# ����û�������DNA���У��������к�������
if inputdna:
    # ��ȡ�û������k-mer��С�����δָ����Ĭ��Ϊ2
    inputksize = int(input("What kmer size shall I use?\n\t") or 2)

    # ���k-mer��С�Ƿ�������������������Ϊ2����ʾ
    if (inputksize < 2 or inputksize >= len(inputdna) or inputksize > 50):
        inputksize = 2
        print("Inappropriate value chosen, resetting to 2\n\t")

    # ��ȡ�û��������СƵ�ʣ����δָ����Ĭ��Ϊ2
    inputminkfreq = int(input("What minimum frequency shall I use?\n\t") or 2)

    # ���ȷ����Ϣ
    print("Thanks!  Processing:\n" + inputdna + "\n for a kmersize of " +
          str(inputksize) + ",\n reporting frequencies greater than " +
          str(inputminkfreq) + "\n")

    # ���ú������ҳ�����������k-mers���Խ������
    outputstuff = new_find_my_kmers(dna=inputdna, ksize=inputksize, minkfreq=inputminkfreq)
    outputstuff.sort()

    # ��������ļ���������k-mer��С����СƵ����Ϣ
    myfilename = "kmerouts" + "_KMER" + str(inputksize) + "_MIN" + str(inputminkfreq) + ".txt"
    outputfilepipe = open(myfilename, "w")  # ���ļ�����д��

    # ����Ƿ��з���������k-mers
    if len(outputstuff) == 0:
        print("No kmers met the criteria, so no outputs to file!\n")
        outputfilepipe.close()  # ���û�з���������k-mers����ر��ļ�
    else:
        # ����������Ļ
        print("Results:\n")
        print(outputstuff)

        # �����д���ļ�
        outputfilepipe.write("### Kmer analysis\n#SQ " + str(inputdna) +
                             "\n#KMER " + str(inputksize) +
                             "\n#MIN " + str(inputminkfreq) + "\n")
        for freqseq in outputstuff:
            outputfilepipe.write(freqseq + "\n")
        outputfilepipe.write("\n")
        outputfilepipe.close()  # д����ɺ�ر��ļ�

        # ��ʾ����ļ�������
        print("\n\nContents of the output:\n")
        syscmd = "cat " + myfilename
        os.system(syscmd)

else:
    # ���δ����DNA���У���ʾ������Ϣ
    print("Sorry, really can't do any of this without a sequence!\n")
