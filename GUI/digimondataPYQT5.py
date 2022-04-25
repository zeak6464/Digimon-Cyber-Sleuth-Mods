import sys
import pandas as pd
import os
import tkinter
from tkinter import filedialog


from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, \
                            QPushButton, QItemDelegate, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

root = tkinter.Tk()
root.withdraw()

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a csv file')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir

file_name = search_for_file_path()
headers = pd.read_csv(file_name)

class FloatDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__()

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QDoubleValidator())
        return editor

class TableWidget(QTableWidget):
    def __init__(self, df):
        super().__init__()
        self.df = df
        self.setStyleSheet('font-size: 10px;')
        
        

        # set table dimension
        nRows, nColumns = self.df.shape
        self.setColumnCount(nColumns)
        self.setRowCount(nRows)

        self.setHorizontalHeaderLabels(list(headers))
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setItemDelegateForColumn(1, FloatDelegate())

        # data insertion
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

        self.cellChanged[int, int].connect(self.updateDF)   

    def updateDF(self, row, column):
        text = self.item(row, column).text()
        self.df.iloc[row, column] = text

class DFEditor(QWidget):
    data = pd.read_csv(file_name)

    df = pd.DataFrame(data)

    def __init__(self):
        super().__init__()
        self.resize(1200, 800)

        mainLayout = QVBoxLayout()

        self.table = TableWidget(DFEditor.df)
        mainLayout.addWidget(self.table)

        button_print = QPushButton('Display DF')
        button_print.setStyleSheet('font-size: 10px')
        button_print.clicked.connect(self.print_DF_Values)
        mainLayout.addWidget(button_print)

        button_export = QPushButton('Export to CSV file')
        button_export.setStyleSheet('font-size: 10px')
        button_export.clicked.connect(self.export_to_csv)
        mainLayout.addWidget(button_export)     

        self.setLayout(mainLayout)
        
    def print_DF_Values(self):
        print(self.table.df)

    def export_to_csv(self):
        self.table.df.to_csv('Data export.csv', index=False)
        print('CSV file exported.')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = DFEditor()
    demo.show()
    
    sys.exit(app.exec_())
