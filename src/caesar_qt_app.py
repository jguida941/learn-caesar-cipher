"""
PyQt6 desktop demo for exploring the Caesar cipher.

Run with:
    python -m src.caesar_qt_app

Requires:
    pip install PyQt6
"""

from __future__ import annotations

from PyQt6 import QtCore, QtGui, QtWidgets

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = LOWER.upper()


def caesar(text: str, shift: int, encode: bool = True) -> str:
    """Encode or decode text using a Caesar cipher."""
    if not isinstance(shift, int) or not (1 <= shift <= 25):
        raise ValueError("shift 1–25")
    if not encode:
        shift = -shift

    shifted_lower = LOWER[shift:] + LOWER[:shift]
    shifted_upper = UPPER[shift:] + UPPER[:shift]
    translation_table = str.maketrans(LOWER + UPPER, shifted_lower + shifted_upper)
    return text.translate(translation_table)


class CaesarApp(QtWidgets.QWidget):
    """Simple GUI for demonstrating how a Caesar cipher works."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Caesar Cipher: Educational")
        self.setMinimumSize(900, 520)

        self.build_ui()
        self.wire_events()
        self.update_mapping()
        self.run_cipher()

    # UI construction -----------------------------------------------------
    def build_ui(self) -> None:
        self.input_edit = QtWidgets.QPlainTextEdit()
        self.input_edit.setPlaceholderText("Enter text…")

        self.output_edit = QtWidgets.QPlainTextEdit()
        self.output_edit.setReadOnly(True)

        self.shift_spin = QtWidgets.QSpinBox()
        self.shift_spin.setRange(1, 25)
        self.shift_spin.setValue(3)

        self.encode_btn = QtWidgets.QRadioButton("Encode")
        self.encode_btn.setChecked(True)

        self.decode_btn = QtWidgets.QRadioButton("Decode")

        self.rot13_btn = QtWidgets.QPushButton("ROT13")
        self.copy_btn = QtWidgets.QPushButton("Copy Result")
        self.clear_btn = QtWidgets.QPushButton("Clear")

        self.show_map_chk = QtWidgets.QCheckBox("Show mapping")
        self.show_map_chk.setChecked(True)

        self.map_table = QtWidgets.QTableWidget(2, 26)
        self.map_table.setHorizontalHeaderLabels(list(LOWER))
        self.map_table.verticalHeader().setVisible(False)
        header = self.map_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.map_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.map_table.setFixedHeight(120)

        self.history_list = QtWidgets.QListWidget()
        self.history_list.setFixedWidth(260)

        # Assemble control row
        control_row = QtWidgets.QHBoxLayout()
        control_row.addWidget(QtWidgets.QLabel("Shift"))
        control_row.addWidget(self.shift_spin)
        control_row.addSpacing(12)
        control_row.addWidget(self.encode_btn)
        control_row.addWidget(self.decode_btn)
        control_row.addSpacing(12)
        control_row.addWidget(self.rot13_btn)
        control_row.addStretch()
        control_row.addWidget(self.show_map_chk)
        control_row.addSpacing(12)
        control_row.addWidget(self.copy_btn)
        control_row.addWidget(self.clear_btn)

        # Splitter with IO pane + history
        io_splitter = QtWidgets.QSplitter()

        io_pane = QtWidgets.QWidget()
        io_layout = QtWidgets.QVBoxLayout(io_pane)
        io_layout.setContentsMargins(0, 0, 0, 0)
        io_layout.addWidget(QtWidgets.QLabel("Input"))
        io_layout.addWidget(self.input_edit)
        io_layout.addWidget(QtWidgets.QLabel("Output"))
        io_layout.addWidget(self.output_edit)
        io_layout.addWidget(self.map_table)

        io_splitter.addWidget(io_pane)
        io_splitter.addWidget(self.history_list)
        io_splitter.setSizes([700, 200])

        root_layout = QtWidgets.QVBoxLayout(self)
        root_layout.addLayout(control_row)
        root_layout.addWidget(io_splitter)

    # Wiring ---------------------------------------------------------------
    def wire_events(self) -> None:
        self.input_edit.textChanged.connect(self.run_cipher)
        self.shift_spin.valueChanged.connect(self.on_shift_changed)
        self.encode_btn.toggled.connect(self.run_cipher)
        self.decode_btn.toggled.connect(self.run_cipher)
        self.show_map_chk.toggled.connect(self.map_table.setVisible)

        self.rot13_btn.clicked.connect(self.apply_rot13)
        self.copy_btn.clicked.connect(self.copy_result)
        self.clear_btn.clicked.connect(self.clear_all)
        self.history_list.itemActivated.connect(self.reuse_history_item)

    # Helpers --------------------------------------------------------------
    def encode_mode(self) -> bool:
        return self.encode_btn.isChecked()

    def on_shift_changed(self, _: int) -> None:
        self.update_mapping()
        self.run_cipher()

    def apply_rot13(self) -> None:
        self.shift_spin.setValue(13)
        self.encode_btn.setChecked(True)
        self.run_cipher()

    def copy_result(self) -> None:
        QtWidgets.QApplication.clipboard().setText(self.output_edit.toPlainText())

    def clear_all(self) -> None:
        self.input_edit.clear()
        self.output_edit.clear()

    def reuse_history_item(self, item: QtWidgets.QListWidgetItem) -> None:
        self.input_edit.setPlainText(item.text().split("|", 1)[-1].strip())

    # Core logic -----------------------------------------------------------
    def run_cipher(self) -> None:
        text = self.input_edit.toPlainText()
        shift = self.shift_spin.value()

        try:
            result = caesar(text, shift, encode=self.encode_mode()) if text else ""
        except Exception as exc:  # pragma: no cover - GUI feedback
            result = f"[error] {exc}"

        previous = self.output_edit.toPlainText()
        self.output_edit.setPlainText(result)

        if result and result != previous:
            label = "ENC" if self.encode_mode() else "DEC"
            self.history_list.insertItem(0, f"{label} s={shift} | {result[:60]}")

    def update_mapping(self) -> None:
        shift = self.shift_spin.value()
        shifted_lower = LOWER[shift:] + LOWER[:shift]

        for index, letter in enumerate(LOWER):
            original_item = QtWidgets.QTableWidgetItem(letter)
            mapped_item = QtWidgets.QTableWidgetItem(shifted_lower[index])
            self.map_table.setItem(0, index, original_item)
            self.map_table.setItem(1, index, mapped_item)

        self.map_table.setVisible(self.show_map_chk.isChecked())


def main() -> None:
    app = QtWidgets.QApplication([])
    window = CaesarApp()
    window.show()
    app.exec()


if __name__ == "__main__":  # pragma: no cover - GUI entry point
    main()
