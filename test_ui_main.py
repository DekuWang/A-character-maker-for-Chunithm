import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile
from ui.test_ui import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.get_directory)
    
    def get_directory(self):
        path = QFileDialog.getExistingDirectory(parent = self, caption = "选个文件", options = ".png")
        print(path)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
