import os

def check_and_delete_files(directory):
    jpg_count = 0
    json_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg"):
                jpg_path = os.path.join(root, file)
                json_path = os.path.splitext(jpg_path)[0] + ".json"
                if not os.path.exists(json_path):
                    os.remove(jpg_path)
                    print(f"Deleted {jpg_path}")
                jpg_count += 1
            elif file.endswith(".json"):
                json_path = os.path.join(root, file)
                jpg_path = os.path.splitext(json_path)[0] + ".jpg"
                if not os.path.exists(jpg_path):
                    os.remove(json_path)
                    print(f"Deleted {json_path}")
                json_count += 1
    print(f"Total .jpg files: {jpg_count}")
    print(f"Total .json files: {json_count}")
print("ok")
# 指定要遍历的目录
top_directory = "./"
check_and_delete_files(top_directory)