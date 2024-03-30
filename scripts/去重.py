import os
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict

# 定义计算文件MD5哈希值的函数
def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# 定义删除重复文件及其对应JSON文件的函数
def delete_duplicates(directory):
    # 创建一个字典来存储哈希值和对应的文件路径
    md5_dict = defaultdict(list)
    json_files = {}

    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # 只处理图片文件
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            md5_hash = calculate_md5(file_path)
            md5_dict[md5_hash].append(file_path)
        # 处理JSON文件
        elif filename.lower().endswith('.json'):
            base_name = os.path.splitext(filename)[0]
            json_files[base_name] = file_path

    # 删除重复的图片文件和对应的JSON文件
    with ThreadPoolExecutor() as executor:
        for md5_hash, files in md5_dict.items():
            if len(files) > 1:
                # 保留一个文件，删除其他重复文件
                for file_path in files[1:]:
                    # 记录重复文件的信息
                    duplicate_info = f"文件 {file_path} 与 {files[0]} 内容重复，即将被删除。"
                    print(duplicate_info)
                    executor.submit(os.remove, file_path)
                    # 删除对应的JSON文件
                    json_filename = os.path.basename(file_path).split('.')[0] + '.json'
                    json_file_path = os.path.join(directory, json_filename)
                    if json_filename in json_files:
                        executor.submit(os.remove, json_file_path)
                        print(f"删除对应的JSON文件：{json_file_path}")

# 定义要检查的目录
directory = 'merged_dataset/'

# 主函数
if __name__ == "__main__":
    delete_duplicates(directory)
