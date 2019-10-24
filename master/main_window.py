from PyQt5.QtWidgets import QMainWindow
from ui_widget import UIWidget


class MainWindow(QMainWindow):
    def __init__(self, surface, controller, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui_widget = UIWidget(surface=surface, controller=controller, window=self)
        self.setCentralWidget(self.ui_widget)

    def update_image(self, surface):
        self.ui_widget.update_image(surface=surface)

