# -*- coding: utf-8 -*

import sys
import csv
import os

from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog



global csv_input_path

class Date():
    def __init__(self,year=1970,month=1,day=1):
        self.year=int(year)
        self.month=int(month)
        self.day=int(day)

def csv_to_list(file_path):
    with open(file_path, newline='', encoding='utf-8') as csv_input:
        input = csv.reader(csv_input)
        input_list=[]
        for row in input:
            input_list.append(row)
        return(input_list)

def get_row_index():
    return 11

def date_row_converter(date_row):
    for i in range(len(date_row)):
        if date_row[i].find("/") != -1:
            date_row[i]=date_row[i][date_row[i].find("/")+1:]
    return date_row

def get_year_and_month(filename):   #type = Date()
    year_index=filename.find("20")
    year=filename[year_index:year_index+4]
    month_index=filename.find("月")-1
    month=filename[month_index]
    return Date(year, month)

def get_date(i,year,month,date_row,is_end):    #type=Date()
    current_date=Date()
    current_date.year=year
    current_date.month=month
    current_date.day=int(date_row[i])
    if i>30 and int(date_row[i])<10 and not is_end:
        current_date.month=str(int(current_date.month)+1)
    return current_date

def end_date_adder(i,year,month,day,date_row):
    end_date=Date(year,month,day)
    if i+1>=len(date_row):
        end_date.day=str(int(end_date.day)+1)
    else:
        end_date=get_date(i+1,year,month,date_row,1)
    return end_date

def is_on_duty(duty):
    if duty.find("-")!=-1:
        return 1
    else:
        return 0

def get_start_time(duty):
    return duty[duty.find("-")-5:duty.find("-")]

def get_end_time(duty):
    return duty[duty.find("-")+1:duty.find("-")+6]

def create_output_list(date_row,row,event_row,year,month):
    output_list=[["Subject","Start Date","Start Time","End Date","End Time","Location"]]
    for i in range(2,len(row)):
        if is_on_duty(row[i]):
            output_list.append(creat_event(i,event_row,row,date_row,year,month))
    return output_list

def creat_event(i,event_row,row,date_row,year,month): #type=list
    event=[]
    start_date=get_date(i,year,month,date_row,0)
    start_time=get_start_time(row[i])
    end_time=get_end_time(row[i])
    end_date=start_date
    if int(end_time[:1])-int(start_time[:1])<0:
        end_date=end_date_adder(i,end_date.year,end_date.month,end_date.day,date_row)

    event.append(event_row[i])
    event.append(str(start_date.year)+"/"+str(start_date.month)+"/"+str(start_date.day))
    event.append(start_time)
    event.append(str(end_date.year)+"/"+str(end_date.month)+"/"+str(end_date.day))
    event.append(end_time)
    event.append("The Wall Live House")

    return event

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 160)
        self.label_input = QtWidgets.QLabel(Dialog)
        self.label_input.setGeometry(QtCore.QRect(30, 20, 101, 31))
        self.label_input.setObjectName("label_input")
        self.label_input_path = QtWidgets.QLabel(Dialog)
        self.label_input_path.setGeometry(QtCore.QRect(150, 20, 221, 31))
        self.label_input_path.setText("")
        self.label_input_path.setObjectName("label_input_path")
        self.label_input_path.setWordWrap(True)
        self.label_this_is = QtWidgets.QLabel(Dialog)
        self.label_this_is.setGeometry(QtCore.QRect(160, 70, 35, 16))
        self.label_this_is.setObjectName("label_this_is")
        self.textbox_year = QtWidgets.QLabel(Dialog)
        self.textbox_year.setGeometry(QtCore.QRect(190, 70, 35, 16))
        self.textbox_year.setText("")
        self.textbox_year.setObjectName("textbox_year")
        self.label_year = QtWidgets.QLabel(Dialog)
        self.label_year.setGeometry(QtCore.QRect(230, 70, 25, 16))
        self.label_year.setObjectName("label_year")
        self.textbox_month = QtWidgets.QLabel(Dialog)
        self.textbox_month.setGeometry(QtCore.QRect(250, 70,20, 16))
        self.textbox_month.setText("")
        self.textbox_month.setObjectName("textbox_month")
        self.label_month = QtWidgets.QLabel(Dialog)
        self.label_month.setGeometry(QtCore.QRect(270, 70, 20, 16))
        self.label_month.setObjectName("label_month")
        self.textbox_name = QtWidgets.QLabel(Dialog)
        self.textbox_name.setGeometry(QtCore.QRect(290, 70, 35, 16))
        self.textbox_name.setText("")
        self.textbox_name.setObjectName("textbox_name")
        self.label_sche = QtWidgets.QLabel(Dialog)
        self.label_sche.setGeometry(QtCore.QRect(330, 70, 45, 16))
        self.label_sche.setObjectName("label_sche")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btn_load)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 110, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.btn_save)
        self.textbox_row = QtWidgets.QLineEdit(Dialog)
        self.textbox_row.setGeometry(QtCore.QRect(30, 70, 115, 21))
        self.textbox_row.setObjectName("textbox_row")
        self.textbox_row.mousePressEvent= lambda _ :self.textbox_row.selectAll()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "惹沃班表小工具"))
        self.label_input.setText(_translate("Dialog", "班表.csv檔路徑："))
        self.label_this_is.setText(_translate("Dialog", "這是"))
        self.label_year.setText(_translate("Dialog", "年"))
        self.label_month.setText(_translate("Dialog", "月"))
        self.label_sche.setText(_translate("Dialog", "的班表"))
        self.pushButton.setText(_translate("Dialog", "讀取檔案"))
        self.pushButton_2.setText(_translate("Dialog", "輸出檔案"))
        self.textbox_row.setText(_translate("Dialog", "請在此輸入列數"))

    def btn_load(self):
        if not self.textbox_row.text().isnumeric():
            self.label_input_path.setText("請告訴我你在哪一列哦！")
        else:
            csv_input_path = QFileDialog.getOpenFileName(QFileDialog(),
                                                         "開啟檔案",
                                                        "/home/Downloads/",
                                                        "csv (*.csv)")[0]
            if csv_input_path != "":
                csv_input_filename = (os.path.basename(csv_input_path))  # get filename
                input_list = csv_to_list(csv_input_path)
                row_index = int(self.textbox_row.text()) - 1
                row = input_list[row_index]
                name = input_list[row_index][0]
                date_row = date_row_converter(input_list[3])
                event_row = input_list[4]
                current_year_and_month = get_year_and_month(csv_input_filename)
                global output_list
                output_list = create_output_list(date_row, row, event_row, current_year_and_month.year,
                                                 current_year_and_month.month)
                self.label_input.setText("班表.csv檔路徑:")
                self.label_input_path.setText(csv_input_path)
                self.textbox_year.setText(str(current_year_and_month.year))
                self.textbox_month.setText(str(current_year_and_month.month))
                self.textbox_name.setText(str(name))
                global is_loaded
                is_loaded = 1
            else:
                is_loaded=0
                self.label_input_path.setText("尚未載入檔案！")

    def btn_save(self):
        if not is_loaded:
            self.label_input_path.text="尚未讀取檔案！"
        else:
            csv_output_path = QFileDialog.getSaveFileName(QFileDialog(),
                                                         "開啟檔案",
                                                        "home/Downloads/"+self.textbox_year.text() + "年" +
                                                                       self.textbox_month.text() + "月" +
                                                                       self.textbox_name.text() + "的班表",
                                                                       "csv (*.csv)")[0]
            if csv_output_path:
                with open(csv_output_path, 'w', newline='') as csv_output_file:
                    writer = csv.writer(csv_output_file)
                    writer.writerows(output_list)
                    self.label_input.text="已輸出.csv檔至："
                    self.label_input_path.text=csv_output_path


'''win = tk.Tk()
win.title("惹沃班表小工具")
win.geometry("350x150")
#win.resizable(False,False)
win.config(background="black")

label_input=tk.Label(text="班表.csv檔路徑：",width=12,bg="black",fg="white")
label_input.grid(row=0,column=0,rowspan=2,sticky=tk.W)

label_input_path=tk.Label(bg="black",fg="white",wraplength=225,justify=tk.LEFT)
label_input_path.grid(row=0,column=1,columnspan=10,sticky=tk.W)

label_this_is=tk.Label(text="這是",bg="black",fg="white",wraplength=200,justify=tk.LEFT)
label_this_is.grid(row=2,column=0,sticky=tk.W)

label_year=tk.Label(text="年",bg="black",fg="white",wraplength=200,justify=tk.LEFT)
label_year.grid(row=2,column=2,sticky=tk.W)

label_month=tk.Label(text="月",bg="black",fg="white",wraplength=200,justify=tk.LEFT)
label_month.grid(row=2,column=4,sticky=tk.W)

label_sche=tk.Label(text="的班表",bg="black",fg="white",wraplength=200,justify=tk.LEFT)
label_sche.grid(row=2,column=6,sticky=tk.W)

textbox_year=tk.Entry(width=4)
textbox_year.grid(row=2,column=1,sticky=tk.W)

textbox_month=tk.Entry(width=2)
textbox_month.grid(row=2,column=3,sticky=tk.W)

textbox_name=tk.Entry(width=4)
textbox_name.grid(row=2,column=5,sticky=tk.W)

textbox_row=tk.Entry(width=10)
textbox_row.insert(tk.END,"在此輸入列數")
textbox_row.grid(row=10,column=0,sticky=tk.W)'''

output_list=[]
is_loaded=0

'''def btn_load():
    if 0 and not textbox_row.get().isnumeric():
        label_input_path.config(text="請告訴我你在哪一列哦！")
    else:
        csv_input_path = filedialog.askopenfilename()
        if csv_input_path != "":
            csv_input_filename = (os.path.basename(csv_input_path))  # get filename
            input_list = csv_to_list(csv_input_path)
            row_index = int(textbox_row.get())-1
            row = input_list[row_index]
            name = input_list[row_index][0]
            date_row = date_row_converter(input_list[3])
            event_row = input_list[4]
            current_year_and_month = get_year_and_month(csv_input_filename)
            global output_list
            output_list = create_output_list(date_row, row, event_row, current_year_and_month.year,
                                               current_year_and_month.month)
            label_input.config(text="班表.csv檔路徑：")
            label_input_path.config(text=csv_input_path)
            textbox_year.delete(0,100)
            textbox_year.insert(tk.END,str(current_year_and_month.year))
            textbox_month.delete(0,100)
            textbox_month.insert(tk.END,str(current_year_and_month.month))
            textbox_name.delete(0,100)
            textbox_name.insert(tk.END,str(name))
            global is_loaded
            is_loaded = 1'''


'''btn_load=tk.Button(command=btn_load,text="開啟檔案")
btn_load.grid(row=10,column=1,columnspan=3,sticky=tk.W)'''

'''def btn_save():
    if not is_loaded:
        label_input_path.config(text="尚未讀取檔案！")
    else:
        csv_output_path=filedialog.asksaveasfilename(initialfile=textbox_year.get()+"年"+
                                                     textbox_month.get()+"月"+
                                                     textbox_name.get()+"的班表", defaultextension=".csv")
        with open(csv_output_path,'w', newline='') as csv_output_file:
            writer = csv.writer(csv_output_file)
            writer.writerows(output_list)
            label_input.config(text="已輸出.csv檔至：")
            label_input_path.config(text=csv_output_path)'''

'''btn_save=tk.Button(text="輸出檔案",command=btn_save)
btn_save.grid(row=10,column=4,columnspan=3,sticky=tk.W)

win.mainloop()'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Ui_Dialog()
    ui.setupUi(MainWindow)

    MainWindow.show()
    ui.textbox_row.selectAll()

    sys.exit(app.exec_())