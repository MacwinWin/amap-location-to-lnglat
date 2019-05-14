import sys
import time
import traceback

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)
import pandas as pd
import requests

TIME_LIMIT = 100

class convertClass(QThread):
    
    countChanged = pyqtSignal(int)
    returnDF = pyqtSignal(pd.DataFrame)
    close = pyqtSignal(int)
    def __init__(self, filePath, city, location):
        super(convertClass, self).__init__()
        self.url = "https://restapi.amap.com/v3/place/text"
        self.df = pd.read_excel(filePath)
        self.df['经纬度'] = ''
        self.city = city
        self.location = location
    
    def run(self):
        i = 0
        try:
            for index, row in self.df.iterrows():
                city = row[self.city]
                item = row[self.location]
                data = {
                'key': 'xxxxxxxxxxxxx', #在高德地图开发者平台申请的key，需要替换为自己的key
                'keywords': item,
                'city': city,
                'types':'普通地名',
                'citylimit':'true'
                }
                r = requests.get(self.url, params=data).json()
                try:
                    i += 1
                    lnglat = r['pois'][0]['location']
                    self.df.loc[index, '经纬度'] = lnglat
                except:
                    traceback.print_exc()
                    pass
                finally:
                    count = i / self.df.shape[0] * 100
                    self.countChanged.emit(int(count))
            self.returnDF.emit(self.df)
            self.close.emit(1)
        except:
            traceback.print_exc()
            self.close.emit(0)
        #return self.df

class Actions(QDialog):
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.
    """
    returnDF = pyqtSignal(pd.DataFrame)
    def __init__(self, ui, filePath, city, location):
        super().__init__()
        self.ui = ui
        self.filePath = filePath
        self.city = city
        self.location = location
        self.initUI()
        
    def initUI(self):
        # 阻塞父窗口
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle('Progress Bar')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.show()
        self.calc = convertClass(self.filePath, self.city, self.location)
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.returnDF.connect(self.returnDf)
        self.calc.close.connect(self.closeWindow)
        self.calc.start()
    
    def closeWindow(self, value):
        if value == 1:
            self.ui.convert_lable.setText('转换完成！')
        elif value == 0:
            self.ui.export_file.setEnabled(False)
            self.ui.convert_lable.setText('转换失败！')
        self.close()
    
    def returnDf(self, df):
        self.returnDF.emit(df)

    def onCountChanged(self, value):
        self.progress.setValue(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Actions()
    sys.exit(app.exec_())