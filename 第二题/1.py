import numpy as np
import os
import re
path = ('data')



file_list = os.listdir(path)


# 标签个数
count = 0
# 标签总面积面积
sum_area = 0
# 面积列表
area = []
# 最大面积
max_area = 0
tmp = 1
for i in file_list:
    file = 'data/' + i
    with open(file, 'r') as f:
        info = f.read()
        value = re.compile("<object>([\s\S]*?)</object>").findall(info, re.S)
        count += len(value)
        for k in value:
            k = k.replace('\n', '').replace('\t', '')
            # name = re.compile("<name>(.*?)</name>").findall(k)[0]
            n = re.compile('<bndbox>(.*?)</bndbox>').findall(k, re.S)[0]
            num = re.compile('(\d+)').findall(n)
            s = (int(num[2]) - int(num[0])) * (int(num[3]) - int(num[1]))
            if max_area == 0:
                max_area = s
            elif s > max_area:
                max_area, s = s, max_area
            area.append(s)



with open('1.txt', 'w') as f:
    f.write('总数为：{}\n'.format(count))
    f.write('平均面积为：{}\n'.format(sum(area)/count))
    f.write('最大面积为：{}\n'.format(max_area))
    f.write('面积的方差为：{}\n'.format(np.var(area)))