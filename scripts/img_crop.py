import os
from ultralytics import YOLO
from PIL import Image

# 模型路径
model_path = r'result\best.pt'
# 图片目录路径
images_dir = r'testdata'
# 输出目录路径
output_dir = r'output'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 加载模型
model = YOLO(model_path)

# 获取图片目录下所有的图片文件
image_files = [os.path.join(images_dir, f) for f in os.listdir(images_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# 对每个图片文件进行检测
for image_file in image_files:
    # 检测图片
    results = model(image_file)

    # 遍历检测结果
    for r in results:
        # 遍历每个预测框
        for box in r.boxes:
            # 获取类别名
            class_name = box.cls.name
            # 获取置信度
            confidence = box.conf

            # 只处理置信度高于某个阈值的预测框
            if confidence > 0.5:
                # 创建类别名对应的输出目录
                class_output_dir = os.path.join(output_dir, class_name)
                if not os.path.exists(class_output_dir):
                    os.makedirs(class_output_dir)

                # 读取原始图片
                im = Image.open(image_file)
                # 获取预测框的坐标
                x1, y1, x2, y2 = box.xyxy.squeeze().tolist()
                # 截取目标
                cropped = im.crop((x1, y1, x2, y2))
                # 保存截取的目标
                cropped.save(os.path.join(class_output_dir, f'{os.path.basename(image_file).split(".")[0]}_{class_name}.jpg'))
