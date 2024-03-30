import os
import argparse

# 获取命令行参数
directory = 'data/uncovered'
number_to_delete = 440

# 检查目录是否存在
if not os.path.isdir(directory):
    print(f"错误：目录 '{directory}' 不存在。")
    exit(1)

# 获取目录中的所有图片文件
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
images = [f for f in os.listdir(directory) if f.lower().endswith(image_extensions)]

# 检查是否有足够的图片文件
if number_to_delete > len(images):
    print(f"错误：目录中只有 {len(images)} 个图片文件，无法删除 {number_to_delete} 个。")
    exit(1)

# 删除指定数量的图片文件
for i in range(number_to_delete):
    image_path = os.path.join(directory, images[i])
    os.remove(image_path)
    print(f"已删除：{image_path}")

print(f"已删除 {number_to_delete} 个图片文件。")
