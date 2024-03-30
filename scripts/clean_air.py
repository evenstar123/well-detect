import os
import json
import time

def delete_empty_label_json(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            json_path = os.path.join(folder_path, filename)
            
            # 读取JSON文件
            try:
                with open(json_path, 'r') as json_file:
                    data = json.load(json_file)
                    
                    # 检查JSON中是否有标签
                    if 'shapes' not in data or len(data['shapes']) == 0:
                        # 没有标签的话删除文件
                        try:
                            json_file.close()
                            os.unlink(json_path)
                            print(f"已删除没有标签的JSON文件: {json_path}")
                        except Exception as e:
                            print(f"删除文件时发生错误: {json_path}")
                            print(f"错误信息: {e}")
            except Exception as e:
                print(f"处理文件时发生错误: {json_path}")
                print(f"错误信息: {e}")

# 指定数据集文件夹路径
dataset_folder = "images"
print("ok")
# 调用函数删除没有标签的JSON文件
delete_empty_label_json(dataset_folder)
