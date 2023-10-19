from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QListWidget, QWidget, QFrame, QLineEdit, QPushButton, QHBoxLayout, QListWidgetItem, QLabel

class SagTaraf(QWidget):
    def __init__(self):
        super().__init__()
        self.todo_items = []

        self.initUI()
        self.load_data()

    def initUI(self):
        self.todo_list = QListWidget(self)
        self.new_todo_edit = QLineEdit(self)
        self.add_button = QPushButton('Ekle', self)
        self.delete_button = QPushButton('Sil', self)

        separator = QFrame(self)
        separator.setFrameShape(QFrame.VLine)
        separator.setFrameShadow(QFrame.Sunken)

        layout = QVBoxLayout()
        title_label = QLabel('TO-DO LIST', self)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        layout.addWidget(self.todo_list)

        todo_layout = QHBoxLayout()
        todo_layout.addWidget(self.new_todo_edit)
        todo_layout.addWidget(self.add_button)
        todo_layout.addWidget(self.delete_button)
        layout.addLayout(todo_layout)
        
        layout.addWidget(separator)

        # Label ekleyerek TODO listesinin altına ekle
        version_label = QLabel('v1.0 QuartzzDev <3', self)
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setStyleSheet("font-size: 10px; color: gray;")
        layout.addWidget(version_label)

        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_todo)
        self.delete_button.clicked.connect(self.delete_todo)
        self.todo_list.itemChanged.connect(self.todo_item_changed)

    def add_todo(self):
        todo_text = self.new_todo_edit.text()
        if todo_text:
            self.todo_items.append({'text': todo_text, 'done': False})
            self.update_todo_list()
            self.new_todo_edit.clear()
            self.save_data()

    def delete_todo(self):
        selected_item = self.todo_list.currentItem()
        if selected_item:
            del self.todo_items[self.todo_list.currentRow()]
            self.update_todo_list()
            self.save_data()

    def update_todo_list(self):
        self.todo_list.clear()
        for item in self.todo_items:
            todo_item = QListWidgetItem(item['text'], self.todo_list)
            todo_item.setFlags(todo_item.flags() | Qt.ItemIsUserCheckable)  # User checkable item
            todo_item.setCheckState(Qt.Unchecked if not item['done'] else Qt.Checked)

    def todo_item_changed(self, item):
        index = self.todo_list.indexFromItem(item).row()
        self.todo_items[index]['done'] = item.checkState() == Qt.Checked
        self.save_data()

    def load_data(self):
        try:
            with open('todo.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    todo_text, todo_done = line.strip().split(':')
                    todo_done = True if todo_done.strip() == 'True' else False
                    self.todo_items.append({'text': todo_text, 'done': todo_done})
        except FileNotFoundError:
            pass

        self.update_todo_list()

    def save_data(self):
        with open('todo.txt', 'w', encoding='utf-8') as file:
            for item in self.todo_items:
                status = '1' if item['done'] else '0'  # "True" ve "False" yerine 1 ve 0 kullanacağız
                file.write(f"{item['text']}:{status}\n")

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    sag_taraf = SagTaraf()
    sag_taraf.show()
    sys.exit(app.exec_())
