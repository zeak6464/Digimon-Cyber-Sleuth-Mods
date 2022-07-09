import sys
import pandas as pd
import os
import tkinter
import shutil
from tkinter import filedialog


from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, \
                            QPushButton, QItemDelegate, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

root = tkinter.Tk()
root.title('Digimon Data Editor')
root.withdraw()

file_name = "./digimondata/modfiles/data/digimon_farm_para.mbe/digimon.csv"
headers = pd.read_csv(file_name)
back_up = "./backup/digimon.csv"
output_filename = "digimon_farm_para mod"
dir_name = "./digimondata"

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


        button_export = QPushButton('Export to CSV file')
        button_export.setStyleSheet('font-size: 10px')
        button_export.clicked.connect(self.export_to_csv)
        mainLayout.addWidget(button_export)

        button_mod = QPushButton('Make Mod file')
        button_mod.setStyleSheet('font-size: 10px')
        button_mod.clicked.connect(self.makemod)
        mainLayout.addWidget(button_mod) 

        self.setLayout(mainLayout)
        

    def export_to_csv(self):
        self.table.df.to_csv(file_name, index=False)
        print('CSV file exported.')
        f = open(file_name)
        f.close()
    
    def makemod(self):
        shutil.make_archive(output_filename, 'zip', dir_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = DFEditor()
    demo.show()
    
    sys.exit(app.exec_())
