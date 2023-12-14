import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox

class TodoList(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.title = QLabel('Todo List')
        self.title.setStyleSheet('font-size: 20px;')

        self.layout.addWidget(self.title)

        self.description = QTextEdit()
        self.description.setPlaceholderText('Enter your task here...')
        self.layout.addWidget(self.description)

        self.add_button = QPushButton('Add Task')
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.task_list = QTextEdit()
        self.task_list.setReadOnly(True)
        self.layout.addWidget(self.task_list)

        self.clear_button = QPushButton('Clear Tasks')
        self.clear_button.clicked.connect(self.clear_tasks)
        self.layout.addWidget(self.clear_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Todo List')
        self.show()

    def add_task(self):
        task = self.description.toPlainText()
        if task:
            self.task_list.append(task)
            self.description.clear()
        else:
            QMessageBox.warning(self, 'Error', 'Please enter a task')

    def clear_tasks(self):
        self.task_list.clear()

def main():
    app = QApplication(sys.argv)
    todo_list = TodoList()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()