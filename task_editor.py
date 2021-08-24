import main
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from datetime import datetime
import calendar

class task_editor(QWidget):
    class Shedular(QWidget):
        global currentYear, currentMonth

        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        def __init__(self):
            super().__init__()
            self.setGeometry(300, 300, 450, 300)
            
            self.calendar = QCalendarWidget(self)
            # self.calendar.move(20, 20)
            self.calendar.setGridVisible(True)

            self.calendar.setMinimumDate(QtCore.QDate(currentYear, currentMonth - 1, 1))
            self.calendar.setMaximumDate(
                QtCore.QDate(currentYear, currentMonth + 1, calendar.monthrange(currentYear, currentMonth)[1]))

            self.calendar.setSelectedDate(QtCore.QDate(currentYear, currentMonth, 1))

    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox2 = QVBoxLayout()
        hbox2 = QHBoxLayout()
        self.taskname = QTextEdit()
        self.listButton = QPushButton()
        self.dateButton = QPushButton()
        self.reminderButton = QPushButton()
        self.shedular = self.Shedular()
        self.addTaskButton = QPushButton("Add Task")
        cancelButton = QPushButton("Cancel")
        self.taskname.keyReleaseEvent = self.addTaskByEnterKey
        self.taskname.keyPressEvent = self.textEditBehavior
        self.taskname.textChanged.connect(self.setAddTaskButtonState)
        self.addTaskButton.setDisabled(True)
        cancelButton.clicked.connect(self.cancel)
        self.addTaskButton.clicked.connect(self.addTask)

        vbox.addWidget(self.taskname)
        vbox.addLayout(hbox)
        hbox.addWidget(self.listButton)
        hbox.addWidget(self.dateButton)
        hbox.addWidget(self.reminderButton)
        vbox2.addLayout(vbox)
        vbox2.addLayout(hbox2)
        hbox2.addWidget(self.addTaskButton)
        hbox2.addWidget(cancelButton)
        hbox2.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(vbox2)

    def textEditBehavior(self, e):
        if not e.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
            QTextEdit.keyPressEvent(self.taskname, e)

    def addTaskByEnterKey(self, e):
        if self.taskname.toPlainText():
            if e.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
                self.addTask()

    def setAddTaskButtonState(self):
        if self.taskname.toPlainText():
            self.addTaskButton.setDisabled(False)
        else:
            self.addTaskButton.setDisabled(True)

    def cancel(self):
        self.taskname.setText("")
        self.hide()
        self.parent().newTaskButton.show()

    def addTask(self):
        task = main.Task()
        task.setTaskName(self.taskname.toPlainText())
        taskItem = QListWidgetItem()
        self.parent().tasksList.addItem(taskItem)
        self.parent().tasksList.setItemWidget(taskItem, task)
        taskItem.setSizeHint(task.sizeHint())
        self.cancel()
