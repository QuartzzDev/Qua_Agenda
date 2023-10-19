from PyQt5.QtWidgets import QVBoxLayout, QTextEdit, QWidget, QPushButton, QLineEdit, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QFrame
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class SolTaraf(QWidget):
    def __init__(self):
        super().__init__()
        self.page_content = {}

        self.initUI()
        self.load_data()

    def initUI(self):
        self.page_list = QListWidget(self)
        self.page_text_edit = QTextEdit(self)
        self.add_page_button = QPushButton('Sayfa Ekle', self)
        self.save_page_button = QPushButton('Sayfayı Kaydet', self)
        self.delete_page_button = QPushButton('Sayfayı Sil', self)
        self.page_name_edit = QLineEdit(self)
        self.page_name_edit.setPlaceholderText('Sayfa İsmi')

        layout = QVBoxLayout()
        page_layout = QHBoxLayout()
        page_layout.addWidget(self.page_name_edit)
        page_layout.addWidget(self.add_page_button)
        page_layout.addWidget(self.save_page_button)
        page_layout.addWidget(self.delete_page_button)
        layout.addLayout(page_layout)
        layout.addWidget(self.page_list)
        layout.addWidget(self.page_text_edit)
        self.setLayout(layout)

        self.add_page_button.clicked.connect(self.add_page)
        self.save_page_button.clicked.connect(self.save_page)
        self.delete_page_button.clicked.connect(self.delete_page)
        self.page_list.itemClicked.connect(self.show_page_content)

    def add_page(self):
        page_name = self.page_name_edit.text()
        if page_name:
            item = QListWidgetItem(page_name, self.page_list)
            self.page_content[page_name] = ''
            self.page_name_edit.clear()
            self.save_data()

    def show_page_content(self, item):
        page_name = item.text()
        self.page_text_edit.setPlainText(self.page_content.get(page_name, ''))

    def save_page(self):
        selected_item = self.page_list.currentItem()
        if selected_item:
            page_name = selected_item.text()
            page_content = self.page_text_edit.toPlainText()
            self.page_content[page_name] = page_content
            self.save_data()

    def delete_page(self):
        selected_item = self.page_list.currentItem()
        if selected_item:
            page_name = selected_item.text()
            del self.page_content[page_name]
            self.page_list.takeItem(self.page_list.currentRow())
            self.page_text_edit.clear()
            self.save_data()

    def load_data(self):
        try:
            with open('agenda.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    page_name, page_content = line.strip().split(':')
                    self.page_content[page_name] = page_content
                    self.page_list.addItem(page_name)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('agenda.txt', 'w', encoding='utf-8') as file:
            for page_name, page_content in self.page_content.items():
                file.write(f"{page_name}:{page_content}\n")

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    sol_taraf = SolTaraf()
    sol_taraf.show()
    sys.exit(app.exec_())