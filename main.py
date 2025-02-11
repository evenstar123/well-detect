# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.0UI界面设计.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sys
import multiprocessing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

from PIL import Image

from ultralytics import YOLO
from sia_classifier import calculate_similarity, calculate_probabilities, plot_probabilities



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1393, 867)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(220, 650, 831, 171))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 801, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1070, 280, 301, 321))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 35, 111, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 75, 111, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(160, 80, 121, 31))
        self.label_7.setObjectName("label_7")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 160, 261, 141))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 61, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setGeometry(QtCore.QRect(150, 20, 54, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(10, 80, 61, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setGeometry(QtCore.QRect(150, 80, 54, 31))
        self.label_11.setObjectName("label_11")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_6.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_7.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_8.setGeometry(QtCore.QRect(10, 110, 111, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_9.setGeometry(QtCore.QRect(150, 110, 111, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_10.setGeometry(QtCore.QRect(20, 110, 131, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_11.setGeometry(QtCore.QRect(130, 40, 111, 31))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_12.setGeometry(QtCore.QRect(170, 110, 121, 31))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 390, 201, 271))
        self.groupBox_3.setObjectName("groupBox_3")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox.setGeometry(QtCore.QRect(150, 30, 42, 31))
        self.spinBox.setObjectName("spinBox")
        self.label_0 = QtWidgets.QLabel(self.groupBox_3)
        self.label_0.setGeometry(QtCore.QRect(0, 30, 141, 31))
        self.label_0.setObjectName("label_0")

        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(106, 70, 91, 31))
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(6)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_1 = QtWidgets.QLabel(self.groupBox_3)
        self.label_1.setGeometry(QtCore.QRect(0, 70, 111, 31))
        self.label_1.setObjectName("label_1")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox.setGeometry(QtCore.QRect(130, 110, 71, 31))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(0, 150, 121, 31))
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(130, 150, 71, 31))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(0, 180, 201, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(0, 220, 201, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 201, 371))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_0 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_0.setObjectName("pushButton_0")
        self.verticalLayout.addWidget(self.pushButton_0)
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(1070, 630, 301, 191))
        self.groupBox_5.setObjectName("groupBox_5")
        self.image_label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.image_label_2.setGeometry(QtCore.QRect(10, 20, 281, 161))
        self.image_label_2.setText("")
        self.image_label_2.setObjectName("image_label_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 670, 201, 151))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(250, 610, 801, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1043, 40, 31, 781))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(210, 40, 20, 781))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.image_label_0 = QtWidgets.QLabel(self.centralwidget)
        self.image_label_0.setGeometry(QtCore.QRect(230, 40, 821, 561))
        self.image_label_0.setText("")
        self.image_label_0.setObjectName("image_label_0")
                # 设置边框样式
        border_style = "border: 1px solid black;"  # 边框宽度为1像素，颜色为黑色

        # 应用样式到控件
        self.image_label_0.setStyleSheet(border_style)

        self.image_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.image_label_1.setGeometry(QtCore.QRect(1070, 40, 311, 231))
        self.image_label_1.setText("")
        self.image_label_1.setObjectName("image_label_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1393, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.pushButton_0.clicked.connect(self.open_image)

        self.pushButton_1.clicked.connect(self.batch_detect)
        self.pushButton_2.clicked.connect(self.save_image)
        self.pushButton_3.clicked.connect(self.quit_app)
        self.checkBox.stateChanged.connect(self.toggleExtraCode)
        #self.spinBox.valueChanged.connect(self.open_image)
        #设置默认参数
        self.spinBox.setValue(1)
        self.doubleSpinBox.setValue(0.25)
        self.doubleSpinBox_2.setValue(0.45)
        self.comboBox.setCurrentIndex(0)


        self.timer = QTimer()
        self.timer.setInterval(2)#
        self.timer.timeout.connect(self.update_progress)


        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "井盖隐患识别系统v2.0"))
        self.groupBox.setTitle(_translate("MainWindow", "检测目录"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "文件路径"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "类别ID"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "置信度"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "坐标位置"))
        self.groupBox_2.setTitle(_translate("MainWindow", "检测结果"))
        self.label_5.setText(_translate("MainWindow", "目标总数："))
        self.label_6.setText(_translate("MainWindow", "所属类别："))
        self.label_7.setText(_translate("MainWindow", "置信度："))
        self.groupBox_6.setTitle(_translate("MainWindow", "目标位置："))
        self.label_8.setText(_translate("MainWindow", "xmin："))
        self.label_9.setText(_translate("MainWindow", "xmax："))
        self.label_10.setText(_translate("MainWindow", "ymin："))
        self.label_11.setText(_translate("MainWindow", "ymax："))
        self.groupBox_3.setTitle(_translate("MainWindow", "参数设置"))
        self.label_0.setText(_translate("MainWindow", "最大目标数"))
        self.comboBox.setItemText(0, _translate("MainWindow", "all"))
        self.comboBox.setItemText(1, _translate("MainWindow", "good"))
        self.comboBox.setItemText(2, _translate("MainWindow", "broke"))
        self.comboBox.setItemText(3, _translate("MainWindow", "uncovered"))
        self.comboBox.setItemText(4, _translate("MainWindow", "lose"))
        self.comboBox.setItemText(5, _translate("MainWindow", "circle"))
        self.label_1.setText(_translate("MainWindow", "检测类别"))
        self.label_2.setText(_translate("MainWindow", "置信度阈值"))
        self.label_3.setText(_translate("MainWindow", "交并比阈值"))
        self.checkBox.setText(_translate("MainWindow", "相似度分析"))
        self.checkBox_2.setText(_translate("MainWindow", "预测源增强"))
        self.groupBox_4.setTitle(_translate("MainWindow", "文件操作"))
        self.pushButton_0.setText(_translate("MainWindow", "导入图片"))
        self.pushButton_1.setText(_translate("MainWindow", "批量识别"))
        self.pushButton_2.setText(_translate("MainWindow", "保存结果"))
        self.pushButton_3.setText(_translate("MainWindow", "退出程序"))
        self.groupBox_5.setTitle(_translate("MainWindow", "多类别相似度"))

    def detect_image(self,image_path,value,conf,iou,classes):


        if classes == 'all':
            classes = None  # 将classes设置为None，表示检测所有类别
        elif classes == 'good':
            classes = 0
        elif classes == 'broke':
            classes = 1
        elif classes == 'uncovered':
            classes = 2
        elif classes == 'circle':
            classes = 3
        elif classes == 'lose':
            classes = 4
        model = YOLO(r'weights\best.pt')
        results = model.predict(source=image_path, max_det=value, conf=conf, iou=iou,classes=classes)
        im = Image.open(image_path)

        class_names = ['good', 'broke', 'lose', 'uncovered', 'circle']

        
        for r in results:
            boxes = r.boxes
            im_array = r.plot()  # plot a BGR numpy array of predictions
            pre_image = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            de_num = len(boxes)
        for box in boxes:
            # 获取类别索引
            # class_indices = box.cls.numpy().astype(int)
            # class_labels = [class_names[i] for i in class_indices]

            class_indices = box.cls.numpy()[0].astype(int)
            class_labels = class_names[class_indices]
            # 获取预测框坐标
            x1, y1, x2, y2 = box.xyxy.numpy().flatten().astype(int)
            
            # 获取预测框置信度
            de_conf = box.conf.numpy()[0]
            print(de_conf)
            croped = im.crop((x1, y1, x2, y2))
            croped = croped.convert('RGB')
            qcroped = QImage(croped.tobytes(), croped.width, croped.height, croped.width * 3, QImage.Format_RGB888)
            # 加载处理后的图片
            qcroped = QPixmap(qcroped)
            # row_count = self.tableWidget.rowCount()
            # self.tableWidget.insertRow(row_count)
            # self.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(row_count)))
            # self.tableWidget.setItem(row_count, 1, QtWidgets.QTableWidgetItem(image_path))
            # self.tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(class_indices)))
            # self.tableWidget.setItem(row_count, 3, QtWidgets.QTableWidgetItem(str(de_conf)))
            # self.tableWidget.setItem(row_count, 4, QtWidgets.QTableWidgetItem(f"({x1},{y1},{x2},{y2})"))

            
        return pre_image, qcroped, croped,de_num,class_labels,de_conf,x1,x2,y1,y2,class_indices

    def toggleExtraCode(self,state):
        if state == Qt.Checked:
            self.pushButton_0.clicked.connect(self.sia_classifier)
        else:
            self.pushButton_0.clicked.disconnect(self.sia_classifier)
    #@QtCore.pyqtSlot(int)
    def open_image(self):
        image_path = QtWidgets.QFileDialog.getOpenFileName(None, "选择图片", "", "Image Files(*.jpg *.png *.jpeg)")[0]
        max_n = self.spinBox.value()
        conf = self.doubleSpinBox.value()
        iou = self.doubleSpinBox_2.value()
        classes = self.comboBox.currentText()
        if image_path:
            self.progressBar.setValue(0)
            self.progressBar.setVisible(True)
            self.star_timer()
            pre_image0,qcroped,croped,de_num,de_cls,de_conf,x1,x2,y1,y2,class_id= self.detect_image(image_path,max_n,conf,iou,classes)
            
            pre_image = pre_image0.convert('RGB')
            qimage = QImage(pre_image.tobytes(), pre_image.width, pre_image.height, pre_image.width * 3, QImage.Format_RGB888)
            # 加载处理后的图片
            pixmap = QPixmap(qimage)
            # 在QLabel中显示图片，保持图片的宽高比
            self.image_label_0.setPixmap(pixmap.scaled(self.image_label_0.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
            self.image_label_1.setPixmap(qcroped.scaled(self.image_label_1.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
            # 在检测结果中显示相关参数
            self.textBrowser_11.setText(str(de_num))
            self.textBrowser_10.setText(str(de_cls))
            self.textBrowser_12.setText(f"{de_conf:.2f}")
            self.textBrowser_7.setText(str(x1))
            self.textBrowser_6.setText(str(x2))
            self.textBrowser_8.setText(str(y1))
            self.textBrowser_9.setText(str(y2))
            self.textBrowser_4.append(f"图片：{image_path} 处理完成。\n")
            # 添加到 tableWidget
            row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_count)
            self.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(row_count)))
            self.tableWidget.setItem(row_count, 1, QtWidgets.QTableWidgetItem(image_path))
            self.tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(class_id)))
            self.tableWidget.setItem(row_count, 3, QtWidgets.QTableWidgetItem(str(de_conf)))
            self.tableWidget.setItem(row_count, 4, QtWidgets.QTableWidgetItem(f"({x1},{y1},{x2},{y2})"))

            self.croped_value = croped
            self.result_pic = pre_image0
    def sia_classifier(self):

        croped = self.croped_value
        stability = 25#稳定度
        directories = {
        'good': 'data/good',
        'broke': 'data/broke',
        'uncovered': 'data/uncovered',
        'circle': 'data/circle',
        'lose': 'data/lose',
        }

        similarity_values, all_similarities = calculate_similarity(croped, directories, stability)
        probabilities = calculate_probabilities(similarity_values)
        ana_im = plot_probabilities(probabilities)
        ana_im.savefig('results1.jpg')
        ana_im = Image.open('results1.jpg')
        ana_im = ana_im.convert('RGB')
        qana_im = QImage(ana_im.tobytes(), ana_im.width, ana_im.height, ana_im.width * 3, QImage.Format_RGB888)
        # 加载处理后的图片
        qana_im = QPixmap(qana_im)
         # 清空图片
        self.image_label_2.clear()
        self.image_label_2.setPixmap(qana_im.scaled(self.image_label_2.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
    def save_image(self):
        im =  self.result_pic
        # 打开文件对话框
        file_path = QtWidgets.QFileDialog.getSaveFileName(None, "保存图片", ".png", "Image Files(*.jpg *.png *.jpeg)")[0]
        if file_path:
            im.save(file_path)
        
    
    def batch_detect(self):
        # 获取文件夹路径
        dir_path = QtWidgets.QFileDialog.getExistingDirectory(None, "选择文件夹", "")
        # 遍历文件夹中的图片
        if dir_path:
            max_n = self.spinBox.value()
            conf = self.doubleSpinBox.value()
            iou = self.doubleSpinBox_2.value()
            classes = self.comboBox.currentText()
            if classes == 'all':
                classes = None  # 将classes设置为None，表示检测所有类别
            elif classes == 'good':
                classes = 0
            elif classes == 'broke':
                classes = 1
            elif classes == 'uncovered':
                classes = 2
            elif classes == 'circle':
                classes = 3
            elif classes == 'lose':
                classes = 4
            model = YOLO(r'weights\best.pt')
            results_file_path = os.path.join(os.path.dirname(dir_path), "results.txt")

            with open(results_file_path, 'w') as f:
                results = model.predict(source=dir_path, max_det=max_n, conf=conf, iou=iou, classes=classes)
                for r in results:
                    img_path = r.path
                    boxes = r.boxes
                    if len(boxes) == 0:
                        f.write(f'{os.path.basename(img_path)} 0 0 0 0 0 0\n')
                    elif len(boxes) == 1:
                        box = boxes[0]
                        class_indices = box.cls.numpy()[0].astype(int)  # 类别ID
                        de_conf = box.conf.numpy()[0]
                        x1, y1, x2, y2 = box.xyxy.numpy().flatten().astype(int)
                        f.write(f'{os.path.basename(img_path)} {class_indices} {de_conf} {x1} {y1} {x2} {y2}\n')
                    else:
                        boxes = sorted(boxes, key=lambda x: x.conf.numpy()[0], reverse=True)
                        if boxes[0].cls.numpy()[0].astype(int) == 4 and boxes[1].cls.numpy()[0].astype(int) == 2:
                            box = boxes[1]
                        else:
                            box = boxes[0]
                        class_indices = box.cls.numpy()[0].astype(int)  # 类别ID
                        de_conf = box.conf.numpy()[0]
                        x1, y1, x2, y2 = box.xyxy.numpy().flatten().astype(int)
                        f.write(f'{os.path.basename(img_path)} {class_indices} {de_conf} {x1} {y1} {x2} {y2}\n')

                    self.textBrowser_4.append(f"图片：{os.path.basename(img_path)} 处理完成。\n")
                self.textBrowser_4.append(f"所有图片处理完成。检测结果已保存到 {results_file_path}")

    def quit_app(self):
        sys.exit(app.exec_())
    def status_display(self):
        pass
    def star_timer(self):
        if not self.timer.isActive():
            self.timer.start()
    def update_progress(self):
        # 更新进度条的值
        self.progressBar.setValue(self.progressBar.value() + 1)
        # 检查是否达到100，如果是，则停止计时器
        if self.progressBar.value() >= 100:
            self.timer.stop()
if __name__ == "__main__":
    import sys
    import multiprocessing
    multiprocessing.freeze_support()
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

"""
3.6开发目标
1.完成进度条的代码编写
2.完成检测目录的代码编写
    
"""

# def batch_detect(self):
#         # 获取文件夹路径
#         dir_path = QtWidgets.QFileDialog.getExistingDirectory(None, "选择文件夹", "")
#         # 遍历文件夹中的图片
#         if dir_path:
#             max_n = self.spinBox.value()
#             conf = self.doubleSpinBox.value()
#             iou = self.doubleSpinBox_2.value()
#             classes = self.comboBox.currentText()
#             if classes == 'all':
#                 classes = None  # 将classes设置为None，表示检测所有类别
#             elif classes == 'good':
#                 classes = 0
#             elif classes == 'broke':
#                 classes = 1
#             elif classes == 'uncovered':
#                 classes = 2
#             elif classes == 'circle':
#                 classes = 3
#             elif classes == 'lose':
#                 classes = 4
#             model = YOLO(r'weights\best.pt')
#             # results = model.predict(source=dir_path, max_det=max_n, conf=conf, iou=iou,classes=classes)
#             # print(results)
#             #im = Image.open(dir_path)
#             #class_names = ['good', 'broke', 'uncovered', 'circle', 'lose']
        
#             results_file_path = os.path.join(os.path.dirname(dir_path),"results.txt")
#                 # 将识别结果写入txt文件
#                 # 每一行的格式为：图片名称 类别id xmin ymin xmax ymax

#             with open(results_file_path, 'w') as f:
#                 results = model.predict(source=dir_path, max_det=max_n, conf=conf, iou=iou,classes=classes)
#                # 遍历所有结果
#                 for r in results:
#                     img_path = r.path
#                     for box in r.boxes:
#                         class_indices = box.cls.numpy()[0].astype(int)  # 类别ID
#                         de_conf = box.conf.numpy()[0]
#                         x1, y1, x2, y2 = box.xyxy.numpy().flatten().astype(int)
#                         f.write(f'{os.path.basename(img_path)} {class_indices} {de_conf} {x1} {y1} {x2} {y2}\n')
#                     self.textBrowser_4.append(f"图片：{os.path.basename(img_path)} 处理完成。\n")
#                 self.textBrowser_4.append(f"所有图片处理完成。检测结果已保存到 {results_file_path}")