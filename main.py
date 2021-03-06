import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from task_editor import *


class ToolBar(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.productivity_button = QPushButton()
        self.productivity_stats = QLabel(f"", self.productivity_button)
        self.search_button = QPushButton()
        self.notification_button = QPushButton()
        self.menu_button = QPushButton()

        self.addWidget(self.productivity_button, alignment=QtCore.Qt.AlignLeft)
        self.addWidget(self.search_button)
        self.addWidget(self.notification_button)
        self.addWidget(self.menu_button)


class Today_Tasks_Page(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        self.title = QLabel("Today")
        self.tasksList = QListWidget()
        self.newTaskButton = New_Task_Button()
        self.taskEditor = task_editor()
        self.taskEditor.hide()

        vbox.addWidget(self.title)
        vbox.addWidget(self.tasksList)
        vbox.addWidget(self.newTaskButton)
        vbox.addWidget(self.taskEditor)
        self.setLayout(vbox)


class Task(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.name = ""
        self.type = ""
        self.shedle = [0, 0, 0, 0, 0, 0]
        self.nameLabel = QLabel(self.name)
        self.typeLabel = QLabel(self.type)
        self.shedleLabel = QLabel()

        self.setLayout(vbox)
        vbox.addWidget(self.nameLabel)
        vbox.addLayout(hbox)
        hbox.addWidget(self.typeLabel)
        hbox.addWidget(self.shedleLabel)

    def setTaskName(self, name):
        self.name = name
        self.nameLabel.setText(name)


# creating task widgets
class New_Task_Button(QPushButton):
    def __init__(self):
        super().__init__()
        self.clicked.connect(self.editTask)
        self.setText("New Task")

    def editTask(self):
        self.hide()
        self.parent().taskEditor.show()


class Task_Description(QTextEdit):
    class set_label_button(QPushButton):
        def __init__(self):
            super().__init__()

    def __init__(self):
        super().__init__()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        hbox1 = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        today_tasks_tab = QPushButton("Today")
        all_tasks_tab = QPushButton("All Tasks")
        self.toolbar = ToolBar()
        self.today_tasks_page = Today_Tasks_Page()
        all_tasks_list = QListWidget()
        self.tasks_pages = QTabWidget()
        # setup today tasks page
        self.tasks_pages.addTab(self.today_tasks_page, "Today")
        self.tasks_pages.addTab(all_tasks_list, "All Tasks")
        self.tasks_pages.tabBar().hide()
        self.tasks_pages.setStyleSheet("QTabWidget::pane { border: 0; }")

        today_tasks_tab.clicked.connect(self.move_to_today_tasks_page)

        hbox1.addLayout(vbox1)
        hbox1.addLayout(vbox2)
        vbox1.addWidget(today_tasks_tab)
        vbox1.addWidget(all_tasks_tab)
        vbox2.addLayout(self.toolbar)
        vbox2.addWidget(self.tasks_pages)
        vbox1.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(hbox1)

    def move_to_today_tasks_page(self):
        self.tasks_pages.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
