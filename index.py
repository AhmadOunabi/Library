from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType          #to code live
import os
from os import path
import sqlite3


MainUI,_ = loadUiType(path.join(path.dirname(__file__),'main.ui'))                     #to code live with ui file 

class MainApp(QMainWindow , MainUI):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Db_connect()
        self.Handel_buttons()
        self.ui_change()
        self.combobox_categories()
        self.combobox_Author()
        
    def ui_change(self):
        self.tabWidget.tabBar().setVisible(False)    # to hide the tabwidgets
    
    def Db_connect(self):
        self.db=sqlite3.connect('library.db')
        self.cr=self.db.cursor()
        print('connected to Database')
    
    def Handel_buttons(self):
        self.pushButton.clicked.connect(self.Open_Today)
        self.pushButton_2.clicked.connect(self.Open_Books)
        self.pushButton_4.clicked.connect(self.Open_Clients)
        self.pushButton_3.clicked.connect(self.Open_Dashboard)
        self.pushButton_6.clicked.connect(self.Open_History)
        self.pushButton_5.clicked.connect(self.Open_Reports)
        self.pushButton_7.clicked.connect(self.Open_Settings)
        self.pushButton_8.clicked.connect(self.Handel_today_work)
        self.pushButton_22.clicked.connect(self.Add_Branch)
        self.pushButton_23.clicked.connect(self.Add_Publisher)
        self.pushButton_24.clicked.connect(self.Add_Author)
        self.pushButton_25.clicked.connect(self.Add_category)
        self.pushButton_47.clicked.connect(self.Add_employee)
        self.pushButton_48.clicked.connect(self.Edit_employee)
        
    
    def Handel_login(self):
        pass
    
    def Handel_reset_password(self):
        pass
    
    def Handel_today_work(self):
        pass
    ################################################# BOOKS
    def All_books(self):
        pass
    
    def New_book(self):
        pass
    
    def Update_book(self):
        pass
    
    def Delete_book(self):
        pass
    ################################################ CLIENTS
    def All_clients(self):
        pass
    
    def New_client(self):
        pass
    
    def Update_client(self):
        pass
    
    def Delete_client(self):
        pass
    ################################################# History
    def Show_history(self):
        pass
    ################################################# Reports
    def All_Books_reports(self):
        pass
    def Books_filter_reports(self):
        pass
    def Books_export_report(self):
        pass
    ################################
    def All_client_reports(self):
        pass
    def Client_Filter_reports(self):
        pass
    def Client_export_report(self):
        pass
    ################################
    def Monthly_repot(self):
        pass
    def Monthly_report_export(self):
        pass
    #################################################### Settings
    
    def Add_Branch(self):
        branch_name=self.lineEdit_31.text()
        branch_code=self.lineEdit_32.text()
        branch_location=self.lineEdit_33.text()
        self.cr.execute(''' INSERT INTO branch(Name,Code,Location)
            VALUES(?,?,?) ''', (branch_name,branch_code,branch_location))
        self.db.commit()
        branch_name=self.lineEdit_31.setText('')
        branch_code=self.lineEdit_32.setText('')
        branch_location=self.lineEdit_33.setText('')
        
    def Add_category(self):
        add_category=self.lineEdit_38.text()
        self.cr.execute(''' INSERT INTO Category(Category_name)
            VALUES(?) ''', (add_category,))
        self.db.commit()
        self.comboBox_12.addItem(add_category)
        add_category=self.lineEdit_38.setText('')
        
    def Add_Publisher(self):
        publisher_name=self.lineEdit_34.text()
        publisher_location=self.lineEdit_35.text()
        self.cr.execute(''' INSERT INTO Publisher(Name,Location)
            VALUES(?,?) ''', (publisher_name,publisher_location))
        self.db.commit()
        publisher_name=self.lineEdit_34.setText('')
        publisher_location=self.lineEdit_35.setText('')
        
    def Add_Author(self):
        Author_name=self.lineEdit_36.text()
        Author_nationality=self.lineEdit_37.text()
        self.cr.execute(''' INSERT INTO Author(Name,Location)
            VALUES(?,?) ''', (Author_name,Author_nationality))
        self.db.commit()
        Author_name=self.lineEdit_36.setText('')
        Author_nationality=self.lineEdit_37.setText('')
        
    def combobox_categories(self): # select all the items in Category name the save them in List 'categories' and then add them to Combobox
        self.cr.execute("SELECT Category_name FROM Category")
        categories=self.cr.fetchall()
        print(categories)
        for i in categories:
            self.comboBox_12.addItem(i[0])
            self.comboBox_2.addItem(i[0])
            self.comboBox_3.addItem(i[0])
            self.comboBox_9.addItem(i[0])
            
    def combobox_Author(self):
        self.cr.execute("SELECT Name FROM Author")
        authors=self.cr.fetchall()
        for i in authors:
            self.comboBox_8.addItem(i[0])
            self.comboBox_7.addItem(i[0])
            
    def combobox_publisher(self):
        self.cr.execute("SELECT Name FROM Publisher")
        publishers=self.cr.fetchall()
        for i in publishers:
            self.comboBox_10.addItem(i[0])
            self.comboBox_6.addItem(i[0])
        
    ################################# Employee
    def Add_employee(self):
        name=self.lineEdit_78.text()
        Email=self.lineEdit_79.text()
        Phone=self.lineEdit_80.text()
        Id=self.lineEdit_81.text()
        Priority=self.lineEdit_91.text()
        self.cr.execute(''' INSERT INTO Employee(Name,Email,National_ID,Phone,Priority)
            VALUES(?,?,?,?,?) ''', (name,Email,Id,Phone,Priority))
        self.db.commit()
        name=self.lineEdit_78.setText('')
        Email=self.lineEdit_79.setText('')
        Phone=self.lineEdit_80.setText('')
        Id=self.lineEdit_81.setText('')
        Priority=self.lineEdit_91.setText('')
        
        
    def Edit_employee(self):
        pass
    ################################# Permission
    def Add_employee_permissions(self):
        pass
    def Admin_reports(self):
        pass
    ################################### Connect Buttons with the Widgets
    def Open_Today(self):
        self.tabWidget.setCurrentIndex(1)         #to open the Widget when I press Today Button
    def Open_Books(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
    def Open_Clients(self):
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_3.setCurrentIndex(0)
    def Open_Dashboard(self):
        self.tabWidget.setCurrentIndex(4)
    def Open_History(self):
        self.tabWidget.setCurrentIndex(5)
    def Open_Reports(self):
        self.tabWidget.setCurrentIndex(6)
        self.tabWidget_11.setCurrentIndex(0)
    def Open_Settings(self):
        self.tabWidget.setCurrentIndex(7)
        self.tabWidget_5.setCurrentIndex(0)
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()