
from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb, datetime

class Ui_Dialog(object):

    def loaddata(self):
        connection = MySQLdb.connect('127.0.0.1', 'root', '','inv_bill_mgmt')
        cursor = connection.cursor()
        sql = "SELECT * FROM inventory_maincommit"
        cursor.execute(sql)
        results = cursor.fetchall()
        self.dataTable.setRowCount(0)
        for r,d in enumerate(results):
            self.dataTable.insertRow(r)
            for c,cd in enumerate(d):
                self.dataTable.setItem(r,c,QtWidgets.QTableWidgetItem(str(cd)))
                #a = self.dataTable.item(0,3).text()
                #b = self.dataTable.item(0,4).text()
                #self.dataTable.setItem(str(int(a)*int(b)))
        cursor.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1043, 739)
        _translate = QtCore.QCoreApplication.translate
        self.finalizePaymentBtn = QtWidgets.QPushButton(Dialog)
        self.finalizePaymentBtn.setGeometry(QtCore.QRect(380, 610, 281, 41))
        self.finalizePaymentBtn.setObjectName("finalizePaymentBtn")
        self.clearBtn = QtWidgets.QPushButton(Dialog)
        self.clearBtn.setGeometry(QtCore.QRect(750, 520, 111, 41))
        self.clearBtn.setObjectName("clearBtn")
        self.addEntryBtn = QtWidgets.QPushButton(Dialog)
        self.addEntryBtn.setGeometry(QtCore.QRect(890, 520, 111, 41))
        self.addEntryBtn.setObjectName("addEntryBtn")
        self.addEntryBtn.clicked.connect(self.loaddata)
        self.dataTable = QtWidgets.QTableWidget(Dialog)
        self.dataTable.setGeometry(QtCore.QRect(40, 80, 951, 361))
        self.dataTable.setMinimumSize(QtCore.QSize(951, 0))
        self.dataTable.setLineWidth(1)
        self.dataTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.dataTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dataTable.setAutoScrollMargin(16)
        self.dataTable.setAlternatingRowColors(True)
        self.dataTable.setShowGrid(True)
        self.dataTable.setWordWrap(True)
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(6)
        self.dataTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setItem(0, 5, item)
        self.dataTable.horizontalHeader().setVisible(True)
        self.dataTable.horizontalHeader().setCascadingSectionResizes(True)
        self.dataTable.horizontalHeader().setDefaultSectionSize(152)
        self.dataTable.horizontalHeader().setHighlightSections(True)
        self.dataTable.horizontalHeader().setMinimumSectionSize(30)
        self.dataTable.horizontalHeader().setSortIndicatorShown(False)
        self.dataTable.horizontalHeader().setStretchLastSection(True)
        self.dataTable.verticalHeader().setVisible(False)
        self.dataTable.verticalHeader().setCascadingSectionResizes(True)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 450, 931, 61))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 20, 951, 41))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.autoSerialText = QtWidgets.QLineEdit(self.groupBox)
        self.autoSerialText.setGeometry(QtCore.QRect(0, 20, 71, 41))
        self.autoSerialText.setObjectName("autoSerialText")
        self.prodIDNameText = QtWidgets.QLineEdit(self.groupBox)
        self.prodIDNameText.setGeometry(QtCore.QRect(70, 20, 681, 41))
        self.prodIDNameText.setObjectName("prodIDNameText")
        self.prodQuantityText = QtWidgets.QLineEdit(self.groupBox)
        self.prodQuantityText.setGeometry(QtCore.QRect(750, 20, 181, 41))
        self.prodQuantityText.setObjectName("prodQuantityText")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 580, 311, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label_9.setObjectName("label_9")
        self.mobileTextField = QtWidgets.QLineEdit(self.frame)
        self.mobileTextField.setGeometry(QtCore.QRect(110, 20, 151, 25))
        self.mobileTextField.setObjectName("mobileTextField")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.label_5.setObjectName("label_5")
        self.invoiceLabel = QtWidgets.QLabel(self.frame)
        self.invoiceLabel.setGeometry(QtCore.QRect(110, 60, 111, 21))
        self.invoiceLabel.setObjectName("invoiceLabel")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 100, 67, 17))
        self.label_7.setObjectName("label_7")
        self.dateLabel = QtWidgets.QLabel(self.frame)
        self.dateLabel.setGeometry(QtCore.QRect(110, 100, 111, 21))
        self.dateLabel.setObjectName("dateLabel")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(710, 580, 301, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(70, 100, 81, 31))
        self.label.setObjectName("label")
        self.totalLabel = QtWidgets.QLabel(self.frame_2)
        self.totalLabel.setGeometry(QtCore.QRect(170, 90, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.totalLabel.setFont(font)
        self.totalLabel.setObjectName("totalLabel")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.label_2.setObjectName("label_2")
        self.gstValueLabel = QtWidgets.QLabel(self.frame_2)
        self.gstValueLabel.setGeometry(QtCore.QRect(170, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gstValueLabel.setFont(font)
        self.gstValueLabel.setObjectName("gstValueLabel")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 560, 991, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.discardListBtn = QtWidgets.QPushButton(Dialog)
        self.discardListBtn.setGeometry(QtCore.QRect(30, 520, 101, 41))
        self.discardListBtn.setObjectName("discardListBtn")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(50, 50, 931, 21))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.label_11.setObjectName("label_11")
        self.userNameLabel = QtWidgets.QLabel(self.frame_3)
        self.userNameLabel.setGeometry(QtCore.QRect(65, 0, 151, 21))
        self.userNameLabel.setObjectName("userNameLabel")
        self.dateTimeLabel = QtWidgets.QLabel(self.frame_3)
        self.dateTimeLabel.setGeometry(QtCore.QRect(780, 0, 151, 21))
        self.dateTimeLabel.setObjectName("dateTimeLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(70, -10, 891, 51))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.prevTransBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.prevTransBtn.setGeometry(QtCore.QRect(0, 20, 181, 31))
        self.prevTransBtn.setObjectName("prevTransBtn")
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(30, 10, 31, 31))
        self.backbutton.setObjectName("backbutton")
        self.groupBox.setTitle(_translate("Dialog", "New Entry"))
        self.mobileTextField.setText(_translate("Dialog", "8801853078"))
        self.prodIDNameText.setText(_translate("Dialog", "Product ID or Product Name"))
        self.prodQuantityText.setText(_translate("Dialog", "Quantity (default 1)"))
        self.invoiceLabel.setText(_translate("Dialog", "AE7155424"))
        self.gstValueLabel.setText(_translate("Dialog", "1.25"))
        self.dateLabel.setText(_translate("Dialog", "12-05-2018"))
        self.totalLabel.setText(_translate("Dialog", "61.25"))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Billing"))
        self.finalizePaymentBtn.setText(_translate("Dialog", "Finalize Payment and Print Invoice"))
        self.clearBtn.setText(_translate("Dialog", "Clear"))
        self.addEntryBtn.setText(_translate("Dialog", "Add Entry"))
        self.dataTable.setSortingEnabled(True)
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "S No"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Product ID"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Product Name"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Quantity"))
        item = self.dataTable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Price (per unit)"))
        item = self.dataTable.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Effective Price"))
        __sortingEnabled = self.dataTable.isSortingEnabled()
        self.dataTable.setSortingEnabled(False)
        self.autoSerialText.setText(_translate("Dialog","   (auto)"))
        self.dataTable.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("Dialog", "Mobile No"))
        self.label_5.setText(_translate("Dialog", "Invoice ID:"))
        self.label_7.setText(_translate("Dialog", "Date:"))
        self.label.setText(_translate("Dialog", "Total Price"))
        self.label_2.setText(_translate("Dialog", "GST and Other Taxes"))
        self.discardListBtn.setText(_translate("Dialog", "Discard List"))
        self.label_11.setText(_translate("Dialog", "Welcome,"))
        self.userNameLabel.setText(_translate("Dialog", "Al Khair Super Market"))
        self.dateTimeLabel.setText(_translate("Dialog", "00-00-0000, 00:00:00"))
        self.prevTransBtn.setText(_translate("Dialog", "Previous Transactions"))
        self.backbutton.setText(_translate("Dialog", "<"))
        now = datetime.datetime.now()
        self.dateTimeLabel.setText(_translate("Dialog",now.strftime("%Y-%m-%d %H:%M:%S"), None))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    timer = QtCore.QTimer(Dialog)
    timer.timeout.connect(lambda: ui.retranslateUi(Dialog))
    timer.start(1000)
    Dialog.show()
    sys.exit(app.exec_())

