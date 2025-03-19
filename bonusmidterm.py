# Form implementation generated from reading ui file 'D:\pythonProject2\mid\bonusmidterm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 300)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #f0f8ff, stop:1 #e6f2ff);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.fileFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.fileFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fileFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fileFrame.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #ddd;\n"
"}")
        self.fileFrame.setObjectName("fileFrame")
        self.fileLayout = QtWidgets.QVBoxLayout(self.fileFrame)
        self.fileLayout.setObjectName("fileLayout")
        self.instructionLabel = QtWidgets.QLabel(parent=self.fileFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.instructionLabel.setFont(font)
        self.instructionLabel.setStyleSheet("color: #555; background-color: transparent; border: none;")
        self.instructionLabel.setObjectName("instructionLabel")
        self.fileLayout.addWidget(self.instructionLabel)
        self.fileInputLayout = QtWidgets.QHBoxLayout()
        self.fileInputLayout.setObjectName("fileInputLayout")
        self.filePathEdit = QtWidgets.QLineEdit(parent=self.fileFrame)
        self.filePathEdit.setReadOnly(True)
        self.filePathEdit.setStyleSheet("QLineEdit {\n"
"    padding: 10px;\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 5px;\n"
"    background-color: #f9f9f9;\n"
"}")
        self.filePathEdit.setObjectName("filePathEdit")
        self.fileInputLayout.addWidget(self.filePathEdit)
        self.browseButton = QtWidgets.QPushButton(parent=self.fileFrame)
        self.browseButton.setMinimumSize(QtCore.QSize(0, 40))
        self.browseButton.setStyleSheet("QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}")
        self.browseButton.setObjectName("browseButton")
        self.fileInputLayout.addWidget(self.browseButton)
        self.fileLayout.addLayout(self.fileInputLayout)
        self.verticalLayout.addWidget(self.fileFrame)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.setObjectName("buttonLayout")
        self.openButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.openButton.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.openButton.setFont(font)
        self.openButton.setStyleSheet("QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #3498db;\n"
"}")
        self.openButton.setObjectName("openButton")
        self.buttonLayout.addWidget(self.openButton)
        self.saveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("QPushButton {\n"
"    background-color: #e74c3c;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #c0392b;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #e74c3c;\n"
"}")
        self.saveButton.setObjectName("saveButton")
        self.buttonLayout.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.buttonLayout)
        self.versionLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.versionLabel.setStyleSheet("color: #7f8c8d; font-size: 9px;")
        self.versionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout.addWidget(self.versionLabel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chương Trình Đào Tạo Visualizer"))
        self.titleLabel.setText(_translate("MainWindow", "CHƯƠNG TRÌNH ĐÀO TẠO VISUALIZER"))
        self.instructionLabel.setText(_translate("MainWindow", "Chọn file Excel chứa dữ liệu chương trình đào tạo:"))
        self.filePathEdit.setPlaceholderText(_translate("MainWindow", "Đường dẫn đến file Excel..."))
        self.browseButton.setText(_translate("MainWindow", "Chọn File"))
        self.openButton.setText(_translate("MainWindow", "Mở Biểu Đồ Trong Trình Duyệt"))
        self.saveButton.setText(_translate("MainWindow", "Lưu Biểu Đồ Thành File HTML"))
        self.versionLabel.setText(_translate("MainWindow", "Version 1.0 | Developed by Student"))
