import os
import json
import matplotlib.pyplot as plt

# 文件夹路径
folder_path = 'images'

# 初始化类别计数器
class_counter = {}

# 遍历文件夹中的所有.json文件
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        with open(os.path.join(folder_path, filename), 'r') as f:
            data = json.load(f)
            # 遍历文件中的每一个shape
            for shape in data['shapes']:
                # 获取类别
                class_name = shape['label']
                # 更新类别计数器
                if class_name in class_counter:
                    class_counter[class_name] += 1
                else:
                    class_counter[class_name] = 1

# 打印类别计数
for class_name, count in class_counter.items():
    print(f'Class {class_name}: {count} instances')

# 可视化
labels = class_counter.keys()
sizes = class_counter.values()

# 自定义标签函数
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.1f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.pie(sizes, labels=labels, autopct=make_autopct(sizes))
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()