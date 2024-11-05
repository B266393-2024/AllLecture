# -*- coding: utf-8 -*-
# 输入的 DNA 序列列表
input_seqs = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

# 对于每一个序列，创建一个索引范围列表
for_range = list(range(0, len(input_seqs)))

# 外层循环：遍历每一个序列，将其作为第一个序列（first_query）进行比较
for Xaxis_item in for_range:
    first_query = list(input_seqs[Xaxis_item])  # 将当前序列转换成字符列表
    
    # 内层循环：将当前序列与每一个序列进行比较（包括它本身）
    for Yaxis_item in for_range:
        distance = 0  # 初始化相似的碱基计数
        other_query = list(input_seqs[Yaxis_item])  # 获取要比较的另一个序列
        
        # 比较两个序列中的每个碱基
        for base in range(0, len(first_query)):
            # 输出当前索引和对应碱基的比较
            print("Index " + str(base) + ": " + str(first_query[base]) + "," + str(other_query[base]) + "...")
            
            # 如果两个序列在同一位置的碱基相同，增加相似计数
            if first_query[base] == other_query[base]:
                distance += 1
        
        # 如果两个序列不相同，输出相似度信息
        if input_seqs[Xaxis_item] != input_seqs[Yaxis_item]:
            # 输出两个序列的相似碱基数量
            print(str(distance) + " identities between " + input_seqs[Xaxis_item] + " and " + input_seqs[Yaxis_item])
            
            # 计算相似度的百分比并输出
            similarity_percent = int(100 * (distance / len(input_seqs[Xaxis_item])))
            print("\t" + str(similarity_percent) + " percent similarity between " + input_seqs[Xaxis_item] + " and " + input_seqs[Yaxis_item])
