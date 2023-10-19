import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QSplitter, QFrame
from left import SolTaraf
from right import SagTaraf

class AgendaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Agenda App')
        self.setGeometry(100, 100, 600, 400)

        self.sol_taraf = SolTaraf()
        self.sag_taraf = SagTaraf()

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        splitter = QSplitter()
        splitter.addWidget(self.sol_taraf)
        splitter.addWidget(self.separator)
        splitter.addWidget(self.sag_taraf)
        splitter.setSizes([self.sol_taraf.height(), 1, self.sol_taraf.height()])

        main_layout = QHBoxLayout()
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)
        self.show()

    def closeEvent(self, event):
        # Verileri kaydet
        self.sol_taraf.save_data()
        self.sag_taraf.save_data()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    agenda_app = AgendaApp()
    sys.exit(app.exec_())
