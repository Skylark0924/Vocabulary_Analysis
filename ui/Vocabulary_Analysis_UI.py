# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vocabulary_Analysis.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.QtWidgets import QPushButton, QRadioButton, QLabel, QLineEdit, QWidget, QTextEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QButtonGroup
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenuBar, QMenu, QAction
import os
import sys

class Ui_MainWindow(QMainWindow):
    def setupUi(self):
        # self.setWindowState(QtCore.Qt.WindowMaximized)
        self.pushButton_clear = QPushButton('Clear')
        self.pushButton_clear.setStyleSheet("QPushButton{background-color:white;\
                                                    color: black;   border-radius: 10px;  border: 3px groove darkgray; border-style: outset;width:280px;}"
                                                "QPushButton:hover{background-color:white; color: black;}"
                                                "QPushButton:pressed{background-color:white; border-style: inset; }")

        # self.pushButton_segmentation = QPushButton('分割结节')
        # self.pushButton_segmentation.setStyleSheet("QPushButton{background-color:white;\
        #                                             color: black;   border-radius: 10px;  border: 3px groove darkgray; border-style: outset;width:280px;}"
        #                                            "QPushButton:hover{background-color:white; color: black;}"
        #                                            "QPushButton:pressed{background-color:white; border-style: inset; }")
        #
        # self.pushButton_manual_detect = QPushButton('手动确认位置')
        # self.pushButton_manual_detect.setStyleSheet("QPushButton{background-color:white;\
        #                                             color: black;   border-radius: 10px;  border: 3px groove darkgray; border-style: outset;width:280px;}"
        #                                             "QPushButton:hover{background-color:white; color: black;}"
        #                                             "QPushButton:pressed{background-color:white; border-style: inset; }")
        #
        # self.pushButton_clear_report = QPushButton('清除诊断报告')
        # self.pushButton_clear_report.setStyleSheet("QPushButton{background-color:white;\
        #                                             color: black;   border-radius: 10px;  border: 3px groove darkgray; border-style: outset;width:280px;}"
        #                                            "QPushButton:hover{background-color:white; color: black;}"
        #                                            "QPushButton:pressed{background-color:white; border-style: inset; }")
        #
        # self.pushButton_save_report = QPushButton('输出诊断报告')
        # self.pushButton_save_report.setStyleSheet("QPushButton{background-color:white;\
        #                                             color: black;   border-radius: 10px;  border: 3px groove darkgray; border-style: outset;width:280px;}"
        #                                           "QPushButton:hover{background-color:white; color: black;}"
        #                                           "QPushButton:pressed{background-color:white; border-style: inset; }")

        self.pushButton_search = QPushButton('Search')
        self.pushButton_search.setStyleSheet("QPushButton{background-color:white;\
                                                    color: black;   border-radius: 10px;  border: 3px groove darkgray; border-style: outset;width:280px;}"
                                                "QPushButton:hover{background-color:white; color: black;}"
                                                "QPushButton:pressed{background-color:white; border-style: inset; }")

        # self.pushButton_close = QPushButton('关闭')
        # self.pushButton_close.setStyleSheet("QPushButton{background-color:white;\
        #                                             color: black;   border-radius: 10px;  border: 3px groove darkgray; border-style: outset;width:280px;}"
        #                                     "QPushButton:hover{background-color:white; color: black;}"
        #                                     "QPushButton:pressed{background-color:white; border-style: inset; }")

        # self.radioButton_hybrid = QRadioButton('复合判断')
        # self.radioButton_hybrid.setToolTip('机器学习特征+传统图像处理特征（建议使用）')
        # self.radioButton_hybrid.setChecked(True)
        # self.radioButton_ml = QRadioButton('机器学习判断')
        # self.radioButton_ml.setToolTip('机器学习特征')

        self.label_explain = QLabel("Explanation of the vocabulary")  # 图片展示区域
        self.label_explain.adjustSize()
        self.label_explain.setWordWrap(True)
        self.label_explain.setAlignment(QtCore.Qt.AlignCenter)
        self.label_explain.setStyleSheet('''
            QLabel{
                color:#232C51;
                background:white;
            }
        ''')
        self.label_map = QWebEngineView()
        # self.label_map.setUrl(QtCore.QUrl("about:blank"))
        # self.label_map.setStyleSheet('''
        #             QWebEngineView{
        #                 color:Black;
        #                 background:white;
        #                 border-top:3px solid darkGray;
        #                 border-bottom:3px solid darkGray;
        #                 border-right:3px solid darkGray;
        #                 border-top-right-radius:10px;
        #                 border-bottom-right-radius:10px;
        #                 border-radius: 10px;
        #                 border:3px groove;
        #             }
        #         ''')
        # self.label_map.adjustSize()
#         self.label_map.setHtml('''<!DOCTYPE html>
# <html>
# <head>
#     <meta charset="utf-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <title></title>
#     <link rel="stylesheet" href="">
# </head>
# <body>
#     <div>测试html</div>
# </body>
# </html>''')

        # self.label_map.setWordWrap(True)
        # self.label_map.setAlignment(QtCore.Qt.AlignCenter)

        # self.label_map # 报告显示区域

        self.lineEdit_patient = QLineEdit('')
        self.lineEdit_oncologist = QLineEdit('')
        self.lineEdit_oncologist.setStyleSheet(
            '''QLineEdit{
                    border:1px solid darkgray;
                    width:300px;
                    border-top:3px solid darkGray;
                    border-bottom:3px solid darkGray;
                    border-right:3px solid darkGray;
                    border-radius:10px;
                    padding:2px 4px;
                    border:3px groove;
            }''')
        self.lineEdit_patient.setStyleSheet(
            '''QLineEdit{
                    border:1px solid darkgray;
                    width:300px;
                    border-top:3px solid darkGray;
                    border-bottom:3px solid darkGray;
                    border-right:3px solid darkGray;
                    border-radius:10px;
                    padding:2px 4px;
                    border:3px groove;
            }''')
        # </editor-fold>

        # <editor-fold desc="Indication widgets">
        label_clf_method = QLabel('分类方法选择：')
        label_clf_method.setStyleSheet('''
                    QLabel{
                        color:Black;
                        background:white;
                        border: None
                    }
                ''')
        label_field = QLabel('Field：           ')
        label_field.setStyleSheet('''
                    QLabel{
                        color:Black;
                        background:white;
                        border: None
                    }
                ''')
        label_vocab = QLabel('Vocabulary：')
        label_vocab.setStyleSheet('''
                    QLabel{
                        color:Black;
                        background:white;
                        border: None
                    }
                ''')
        label_map = QLabel('Semantic Relation Map')
        label_map.setStyleSheet('''
                    QLabel{
                        color:Black;
                        background:white;
                        border: None
                    }
                ''')
        self.label_test = QTextEdit('')
        self.label_test.setPlaceholderText("Comment")
        self.label_test.setStyleSheet(
            '''QTextEdit{
                    border: None
            }''')
        # </editor-fold>

        # <editor-fold desc="Arrangement of widgets">
        """
        分类方法选择:  O 复合诊断
                     O 机器学习诊断
        """
        # self.groupBox_clf_method = QButtonGroup()  # 分类方式二选一, 并竖着放置
        # self.groupBox_clf_method.addButton(self.radioButton_hybrid)
        # self.groupBox_clf_method.addButton(self.radioButton_ml)
        # vLayout_radioButton = QVBoxLayout()
        # vLayout_radioButton.addWidget(self.radioButton_hybrid)
        # vLayout_radioButton.addWidget(self.radioButton_ml)

        # hLayout_clf_method = QHBoxLayout()  # 水平放置分类方法选择
        # hLayout_clf_method.addWidget(label_clf_method)
        # hLayout_clf_method.addLayout(vLayout_radioButton)

        """
        患者: ____
        医师: ____
        """
        hLayout_patient = QHBoxLayout()
        hLayout_patient.addWidget(label_field)
        hLayout_patient.addWidget(self.lineEdit_patient)
        hLayout_patient.addStretch(1)
        hLayout_oncologist = QHBoxLayout()
        hLayout_oncologist.addWidget(label_vocab)
        hLayout_oncologist.addWidget(self.lineEdit_oncologist)
        hLayout_oncologist.addStretch(1)
        vLayout_person = QVBoxLayout()
        vLayout_person.addLayout(hLayout_patient)
        vLayout_person.addLayout(hLayout_oncologist)

        """
        开始诊断
        圈画结节
        分割结节
        关闭
        """
        vLayout_functions = QVBoxLayout()
        vLayout_functions.addStretch()  # 上下各 addStretch 可以使得内容居中
        vLayout_functions.addWidget(self.pushButton_search)
        vLayout_functions.addSpacing(20)
        vLayout_functions.addWidget(self.pushButton_clear)
        vLayout_functions.addSpacing(20)
        # vLayout_functions.addWidget(self.pushButton_manual_detect)
        # vLayout_functions.addSpacing(20)
        # vLayout_functions.addWidget(self.pushButton_segmentation)
        # vLayout_functions.addSpacing(20)
        # vLayout_functions.addWidget(self.pushButton_close)
        # vLayout_functions.addSpacing(20)
        vLayout_functions.addStretch()
        vLayout_functions.setAlignment(QtCore.Qt.AlignCenter)

        """
        诊断结果:
        消除报告 输出报告
        """
        hLayout_report = QHBoxLayout()
        # hLayout_report.addWidget(self.pushButton_clear_report)
        # hLayout_report.addWidget(self.pushButton_save_report)
        vLayout_report = QVBoxLayout()
        vLayout_report.addWidget(label_map)
        vLayout_report.addLayout(hLayout_report)
        # vLayout_report.addWidget(label_map)

        vLayout_test = QVBoxLayout()
        # vLayout_test.addWidget(self.pushButton_save_report)
        vLayout_test.addWidget(self.label_test)
        vLayout_test.addLayout(hLayout_report)

        """
        block01 = clf_method choice + person_information (扁)
        block02 = empty
        block03 = vLayout_report
        block11 = label_explain
        block12 = function_buttons (todo: 想要隐藏)
        block13 = report
        ===========================
        block01 |block02| block03
        ---------------------------
                |       |report
        block11 | btns  |------
                |       |test
        ============================
        """
        hLayout01 = QHBoxLayout()
        # hLayout01.addLayout(hLayout_clf_method)
        hLayout01.addLayout(vLayout_person)
        block01 = QWidget()
        block01.setLayout(hLayout01)
        block01.setStyleSheet('''
            QWidget{
                color:#232C51;
                background:white;
                border-top:3px solid darkGray;
                border-bottom:3px solid darkGray;
                border-right:3px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
                border-radius: 10px;
                border:3px groove;
            }
        ''')

        block12 = QWidget()
        block12.setLayout(vLayout_functions)

        block03 = QWidget()
        block03.setLayout(vLayout_report)
        block03.setStyleSheet('''
            QWidget{
                color:#232C51;
                background:white;
                border: None;
            }
        ''')

        block23 = QWidget()
        block23.setLayout(vLayout_test)
        block23.setStyleSheet('''
            QWidget{
                color:#232C51;
                background:white;
                border-radius: 10px;
                border:3px groove;
            }
        ''')

        gLayout_main = QGridLayout()
        gLayout_main.addWidget(block01, 0, 1)
        gLayout_main.addWidget(self.label_explain, 1, 1, 2, 1)
        gLayout_main.addWidget(block12, 1, 2, 2, 1)
        gLayout_main.addWidget(block03, 0, 3)
        gLayout_main.addWidget(block23, 2, 3)
        gLayout_main.addWidget(self.label_map, 1, 3)

        gLayout_main.setRowStretch(0, 1)
        gLayout_main.setRowStretch(1, 4)
        gLayout_main.setRowStretch(2, 2)

        gLayout_main.setSpacing(0)
        # gLayout_main.setColumnStretch(0, 3)
        # gLayout_main.setColumnStretch(1, 1)
        # gLayout_main.setColumnStretch(2, 3)

        '''
        hLayout_first_line = QHBoxLayout()
        hLayout_first_line.addLayout(hLayout_clf_method)
        hLayout_first_line.addLayout(vLayout_person)
        hLayout_first_line.addLayout(vLayout_report)

        hLayout_second_line = QHBoxLayout()
        hLayout_second_line.addWidget(self.label_explain)
        hLayout_second_line.addLayout(vLayout_functions)
        hLayout_second_line.addWidget(self.label_map)

        vLayout_main = QVBoxLayout()
        vLayout_main.addLayout(hLayout_first_line)
        vLayout_main.addLayout(hLayout_second_line)
        '''
        self.widget_main = QWidget()
        self.widget_main.setLayout(gLayout_main)
        self.widget_main.setStyleSheet('''
            QWidget{
                background:#ffffff;

            }
        ''')
        self.setCentralWidget(self.widget_main)
        # </editor-fold>

        # <editor-fold desc="Menu Bar">
        """|文件|关于"""
        menuBar = self.menuBar()
        menuFile = menuBar.addMenu('文件')
        menuAbout = menuBar.addMenu('关于')

        """
        文件
        |——— 打开图像文件
        |——— 打开dicom文件
        |——— 退出
        """
        self.actionOpenImg = QAction('打开图像文件')
        self.actionOpenDcm = QAction('打开dicom文件')
        self.actionExit = QAction('退出')
        menuFile.addAction(self.actionOpenImg)
        menuFile.addAction(self.actionOpenDcm)
        menuFile.addAction(self.actionExit)

        self.actionAbout = QAction('关于')
        menuAbout.addAction(self.actionAbout)
        # </editor-fold>

        # <editor-fold desc="Status Bar">
        self.statusBar()
        self.statusBar().showMessage('完成')
        self.statusBar().setStyleSheet('''
            QStatusBar{
                background:white;
            }
        ''')

        # </editor-fold>

        # <editor-fold desc="Decoration">
        self.setWindowTitle('甲状腺识别')
        font = QtGui.QFont("Microsoft YaHei", 16)
        self.setFont(font)
        # self.widget_main.setFont(font)
        self.statusBar().setFont(font)

        self.label_explain.setMinimumSize(QtCore.QSize(300, 300))
        # self.label_map.setMinimumSize(QtCore.QSize(200, 300))
        label_map.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_map.wordWrap()
        # self.label_map.setFrameShape(QtWidgets.QFrame.Panel)

        # </editor-fold>
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.widget_main.setSpacing(0)
        # #
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    font = QtGui.QFont("Microsoft YaHei", 16)
    app.setFont(font)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
