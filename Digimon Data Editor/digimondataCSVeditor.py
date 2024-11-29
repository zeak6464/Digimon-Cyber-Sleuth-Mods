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

def search_for_file_path():
    try:
        currdir = os.getcwd()
        tempdir = filedialog.askopenfilename(
            parent=root, 
            initialdir=currdir, 
            title='Please select a csv file',
            filetypes=[("CSV files", "*.csv")]
        )
        if len(tempdir) > 0:
            print("Selected file: %s" % tempdir)
            return tempdir
        return None
    except Exception as e:
        print(f"Error selecting file: {str(e)}")
        return None

try:
    file_name = search_for_file_path()
    if not file_name:
        print("No file selected. Exiting...")
        sys.exit(1)
    
    headers = pd.read_csv(file_name)
    output_filename = "Digimon_Data_Mod"
    dir_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "digimondata")
except Exception as e:
    print(f"Error initializing: {str(e)}")
    sys.exit(1)

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
        self.setStyleSheet('font-size: 12px;')
        
        # set table dimension
        nRows, nColumns = self.df.shape
        self.setColumnCount(nColumns)
        self.setRowCount(nRows)

        # Set headers and style
        self.setHorizontalHeaderLabels(list(headers))
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().setStretchLastSection(True)
        
        # Set column widths
        for i in range(self.columnCount()):
            self.setColumnWidth(i, 150)

        self.setItemDelegateForColumn(1, FloatDelegate())

        # data insertion
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                item = QTableWidgetItem(str(self.df.iloc[i, j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.setItem(i, j, item)

        self.cellChanged[int, int].connect(self.updateDF)   

    def updateDF(self, row, column):
        text = self.item(row, column).text()
        self.df.iloc[row, column] = text
        
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_C and (event.modifiers() & Qt.ControlModifier):
            self.copied_cells = sorted(self.selectedIndexes())
        elif event.key() == Qt.Key_V and (event.modifiers() & Qt.ControlModifier):
            r = self.currentRow() - self.copied_cells[0].row()
            c = self.currentColumn() - self.copied_cells[0].column()
            for cell in self.copied_cells:
                self.setItem(cell.row() + r, cell.column() + c, QTableWidgetItem(cell.data()))

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
        button_export.setStyleSheet('font-size: 12px')
        button_export.clicked.connect(self.export_to_csv)
        mainLayout.addWidget(button_export)
        

        button_mod = QPushButton('Make Mod file')
        button_mod.setStyleSheet('font-size: 12px')
        button_mod.clicked.connect(self.makemod)
        mainLayout.addWidget(button_mod) 

        self.setLayout(mainLayout)
        
        
    def export_to_csv(self):
        try:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv")],
                initialfile=os.path.basename(file_name)
            )
            if save_path:
                self.table.df.to_csv(save_path, index=False)
                print(f'CSV file exported successfully to: {save_path}')
        except Exception as e:
            print(f"Error exporting CSV: {str(e)}")
    
    def makemod(self):
        try:
            if not os.path.exists(dir_name):
                print(f"Error: Directory {dir_name} does not exist")
                return
                
            save_path = filedialog.asksaveasfilename(
                defaultextension=".zip",
                filetypes=[("ZIP files", "*.zip")],
                initialfile=f"{output_filename}.zip"
            )
            if save_path:
                base_path = os.path.splitext(save_path)[0]
                shutil.make_archive(base_path, 'zip', dir_name)
                print(f'Mod file created successfully at: {save_path}')
        except Exception as e:
            print(f"Error creating mod file: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = DFEditor()
    demo.show()
    
    sys.exit(app.exec_())
