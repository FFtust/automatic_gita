import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import autopiano

 
class mwindow(QWidget, autopiano.Ui_MainWindow):
    def __init__(self):
        super(mwindow, self).__init__()
        self.setupUi(self)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mwindow()
    w.show()
    sys.exit(app.exec_())