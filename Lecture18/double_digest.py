import re
dna = open('long_dna.txt').read().rstrip('\n')
BpsmI='A[GATC]TAAT'
print('BpsmI cuts at:',BpsmI) 
for matching in re.finditer(BpsmI, dna):
    print(matching.start()+3) 
    
last_cut = 0
findnum=0
for matching in re.finditer(BpsmI, dna):
    findnum += 1
    cut_position = matching.start() + 3
# Distance from the current cut site to the previous one
    fragment_size = cut_position - last_cut
    print('Fragment size is ' + str(fragment_size))
    last_cut = cut_position
# We also have to remember the last fragment, from the last cut to the end:
    if findnum == len(list(re.finditer(BpsmI, dna))) :
       fragment_size = len(dna) - last_cut
       print('Fragment size is ' + str(fragment_size))
       
#ʹ���������ʽ�� DNA �������ҵ����з��� BpsmI �� BpsmII �и�λ������С�
#�����ÿ���и�λ���λ�ã�������Щλ�ô洢�� all_cuts �б��С�
#��󣬽������и�λ�ð���������׼����һ�������и���Ƭ�δ�С��
BpsmI='A[GATC]TAAT'
BpsmII='GC[AG][AT]TG'
all_cuts = []
for match in re.finditer(BpsmI, dna): 
    all_cuts.append(match.start() + 3) 
for match in re.finditer(BpsmII, dna): 
    all_cuts.append(match.start() + 4)
print(all_cuts)
all_cuts.sort()

#���㲢��ӡ�� DNA �����и���Ƭ�εĴ�С
last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
    last_cut = cut_position
fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )

#��DNA�����ַ���������
fragment_sequences = {}
last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
    fragment_sequences['Fragment'+str(counter)] = dna[last_cut:cut_position]
    print(fragment_sequences['Fragment'+str(counter)])
    fragends = dna[last_cut:cut_position][0:6] + '...' + dna[last_cut:cut_position][-6:]
    print('Fragment '+str(counter)+ ' has ends: '+fragends+'\n')
    last_cut = cut_position
fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )
fragment_sequences['Fragment'+str(counter)] = dna[last_cut:]
print(fragment_sequences['Fragment'+str(counter)])
fragends = dna[last_cut:][0:6] + '...' + dna[last_cut:][-6:]
print('Fragment has ends: '+fragends)
print(('\n########\n').join(list(fragment_sequences.values())))