# -*- coding: utf-8 -*-
# ����� DNA �����б�
input_seqs = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

# ����ÿһ�����У�����һ��������Χ�б�
for_range = list(range(0, len(input_seqs)))

# ���ѭ��������ÿһ�����У�������Ϊ��һ�����У�first_query�����бȽ�
for Xaxis_item in for_range:
    first_query = list(input_seqs[Xaxis_item])  # ����ǰ����ת�����ַ��б�
    
    # �ڲ�ѭ��������ǰ������ÿһ�����н��бȽϣ�����������
    for Yaxis_item in for_range:
        distance = 0  # ��ʼ�����Ƶļ������
        other_query = list(input_seqs[Yaxis_item])  # ��ȡҪ�Ƚϵ���һ������
        
        # �Ƚ����������е�ÿ�����
        for base in range(0, len(first_query)):
            # �����ǰ�����Ͷ�Ӧ����ıȽ�
            print("Index " + str(base) + ": " + str(first_query[base]) + "," + str(other_query[base]) + "...")
            
            # �������������ͬһλ�õļ����ͬ���������Ƽ���
            if first_query[base] == other_query[base]:
                distance += 1
        
        # ����������в���ͬ��������ƶ���Ϣ
        if input_seqs[Xaxis_item] != input_seqs[Yaxis_item]:
            # ����������е����Ƽ������
            print(str(distance) + " identities between " + input_seqs[Xaxis_item] + " and " + input_seqs[Yaxis_item])
            
            # �������ƶȵİٷֱȲ����
            similarity_percent = int(100 * (distance / len(input_seqs[Xaxis_item])))
            print("\t" + str(similarity_percent) + " percent similarity between " + input_seqs[Xaxis_item] + " and " + input_seqs[Yaxis_item])
