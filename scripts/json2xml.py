import os
import xml.dom
 
import numpy as np
import codecs
import json
import glob
import cv2
import shutil
 
# 1.标签路径
labelme_path = r"images"  # 原始json、jpg标注数据路径,需要更换成自己的数据集名称
saved_path = r"data\Annotations"  # 保存路径
 
# 2.获取待处理文件
files = glob.glob("%s/*.json" % (labelme_path))
 
# 3.读取标注信息并写入 xml
for json_filename in files:
     json_file = json.load(open(json_filename, "r", encoding="utf-8"))
     i = 0
     # 图像名字
     img_name = json_filename.replace(".json", ".jpg")
     height, width, channels = cv2.imread(img_name).shape
     # xml名字
     xmlName = os.path.join(saved_path, json_filename.split("\\")[-1].replace(".json", ".xml"))
 
     with codecs.open(xmlName, "w", "utf-8") as xml:
        print(2)
        xml.write('<annotation>\n')
        xml.write('\t<folder>' + 'jpg' + '</folder>\n')
        xml.write('\t<filename>' + img_name + '</filename>\n')
        # -------------------------------------------------
        xml.write('\t<source>\n')
        xml.write('\t\t<database>hulan</database>\n')
 
        # --------------------------------------------------
        xml.write('\t</source>\n')
        # -----------------------------------------------------------
        xml.write('\t<size>\n')
        xml.write('\t\t<width>' + str(width) + '</width>\n')
        xml.write('\t\t<height>' + str(height) + '</height>\n')
        xml.write('\t\t<depth>' + str(channels) + '</depth>\n')
        # ------------------------------------------------
        xml.write('\t</size>\n')
        xml.write('\t\t<segmented>0</segmented>\n')
 
        # 节点判断
        for multi in json_file["shapes"]:
            points = np.array(multi["points"])
            xmin = min(points[:, 0])
            xmax = max(points[:, 0])
            ymin = min(points[:, 1])
            ymax = max(points[:, 1])
            label = multi["label"]
            if xmax <= xmin:
                pass
            elif ymax <= ymin:
                pass
            else:
                xml.write('\t<object>\n')
                xml.write('\t\t<name>' + json_file["shapes"][i]["label"] + '</name>\n')
                xml.write('\t\t<pose>Unspecified</pose>\n')
                xml.write('\t\t<truncated>0</truncated>\n')
                xml.write('\t\t<difficult>0</difficult>\n')
                xml.write('\t\t<bndbox>\n')
                xml.write('\t\t\t<xmin>' + str(xmin) + '</xmin>\n')
                xml.write('\t\t\t<ymin>' + str(ymin) + '</ymin>\n')
                xml.write('\t\t\t<xmax>' + str(xmax) + '</xmax>\n')
                xml.write('\t\t\t<ymax>' + str(ymax) + '</ymax>\n')
                xml.write('\t\t</bndbox>\n')
                xml.write('\t</object>\n')
                print(json_filename, xmin, ymin, xmax, ymax, label)
                i = i + 1
        xml.write('</annotation>')