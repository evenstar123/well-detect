import os
from PIL import Image

# 设置目录路径
directory = '/data/good'

# 阈值
width_threshold = 500
height_threshold = 500

def is_low_resolution(image_path, width_threshold, height_threshold):
    with Image.open(image_path) as img:
        width, height = img.size
        return width < width_threshold or height < height_threshold

for filename in os.listdir(directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        image_path = os.path.join(directory, filename)
        if is_low_resolution(image_path, width_threshold, height_threshold):
            print(f"删除低分辨率图片：{image_path}")
            os.remove(image_path)
        else:
            print(f"保留图片：{image_path}")

print("操作完成。")
