
#  ______   __  __     ______        __  __     __     ______   ______     __  __     ______     __   __    
# /\__  _\ /\ \_\ \   /\  ___\      /\ \/ /    /\ \   /\__  _\ /\  ___\   /\ \_\ \   /\  ___\   /\ "-.\ \   
# \/_/\ \/ \ \  __ \  \ \  __\      \ \  _"-.  \ \ \  \/_/\ \/ \ \ \____  \ \  __ \  \ \  __\   \ \ \-.  \  
#    \ \_\  \ \_\ \_\  \ \_____\     \ \_\ \_\  \ \_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\\"\_\ 
#     \/_/   \/_/\/_/   \/_____/      \/_/\/_/   \/_/     \/_/   \/_____/   \/_/\/_/   \/_____/   \/_/ \/_/ 
#                                                                                                          
# UI_Controller.py
#
# Dependencies
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from gui.main import *
from item import *
import backend_functions

###########################################################################################################


class Warehouse_Gui(QtWidgets.QMainWindow):
	""" Class creates the GUI for The Kitchen's warehouse application. Includes GUI creation as well as defines all
	call back functions """

	def __init__(self):
		""" Class Constructor. Calls super constructor """
		super().__init__(self)
		

	def launch(self):
		""" This call will launch the GUI application. Begins the event loop and waits for user interaction """
		pass


	def addItem(self):
		""" Passes in an item object that will be added to the GUI """
		# Will pull all from the create item window
		backend_function.addItem(Item(createItem.item.name,
			createItem.item.id,
			createItem.item.length, 
			createItem.item.width
		))


	def removeItem(self):
		""" Removes an item from the database """
		# Will delete object name in editItem Window
		backend_functions.removeItem(editItem.item)


	def drawWarehouse(self, warehouse_mat):
		""" Pass in a warehouse matrix with all the current locations of the items in the warehouse """
		pass


	def consolidateWarehouse(self):
		""" Will consolidate all the items in the warehouse. Focuses on saving as much space as possible """
		pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())