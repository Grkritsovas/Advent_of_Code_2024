import sys

input_data = sys.argv[-1]
f = open(input_data, 'r')
lines = f.read().split('\n')
id_list_1 = []
id_list_2 = []

for line in lines:
    try:
        id_1, id_2 = line.split()
        id_list_1.append(int(id_1))
        id_list_2.append(int(id_2))
    except:
        pass

id_list_1.sort()
id_list_2.sort()

diffs = 0

for i in range(len(id_list_1)):
    diffs += abs(id_list_1[i] - id_list_2[i])

print(diffs)

id_set_1 = set(id_list_1)

freq_num = {}

for num in id_list_2:
    if num in id_set_1:
        freq_num[num] = freq_num.get(num, 0) + 1

similarity_score = 0

for num, freq in freq_num.items():
    similarity_score += num*freq

print(similarity_score)