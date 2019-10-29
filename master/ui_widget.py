from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QInputDialog, QLineEdit, QScrollArea, QVBoxLayout, QLabel, \
    QHBoxLayout, QFrame, QTableWidget, QGridLayout, QFormLayout, QGroupBox, QLayoutItem, QMessageBox

from gui.createItem import *
from gui.editItem   import *
import pygame
from functools import partial

class UIWidget(QWidget):
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
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.drawImage(0, 0, self.image)
        painter.end()

    def create_ui(self):
        warehouse_size_button = QPushButton('Edit Warehouse Size', self)
        warehouse_size_button.clicked.connect(self.change_warehouse_size)
        warehouse_size_button.resize(warehouse_size_button.sizeHint())
        warehouse_size_button.move(10, 510)

    def delayed_ui(self):
        if not self.full_ui_created:
            item_add_button = QPushButton('Add Item', self)
            item_add_button.clicked.connect(self.add_item)
            item_add_button.resize(item_add_button.sizeHint())
            item_add_button.move(550, 10)
            item_add_button.show()
            item_remove_button = QPushButton('Remove Item', self)
            item_remove_button.clicked.connect(self.remove_item)
            item_remove_button.resize(item_remove_button.sizeHint())
            item_remove_button.move(675, 10)
            item_remove_button.show()
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
        width = surface.get_width()
        height = surface.get_height()
        self.surface = surface.get_buffer().raw
        self.image = QtGui.QImage(self.surface, width, height, QtGui.QImage.Format_RGB32)

    def change_warehouse_size(self):
        user_input, pressed_ok = QInputDialog.getText(self, "Width", "Enter Warehouse Width:", QLineEdit.Normal, "")
        if pressed_ok and user_input != '':
            width = user_input
            user_input, pressed_ok = QInputDialog.getText(self, "Height", "Enter Warehouse Height:", QLineEdit.Normal,
                                                          "")
            if pressed_ok and user_input != '':
                height = user_input
                if int(width) and int(height):
                    self.delayed_ui()
                    self.controller.change_warehouse_size(int(width), int(height))

    def remove_item(self):
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

    def add_item(self, set_default_values=True, default_values=("", "", "", "", "")):
        if set_default_values:
            default_values = ["", "", "", "", ""]
        item_parts = []
        check_fail = False
        
        self.createWindow = QtWidgets.QMainWindow()
        self.createWindow_ui = CreateItem()
        self.createWindow_ui.setupUi(self.createWindow)
        self.createWindow_ui.pushButton.clicked.connect(self.createItem)
        self.createWindow_ui.pushButton_2.clicked.connect(self.cancelCreateWindow)
        self.createWindow.show()

    def cancelCreateWindow(self):
        self.createWindow.close()

    def createItem(self):
        item_parts = []
        item_parts.append(self.createWindow_ui.lineEdit_4.text())
        item_parts.append(self.createWindow_ui.lineEdit.text())
        item_parts.append(self.createWindow_ui.lineEdit_5.text())
        item_parts.append(self.createWindow_ui.lineEdit_2.text())
        item_parts.append(self.createWindow_ui.lineEdit_3.text())

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

        button = self.sender()
        button_text = (button.text().split(" "))[-1]
        for item in list(self.controller.item_list):
            if item.item_id == button_text:
                message_box_text = "Item ID: " + item.item_id + "\nItem Name: " + item.name + "\nItem Quantity: " \
                                   + str(item.quantity) + "\nItem Width: " + str(item.width) + "\nItem Length: " \
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
        self.editWindow.close()

    def deleteItem(self, itemID):
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
        user_input, pressed_ok = QInputDialog.getText(self, "Find Item", "Enter Item ID:", QLineEdit.Normal, "")
        if pressed_ok and user_input != '':
            self.controller.locate_item(matching_id=user_input)



# Todo: maybe switch inputs to these classes, they are multiple inputs per dialog box
class WarehouseDialog(QWidget):
    def __init__(self):
        super(WarehouseDialog, self).__init__()
        width_label = QLabel("Width:")
        length_label = QLabel("Length:")

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")


class ItemDialog(QWidget):
    def __init__(self):
        super(ItemDialog, self).__init__()
        id_label = QLabel("Item ID:")
        name_label = QLabel("Item Name:")
        width_label = QLabel("Item Width:")
        length_label = QLabel("Item Length:")
        id_input = QLineEdit()

