import file_manager
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import QColor, QIcon, QPixmap

'''
To build App into .exe
pyinstaller --noconsole --icon=icon.ico  -F main.py --name='Projects Manager'
'''

class DemoApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./project_manager.ui', self)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.search_field.textChanged.connect(self.handleSearch)
        self.search_field.returnPressed.connect(self.handleSearch)
        self.search_button.clicked.connect(self.handleSearch)
        self.list_view.setSpacing(5)
        self.list_view.itemClicked.connect(self.handleClickItem)
        self.populate_list()
        self.all_radio.setChecked(True)

        self.all_radio.lang = "all"
        self.python_radio.lang = "py"
        self.dart_radio.lang = "dart"
        self.rust_radio.lang = "rs"
        self.html_radio.lang = "html"
        self.css_radio.lang = "css"
        self.js_radio.lang = "js"
        self.c_radio.lang = "c"
        self.ts_radio.lang = "tsx"

        self.all_radio.toggled.connect(self.handleRadio)
        self.python_radio.toggled.connect(self.handleRadio)
        self.dart_radio.toggled.connect(self.handleRadio)
        self.rust_radio.toggled.connect(self.handleRadio)
        self.html_radio.toggled.connect(self.handleRadio)
        self.css_radio.toggled.connect(self.handleRadio)
        self.js_radio.toggled.connect(self.handleRadio)
        self.c_radio.toggled.connect(self.handleRadio)
        self.ts_radio.toggled.connect(self.handleRadio)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape: 
            self.close()

    def handleClickItem(self, item):
        os.startfile(item.value.get(0))


    def handleSearch(self):
        query = self.search_field.text()
        filter_list = file_manager.search_projects(query, file_manager.get_all_projects())
        self.populate_list(project_list=filter_list, default=False)
    

    def handleRadio(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            if radio_button.lang == "all":
                self.populate_list()
            else:
                filter_list = file_manager.filter_projects_by_language(radio_button.lang)
                self.populate_list(project_list=filter_list, default=False)


    def populate_list(self, project_list=[], default=True):
        import constants
        self.list_view.clear() 
        if default:
            project_list = file_manager.get_all_projects()
        for projects in project_list:
            item = QListWidgetItem(projects[2])
            pixmap = QPixmap("./icons/placeholder_logo.png")
            icon = QIcon(constants.logos.get(projects[1], pixmap))
            item.setIcon(icon)
            item.value = projects
            self.list_view.addItem(item)
        self.count_label.setText(f"Showing {self.list_view.count()} Projects")
    
    def get_list_items(self):
        new_list = []
        for i in range(self.list_view.count()-1):
            new_list.append(self.list_view.item(0).value)
        return new_list


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

app = QApplication(sys.argv)
demo = DemoApp()
demo.show()

try:
    sys.exit(app.exec_())
except:
    print("Closing Window")