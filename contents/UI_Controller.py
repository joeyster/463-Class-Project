
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
from gui.rough import *

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
		pass


	def removeItem(self):
		""" Removes an item from the database """
		pass


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
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

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
		pass


	def removeItem(self):
		""" Removes an item from the database """
		pass


	def drawWarehouse(self, warehouse_mat):
		""" Pass in a warehouse matrix with all the current locations of the items in the warehouse """
		pass


	def consolidateWarehouse(self):
		""" Will consolidate all the items in the warehouse. Focuses on saving as much space as possible """
		pass