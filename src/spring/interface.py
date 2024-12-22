from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout, QSizePolicy
from PySide2.QtCore import Qt
import hou  # type: ignore
from spring.simulation import simulate, stop_simulation


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.set_window_settings()
        self.set_ui()
        self.set_functionnals()

    def set_window_settings(self) -> None:
        self.setParent(hou.ui.mainQtWindow(), Qt.Window)
        self.setWindowTitle("convert Nodes to Spring")
        self.resize(400, 150)

    def set_ui(self) -> None:
        self.setStyleSheet(
            """
                font-size: 11pt;
            """
        )
        main_layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(main_layout)

        self.convert_button: QPushButton = QPushButton("Convert Nodes")
        self.convert_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.stop_button: QPushButton = QPushButton("Stop")
        self.stop_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.stop_button.setEnabled(False)

        main_layout.addWidget(self.convert_button)
        main_layout.addWidget(self.stop_button)

    def set_functionnals(self) -> None:
        self.convert_button.clicked.connect(self.convert_btn_event)
        self.stop_button.clicked.connect(self.stop_btn_event)

    def convert_btn_event(self) -> None:
        self.stop_button.setEnabled(True)
        self.convert_button.setEnabled(False)
        simulate()

    def stop_btn_event(self) -> None:
        self.stop_button.setEnabled(False)
        self.convert_button.setEnabled(True)
        stop_simulation()
