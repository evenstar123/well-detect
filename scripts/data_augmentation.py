import os
import json
from PIL import Image, ImageEnhance, ImageOps
import base64
import numpy as np
import io

# 设置输入和输出目录
input_dir = './input'  # 原始图片和JSON文件的目录
output_dir = './output'  # 增强后图片和JSON文件的输出目录

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 获取所有图片文件
image_files = [f for f in os.listdir(input_dir) if f.endswith('.jpg')]

# 设置要生成的图片数量
num_new_images = 100

# 生成新图片
for i in range(num_new_images):
    # 随机选择一张图片
    image_file = np.random.choice(image_files)
    image_path = os.path.join(input_dir, image_file)
    json_file = os.path.splitext(image_file)[0] + '.json'
    json_path = os.path.join(input_dir, json_file)

    # 读取图片和JSON文件
    image = Image.open(image_path)
    with open(json_path, 'r') as f:
        json_data = json.load(f)

    # 随机选择一种增强方法
    enhancement = np.random.choice(['contrast', 'brightness', 'grayscale'])

    if enhancement == 'contrast':
        # 随机调整对比度
        enhancer = ImageEnhance.Contrast(image)
        factor = np.random.uniform(0.5, 1.5)  # 对比度因子
        enhanced_image = enhancer.enhance(factor)
    elif enhancement == 'brightness':
        # 随机调整亮度
        enhancer = ImageEnhance.Brightness(image)
        factor = np.random.uniform(0.5, 1.5)  # 亮度因子
        enhanced_image = enhancer.enhance(factor)
    elif enhancement == 'grayscale':
        # 转换为灰度图像
        enhanced_image = ImageOps.grayscale(image)

    # 保存增强后的图片
    new_image_name = f'enhanced_{i}.jpg'
    new_image_path = os.path.join(output_dir, new_image_name)
    enhanced_image.save(new_image_path)

    # 更新JSON文件中的imagePath和imageData
    json_data['imagePath'] = new_image_name
    with io.BytesIO() as buf:
        enhanced_image.save(buf, format='JPEG')
        b64_image = base64.b64encode(buf.getvalue()).decode('utf-8')
    json_data['imageData'] = b64_image

    # 保存新的JSON文件
    new_json_path = os.path.join(output_dir, os.path.splitext(new_image_name)[0] + '.json')
    with open(new_json_path, 'w') as f:
        json.dump(json_data, f, indent=2)

print(f'Generated {num_new_images} new images and JSON files in {output_dir}')
