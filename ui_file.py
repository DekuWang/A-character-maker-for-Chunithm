"""
All about UI
"""
# First-party module
import sys

# Third-party module
from PyQt6.QtWidgets import (QApplication, QWidget, QMessageBox,
                             QToolTip, QPushButton)
from PyQt6.QtGui import QFont


class MainPage(QWidget):
    """
    initial page with function button, 
    creaet character work
    create character
    create nameplate
    craete trophy
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Including all components for the main page
        """
        QToolTip.setFont(QFont('SansSerif',10))

        self.setToolTip("This is a <i>QWidget</i> widget")

        btn = QPushButton('Button', self)
        btn.setToolTip("This is a button")
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        btn.clicked.connect(self.print_sth)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Tooltips')
        self.show()

        self.center()

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, "Message", "you sure?",
                                     QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.Yes)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def print_sth(self):
        print(123421)

def main():
    app = QApplication(sys.argv)
    mp = MainPage()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
