from PyQt5.QtWidgets import QWidget, QPushButton, QInputDialog, QLineEdit, QScrollArea, QVBoxLayout,\
    QFormLayout, QGroupBox, QMessageBox, QErrorMessage

from gui.createItem import *
from gui.editItem import *
from functools import partial
from gui.startup import *


class UIWidget(QWidget):
    """Overwrite the UIWidget from PyQt to accommodate the pygame window and implement the UI."""
    def __init__(self, surface, controller, window, parent=None):
        super(UIWidget, self).__init__(parent)
        self.controller = controller
        self.window = window
        width = surface.get_width()
        height = surface.get_height()
        self.surface = surface.get_buffer().raw
        self.image = QtGui.QImage(self.surface, width, height, QtGui.QImage.Format_RGB32)
        self.full_ui_created = False
        self.item_button_list = []
        self.group_box = None
        self.form_layout = None
        self.scroll_area = None
        self.box_layout = None
        self.create_ui()

    def paintEvent(self, event):
        """Overwrite the built in paintEvent function."""
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.drawImage(0, 0, self.image)
        painter.end()

    def create_ui(self):
        self.startWindow = QtWidgets.QMainWindow()
        self.startWindow_ui = startup()
        self.startWindow.setWindowTitle('Create Warehouse')
        self.startWindow_ui.setupUi(self.startWindow)
        self.startWindow_ui.pushButton.clicked.connect(self.startWarehouseSize)

    def startWarehouseSize(self):
        width = self.startWindow_ui.lineEdit_2.text()
        height = self.startWindow_ui.lineEdit.text()
        self.controller.change_warehouse_size(int(width), int(height))
        self.delayed_ui()
        self.startWindow.close()

    def delayed_ui(self):
        """Create the rest of the UI after the warehouse size is set."""
        if not self.full_ui_created:
            warehouse_size_button = QPushButton('Edit Warehouse Size', self)
            warehouse_size_button.clicked.connect(self.change_warehouse_size)
            warehouse_size_button.resize(warehouse_size_button.sizeHint())
            warehouse_size_button.move(10, 510)
            warehouse_size_button.show()
            item_add_button = QPushButton('Add Item', self)
            item_add_button.clicked.connect(self.add_item)
            item_add_button.resize(item_add_button.sizeHint())
            item_add_button.move(550, 10)
            item_add_button.setFixedSize(200,30)
            item_add_button.show()
            pack_warehouse_button = QPushButton('Pack Warehouse', self)
            pack_warehouse_button.clicked.connect(self.controller.pack_warehouse)
            pack_warehouse_button.resize(pack_warehouse_button.sizeHint())
            pack_warehouse_button.move(222, 510)
            pack_warehouse_button.show()
            highlight_item_button = QPushButton('Find Item', self)
            highlight_item_button.clicked.connect(self.locate_item)
            highlight_item_button.resize(highlight_item_button.sizeHint())
            highlight_item_button.move(415, 510)
            highlight_item_button.show()
            self.group_box = QGroupBox('Items In Warehouse:')
            self.form_layout = QFormLayout()
            self.group_box.setLayout(self.form_layout)
            self.scroll_area = QScrollArea()
            self.scroll_area.setWidget(self.group_box)
            self.scroll_area.setWidgetResizable(True)
            self.scroll_area.setGeometry(500, 50, 0, 0)
            self.box_layout = QVBoxLayout(self)
            self.box_layout.addWidget(self.scroll_area)
            self.box_layout.setContentsMargins(500, 50, 0, 0)
            self.full_ui_created = True

    def update_image(self, surface):
        """Update the pygame surface on the widget window."""
        width = surface.get_width()
        height = surface.get_height()
        self.surface = surface.get_buffer().raw
        self.image = QtGui.QImage(self.surface, width, height, QtGui.QImage.Format_RGB32)

    def change_warehouse_size(self):
        """React to edit warehouse button."""
        user_input, pressed_ok = QInputDialog.getText(self, "Width", "Enter Warehouse Width:", QLineEdit.Normal, "")
        if pressed_ok and user_input != '':
            width = user_input
            user_input, pressed_ok = QInputDialog.getText(self, "Height", "Enter Warehouse Height:", QLineEdit.Normal, "")
            if pressed_ok and user_input != '':
                height = user_input
                if int(width) and int(height):
                    self.delayed_ui()
                    self.controller.change_warehouse_size(int(width), int(height))

    def remove_item(self):
        """React to remove an item button."""
        user_input, pressed_ok = QInputDialog.getText(self, "Remove Item", "Enter Item ID:", QLineEdit.Normal, "")
        if pressed_ok and user_input != '':
            self.controller.remove_item(user_input)
            while self.form_layout.rowCount() > 0:
                self.form_layout.removeRow(0)
            for item in self.controller.item_list:
                item_button = QPushButton(item.item_id, self)
                item_button.clicked.connect(self.item_button_click)
                item_button.resize(item_button.sizeHint())
                self.form_layout.addRow(item_button)

    def add_item(self):
        """React to add item button."""
        self.createWindow = QtWidgets.QMainWindow()
        self.createWindow_ui = CreateItem()
        self.createWindow_ui.setupUi(self.createWindow)
        self.createWindow_ui.pushButton.clicked.connect(self.createItem)
        self.createWindow_ui.pushButton_2.clicked.connect(self.cancelCreateWindow)
        self.createWindow.show()

    def cancelCreateWindow(self):
        """Cancel creating an item."""
        self.createWindow.close()

    def createItem(self):
        """Create an item window for user input."""
        item_parts = []
        item_parts.append(self.createWindow_ui.lineEdit_4.text())
        item_parts.append(self.createWindow_ui.lineEdit.text())
        item_parts.append(self.createWindow_ui.lineEdit_5.text())
        item_parts.append(self.createWindow_ui.lineEdit_3.text())
        item_parts.append(self.createWindow_ui.lineEdit_2.text())
        not_ints = True
        try:
            int(item_parts[2])
            int(item_parts[3])
            int(item_parts[4])
        except:
            not_ints = False
            self.display_error("Invalid entry in create item.")
        if not_ints:
            self.controller.add_item(item_parts=item_parts)
            while self.form_layout.rowCount() > 0:
                self.form_layout.removeRow(0)
            for item in self.controller.item_list:
                button_str = item.name + ' - ID: ' + item.item_id
                item_button = QPushButton(button_str, self)
                item_button.clicked.connect(self.item_button_click)
                item_button.resize(item_button.sizeHint())
                self.form_layout.addRow(item_button)
            self.createWindow.setWindowTitle('Create New Item')
        self.createWindow.close()

    def item_button_click(self):
        """React to selecting an item, display info about item and ask for changes."""
        button = self.sender()
        button_text = (button.text().split(" "))[-1]
        for item in list(self.controller.item_list):
            if item.item_id == button_text:
                message_box_text = "Item ID: " + item.item_id + "\nItem Name: " + item.name + "\nItem Quantity: " \
                                   + str(item.quantity) + "\nItem Length: " + str(item.width) + "\nItem Width: " \
                                   + str(item.length) + "\n\nWould you like to make changes to this item?"
                message_box = QMessageBox.question(self, 'Item Details', message_box_text,
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if message_box == QMessageBox.Yes:
                    self.editWindow = QtWidgets.QMainWindow()
                    self.editWindow_ui = EditItem()
                    self.editWindow_ui.setupUi(self.editWindow)
                    self.editWindow_ui.pushButton_2.clicked.connect(self.cancelEditWindow)
                    button = self.sender()
                    button_text = (button.text().split(" "))[-1]
                    for item in list(self.controller.item_list):
                        if item.item_id == button_text:
                            # Fill text boxes
                            self.editWindow_ui.lineEdit.setText(str(item.name))
                            self.editWindow_ui.lineEdit_4.setText(str(item.item_id))
                            self.editWindow_ui.lineEdit_5.setText(str(item.quantity))
                            self.editWindow_ui.lineEdit_2.setText(str(item.length))
                            self.editWindow_ui.lineEdit_3.setText(str(item.width))
                    self.editWindow_ui.pushButton_3.clicked.connect(partial(self.deleteItem,item.item_id))
                    self.editWindow_ui.pushButton.clicked.connect(partial(self.updateItem,item))
                    self.editWindow.setWindowTitle(item.name)

                    self.editWindow.show()

    def cancelEditWindow(self):
        """Cancel the editing an item window."""
        self.editWindow.close()

    def deleteItem(self, itemID):
        """Prompt the user to remove an item from the warehouse."""
        self.controller.remove_item(itemID)
        while self.form_layout.rowCount() > 0:
            self.form_layout.removeRow(0)
        for item in self.controller.item_list:
            item_button = QPushButton(item.item_id, self)
            item_button.clicked.connect(self.item_button_click)
            item_button.resize(item_button.sizeHint())
            self.form_layout.addRow(item_button)

        self.editWindow.close()

    def updateItem(self, item):
        """Change the attributes of an item from user input."""
        self.controller.item_list.remove(item)
        item.item_id = self.editWindow_ui.lineEdit_4.text()
        item.name = self.editWindow_ui.lineEdit.text()
        item.quantity = self.editWindow_ui.lineEdit_5.text()
        item.length = self.editWindow_ui.lineEdit_2.text()
        item.width = self.editWindow_ui.lineEdit_3.text()
        item_parts = []
        item_parts.append(item.item_id)
        item_parts.append(item.name)
        item_parts.append(item.quantity)
        item_parts.append(item.width)
        item_parts.append(item.length)
        self.controller.add_item(item_parts=item_parts)
        while self.form_layout.rowCount() > 0:
            self.form_layout.removeRow(0)
        for item in self.controller.item_list:
            button_str = item.name + ' - ID: ' + item.item_id
            item_button = QPushButton(button_str, self)
            item_button.clicked.connect(self.item_button_click)
            item_button.resize(item_button.sizeHint())
            self.form_layout.addRow(item_button)

        self.editWindow.close()

    def locate_item(self):
        """Ask the user for an item id and then call the locate function."""
        user_input, pressed_ok = QInputDialog.getText(self, "Find Item", "Enter Item ID:", QLineEdit.Normal, "")
        if pressed_ok and user_input != '':
            self.controller.locate_item(matching_id=user_input)

    def display_error(self, message):
        """Display error message in qt window."""
        error_message = QErrorMessage(self)
        error_message.showMessage(message)
        error_message.setWindowTitle("Warehouse Error")
