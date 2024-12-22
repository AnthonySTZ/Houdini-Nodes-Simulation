from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout, QSizePolicy
from PySide2.QtCore import Qt
import hou  # type: ignore


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

        convert_button: QPushButton = QPushButton("Convert Nodes")
        convert_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        stop_button: QPushButton = QPushButton("Stop")
        stop_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        stop_button.setEnabled(False)

        main_layout.addWidget(convert_button)
        main_layout.addWidget(stop_button)

    def set_functionnals(self) -> None:
        pass
