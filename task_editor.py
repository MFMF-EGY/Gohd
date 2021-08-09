import main
from PyQt5.QtWidgets import *


class task_editor(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox2 = QVBoxLayout()
        hbox2 = QHBoxLayout()
        taskname = QTextEdit()
        listButton = QComboBox()
        dateButton = QComboBox()
        reminderButton = QComboBox()
        addTaskButton = QPushButton()
        cancelButton = QPushButton()

        vbox.addWidget(taskname)
        vbox.addLayout(hbox)
        hbox.addWidget(listButton)
        hbox.addWidget(dateButton)
        hbox.addWidget(reminderButton)
        vbox2.addLayout(vbox)
        vbox2.addLayout(hbox2)
        hbox2.addWidget(addTaskButton)
        hbox2.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding) )
        hbox2.addWidget(cancelButton)
        self.setLayout(vbox2)
