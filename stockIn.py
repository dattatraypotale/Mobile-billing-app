# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stockIn.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(714, 477)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(9, 34, 211, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.splitter_12 = QtWidgets.QSplitter(self.frame)
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName("splitter_12")
        self.label_8 = QtWidgets.QLabel(self.splitter_12)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.splitter_12)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.splitter_13 = QtWidgets.QSplitter(self.frame)
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName("splitter_13")
        self.label_9 = QtWidgets.QLabel(self.splitter_13)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.splitter_13)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.splitter_14 = QtWidgets.QSplitter(self.frame)
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName("splitter_14")
        self.label_10 = QtWidgets.QLabel(self.splitter_14)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.splitter_14)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.splitter_15 = QtWidgets.QSplitter(self.frame)
        self.splitter_15.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_15.setObjectName("splitter_15")
        self.label_11 = QtWidgets.QLabel(self.splitter_15)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.splitter_15)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.splitter_16 = QtWidgets.QSplitter(self.frame)
        self.splitter_16.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_16.setObjectName("splitter_16")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.splitter_16)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(226, 34, 217, 162))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 0, 1, 2)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(449, 34, 256, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(226, 202, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(9, 231, 691, 231))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(9, 9, 485, 19))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "Name :"))
        self.label_8.setText(_translate("Form", "Model Numbr :"))
        self.label_9.setText(_translate("Form", "price :"))
        self.label_10.setText(_translate("Form", "Qty :"))
        self.label_11.setText(_translate("Form", "Vendor"))
        self.pushButton.setText(_translate("Form", "ADD"))
        self.label_15.setText(_translate("Form", "Name :"))
        self.label_14.setText(_translate("Form", "Model Number :"))
        self.label_16.setText(_translate("Form", "Vendor"))
        self.pushButton_2.setText(_translate("Form", "search"))
        self.pushButton_3.setText(_translate("Form", "Update"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "StockIn Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Model No."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "HSN Code"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "IMEI No."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Vendor"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Price"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">Add stock </span></p></body></html>"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">Update HSN code,EMEI No and other Information</span></p></body></html>"))

        self.pushButton.clicked.connect(self.clickMethod_add)
        self.pushButton_3.clicked.connect(self.clickMethod_update)
        self.pushButton_2.clicked.connect(self.search_stock_in_records)

    def clickMethod_add(self):
        Ui_Form.stock_in(self)
        Ui_Form.make_table(self)

    def clickMethod_update(self):
        Ui_Form.update_stock_in_record(self)

    def stock_in(self):
        print("inside stock_in")
        name = self.lineEdit.text()
        model_number = self.lineEdit_2.text()
        price = int(self.lineEdit_3.text())
        qty = int(self.lineEdit_4.text())
        vendor = self.lineEdit_5.text()
        today_date = self.calendarWidget.selectedDate()
        # print("{} {} {} {} {} {}".format(name, model_number, price, qty, vendor, today_date.toString()))
        return name, model_number, price, qty, vendor, today_date.toString()

    def make_table(self):
        print("inside make table")
        stock_in_data = Ui_Form.stock_in(self)
        print(stock_in_data)

        self.tableWidget.setRowCount(0)

        qty = int(stock_in_data[3])
        for row_number in range(qty):
            self.tableWidget.insertRow(row_number)
            for colomn_number in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(stock_in_data[5])))
                self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(stock_in_data[0])))
                self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(stock_in_data[1])))
                self.tableWidget.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(stock_in_data[4])))
                self.tableWidget.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(stock_in_data[2])))

    def update_stock_in_record(self):
        row = self.tableWidget.rowCount()

        # product_id = "" since product_id is set autoincrement in database no need to reference in query
        conn = sqlite3.connect('mymobileshoppy.db');
        c = conn.cursor()

        for row_num in range(row):

            product_name = self.tableWidget.item(row_num, 1).text()
            product_model_number = self.tableWidget.item(row_num, 2).text()
            product_hsn_code = self.tableWidget.item(row_num, 3).text()
            product_imei_number = self.tableWidget.item(row_num, 4).text()
            product_price = int(self.tableWidget.item(row_num, 6).text())
            vendor = self.tableWidget.item(row_num, 5).text()
            stock_in_date = self.tableWidget.item(row_num, 0).text()

            data = [product_name, product_model_number, product_hsn_code, product_imei_number, product_price,
                    vendor, stock_in_date]

            print("Opened database successfully");

            sql = "INSERT INTO stocks (product_name, product_model_number, product_hsn_code, product_imei_number, product_price, vendor, stock_in_date) VALUES (?,?,?,?,?,?,?)"

            c.execute(sql, data)
            print(data)

        conn.commit()
        print("Records created successfully")
        conn.close()

    def search_stock_in_records(self):
        name = self.lineEdit_9.text()
        product_model_number = self.lineEdit_8.text()
        vendor = self.lineEdit_10.text()
        print(len(name))
        print("{} {} {}".format(name, product_model_number, vendor))
        self.tableWidget.setRowCount(0)
        conn = sqlite3.connect('mymobileshoppy.db');
        c = conn.cursor()

        if ( len(name) > 0 ):
            print("In name")
            query = "select product_name,product_model_number,product_hsn_code,product_imei_number,product_price,vendor,stock_in_date  from stocks WHERE product_name = ?"
            result = c.execute(query, (name,))

            for row_num, row_data in enumerate(result):
                self.tableWidget.insertRow(row_num)
                self.tableWidget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(row_data[6])))
                self.tableWidget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(row_data[0])))
                self.tableWidget.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(row_data[1])))
                self.tableWidget.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(row_data[2])))
                self.tableWidget.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(row_data[3])))
                self.tableWidget.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(row_data[5])))
                self.tableWidget.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(row_data[4])))

        if ( len(product_model_number) > 0 ):
            print("in product model")
            query = "select product_name,product_model_number,product_hsn_code,product_imei_number,product_price,vendor,stock_in_date  from stocks WHERE product_model_number = ?"
            result = c.execute(query, (product_model_number,))

            for row_num, row_data in enumerate(result):
                self.tableWidget.insertRow(row_num)
                self.tableWidget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(row_data[6])))
                self.tableWidget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(row_data[0])))
                self.tableWidget.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(row_data[1])))
                self.tableWidget.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(row_data[2])))
                self.tableWidget.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(row_data[3])))
                self.tableWidget.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(row_data[5])))
                self.tableWidget.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(row_data[4])))

        if ( len(vendor) > 0 ):
            print("IN vendor")
            query = "select product_name,product_model_number,product_hsn_code,product_imei_number,product_price,vendor,stock_in_date  from stocks WHERE vendor = ?"
            result = c.execute(query, (vendor,))

            for row_num, row_data in enumerate(result):
                self.tableWidget.insertRow(row_num)
                self.tableWidget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(row_data[6])))
                self.tableWidget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(row_data[0])))
                self.tableWidget.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(row_data[1])))
                self.tableWidget.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(row_data[2])))
                self.tableWidget.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(row_data[3])))
                self.tableWidget.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(row_data[5])))
                self.tableWidget.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(row_data[4])))

        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

