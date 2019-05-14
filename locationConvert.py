import sys
import os
import traceback
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIntValidator, QIcon
from PyQt5 import QtCore
from module import main, fileRW, convert
from module.thread import Actions
import qdarkstyle

class MyFrom(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.fileRW = fileRW.fileClass()
        self.ui.select_file.clicked.connect(self.getFileName)
        self.ui.start_convert.clicked.connect(self.convertLocation)
        self.ui.clear.clicked.connect(self.clearTextBrowser)
        self.ui.export_file.clicked.connect(self.exportFile)
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    def convertLocation(self):
        self.city = self.ui.city_lineEdit.text()
        self.location = self.ui.location_lineEdit.text()        
        self.main = Actions(self.ui, self.filePath, self.city, self.location)
        self.main.returnDF.connect(self.receiveDF)
        #self.main.show()
        #self.main.exec_()
    
    def receiveDF(self, df):
        self.df = df
        self.exportEnable()
        self.ui.export_file.setEnabled(True)

    def clearTextBrowser(self):
        self.filePath = []
        self.ui.select_textBrowser.clear()
        self.ui.city_lineEdit.setEnabled(False)
        self.ui.location_lineEdit.setEnabled(False)
        self.ui.export_file.setEnabled(False)
        self.ui.convert_lable.clear()

    def getFileName(self):
        self.filePath = self.fileRW.read_one_file()
        #self.fileName = os.path.basename(self.filePath)
        self.ui.select_textBrowser.setText(os.path.basename(self.filePath))
        self.ui.convert_lable.setText('')
        self.ui.export_lable.setText('')
        self.convertEnable()
    
    def convertEnable(self):
        if self.ui.select_textBrowser.toPlainText() != '':
            self.ui.city_lineEdit.setEnabled(True)
            self.ui.location_lineEdit.setEnabled(True)
            self.ui.start_convert.setEnabled(True)
    
    def exportEnable(self):
        if self.ui.convert_lable.text() == '转换完成！':
            self.ui.export_file.setEnabled(True)
    
    def exportFile(self):
        self.path = self.fileRW.write_file()
        try:
            self.df.to_excel(self.path, index = None, engine = 'xlsxwriter')
            self.ui.export_lable.setText('导出完成！')
            self.init()
        except:
            traceback.print_exc()
    
    def init(self):
        self.filePath = []
        self.ui.select_textBrowser.clear()
        self.ui.city_lineEdit.setEnabled(False)
        self.ui.location_lineEdit.setEnabled(False)
        self.ui.start_convert.setEnabled(False)
        self.ui.export_file.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w = MyFrom()
    app.setWindowIcon(QIcon('logo.ico'))
    w.show()
    sys.exit(app.exec_())