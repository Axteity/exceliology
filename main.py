import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from UI.mainmenu import Ui_MainWindow

# Application instance creation
app = QApplication(sys.argv)

# Main window instance creation
window = QMainWindow()

# UI widgets instances creation
ui = Ui_MainWindow()
ui.setupUi(window)

# Displaying window
window.show()

# Starting event handler loop
sys.exit(app.exec())