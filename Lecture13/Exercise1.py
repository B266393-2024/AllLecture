input_txt_contents=open('input.txt').read().replace('ATTCGATTATAAGC','').split()
with open('cleaned_sequences.txt','w') as cleanseqs:
    for cleanones in input_txt_contents:
        cleanseqs.write(cleanones + '\n')
        cleanseqs.write(str(len(cleanones)) + '\n')
with open('cleaned_sequences.txt', 'r') as cleanseqs:
    print(cleanseqs.read())
