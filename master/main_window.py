from PyQt5.QtWidgets import QMainWindow
from ui_widget import UIWidget


class MainWindow(QMainWindow):
    """Overwrite the main window of PyQt for pygame integration."""
    def __init__(self, surface, controller, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui_widget = UIWidget(surface=surface, controller=controller, window=self)
        self.setCentralWidget(self.ui_widget)
        self.setWindowTitle('The Warehouse')

    def update_image(self, surface):
        """Update the image in the pygame window."""
        self.ui_widget.update_image(surface=surface)

