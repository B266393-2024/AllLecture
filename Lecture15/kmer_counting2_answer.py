# 定义一个函数来查找给定DNA序列中的k-mers
def new_find_my_kmers(dna, ksize=2, minkfreq=2):
    kmersfound = []  # 初始化列表来存储找到的所有k-mers
    kmerstarts = list(range(0, len(dna)))  # 创建一个列表，包含DNA序列中所有可能的起始位置

    # 遍历序列中每一个可能的k-mer起始位置
    for base in kmerstarts:
        if (base + ksize) < len(dna) + 1:  # 检查k-mer是否会超出序列的长度
            seqout = (dna)[base:base + ksize]  # 提取k-mer
            kmersfound = kmersfound + [seqout]  # 将k-mer添加到kmersfound列表中

    nrset = list(set(kmersfound))  # 通过集合去重，得到唯一的k-mers列表
    returnstuff = []  # 初始化列表，用于存储符合条件的k-mers和频率

    # 遍历每个唯一k-mer，检查其频率是否符合要求
    for kfreqfind in nrset:
        if kmersfound.count(kfreqfind) > minkfreq:  # 频率大于指定的最小值
            returnstuff.append(kfreqfind.upper() + ": " + str(kmersfound.count(kfreqfind)))  # 将k-mer和频率添加到returnstuff

    return returnstuff  # 返回符合条件的k-mers和其频率


# 询问用户输入DNA序列，并将其转换为大写
inputdna = input("What is your sequence?\n\t").upper()

# 如果用户输入了DNA序列，继续进行后续处理
if inputdna:
    # 获取用户输入的k-mer大小，如果未指定则默认为2
    inputksize = int(input("What kmer size shall I use?\n\t") or 2)

    # 检查k-mer大小是否合理，如果不合理则重置为2并提示
    if (inputksize < 2 or inputksize >= len(inputdna) or inputksize > 50):
        inputksize = 2
        print("Inappropriate value chosen, resetting to 2\n\t")

    # 获取用户输入的最小频率，如果未指定则默认为2
    inputminkfreq = int(input("What minimum frequency shall I use?\n\t") or 2)

    # 输出确认信息
    print("Thanks!  Processing:\n" + inputdna + "\n for a kmersize of " +
          str(inputksize) + ",\n reporting frequencies greater than " +
          str(inputminkfreq) + "\n")

    # 调用函数，找出符合条件的k-mers并对结果排序
    outputstuff = new_find_my_kmers(dna=inputdna, ksize=inputksize, minkfreq=inputminkfreq)
    outputstuff.sort()

    # 定义输出文件名，包含k-mer大小和最小频率信息
    myfilename = "kmerouts" + "_KMER" + str(inputksize) + "_MIN" + str(inputminkfreq) + ".txt"
    outputfilepipe = open(myfilename, "w")  # 打开文件进行写入

    # 检查是否有符合条件的k-mers
    if len(outputstuff) == 0:
        print("No kmers met the criteria, so no outputs to file!\n")
        outputfilepipe.close()  # 如果没有符合条件的k-mers，则关闭文件
    else:
        # 输出结果到屏幕
        print("Results:\n")
        print(outputstuff)

        # 将结果写入文件
        outputfilepipe.write("### Kmer analysis\n#SQ " + str(inputdna) +
                             "\n#KMER " + str(inputksize) +
                             "\n#MIN " + str(inputminkfreq) + "\n")
        for freqseq in outputstuff:
            outputfilepipe.write(freqseq + "\n")
        outputfilepipe.write("\n")
        outputfilepipe.close()  # 写入完成后关闭文件

        # 显示输出文件的内容
        print("\n\nContents of the output:\n")
        syscmd = "cat " + myfilename
        os.system(syscmd)

else:
    # 如果未输入DNA序列，提示错误信息
    print("Sorry, really can't do any of this without a sequence!\n")
