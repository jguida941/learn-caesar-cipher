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


def apply_futuristic_theme(app: QtWidgets.QApplication) -> None:
    """Apply a sleek neon-on-carbon theme inspired by the sample styling."""
    app.setStyle("Fusion")

    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor("#121212"))
    palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtGui.QColor("#eeeeee"))
    palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor("#101014"))
    palette.setColor(QtGui.QPalette.ColorRole.AlternateBase, QtGui.QColor("#1b1b22"))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase, QtGui.QColor("#1b1b22"))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipText, QtGui.QColor("#ffffff"))
    palette.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor("#f0f0f0"))
    palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor("#18181e"))
    palette.setColor(QtGui.QPalette.ColorRole.ButtonText, QtGui.QColor("#eeeeee"))
    palette.setColor(QtGui.QPalette.ColorRole.BrightText, QtGui.QColor("#ff6b6b"))
    palette.setColor(QtGui.QPalette.ColorRole.Highlight, QtGui.QColor("#00ffaa"))
    palette.setColor(QtGui.QPalette.ColorRole.HighlightedText, QtGui.QColor("#121212"))
    app.setPalette(palette)

    app.setStyleSheet(
        """
        QWidget {
            background: #121212;
            color: #EEE;
            font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
        }
        QGroupBox {
            border: 1px solid #2D2D2D;
            border-radius: 10px;
            margin-top: 8px;
            padding: 12px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 6px;
            color: #00FFAA;
            font-weight: 600;
        }
        QLabel#mappingHint {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #1a1a1d, stop:1 #232327);
            border: 1px solid #2F2F2F;
            border-radius: 12px;
            padding: 10px 14px;
            font-size: 15px;
            color: #87ffe9;
        }
        QTextEdit, QPlainTextEdit, QListWidget, QTableWidget {
            background: #1F1F1F;
            border: 1px solid #2D2D2D;
            border-radius: 10px;
            padding: 6px;
            selection-background-color: #00FFAA;
            selection-color: #0A0A0A;
        }
        QSpinBox {
            background: #1F1F1F;
            border: 1px solid #2D2D2D;
            border-radius: 8px;
            padding: 4px;
        }
        QPushButton {
            background: #1F1F1F;
            border: 2px solid #2D2D2D;
            border-radius: 8px;
            padding: 8px 14px;
            min-width: 100px;
            color: #EEE;
            font-weight: 500;
        }
        QPushButton:hover {
            border-color: #00FFAA;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #1F1F1F, stop:1 #2F2F2F);
        }
        QPushButton:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #2F2F2F, stop:1 #1F1F1F);
        }
        QPushButton#rot13Btn {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #ff6b6b, stop:1 #ffa94d);
            border: none;
            color: #121212;
            font-weight: bold;
        }
        QPushButton#rot13Btn:hover {
            border: 2px solid #FFD700;
            margin: -1px;
        }
        QToolButton {
            color: #00FFAA;
            font-weight: 600;
            border: none;
            padding: 4px 6px;
        }
        QToolButton:hover {
            color: #7bffe2;
        }
        QToolButton:checked {
            color: #FFD54F;
        }
        #infoPanel {
            background: #16161d;
            border: 1px solid #2D2D2D;
            border-radius: 12px;
        }
        #infoPanel QLabel {
            color: #a5ffea;
            font-size: 14px;
            line-height: 1.6em;
        }
        QCheckBox {
            spacing: 8px;
        }
        QRadioButton::indicator, QCheckBox::indicator {
            width: 16px;
            height: 16px;
        }
        QRadioButton::indicator::checked,
        QCheckBox::indicator::checked {
            background: #00FFAA;
            border: 1px solid #00FFAA;
        }
        QTableWidget::item {
            border: none;
        }
        QListWidget::item {
            padding: 6px 8px;
        }
        QListWidget::item:hover {
            background: rgba(0, 255, 170, 0.08);
        }
        QListWidget::item:selected {
            background: rgba(0, 255, 170, 0.25);
            color: #00FFAA;
        }
        QToolTip {
            background: #1E1E1E;
            color: #00FFAA;
            border: 1px solid #00FFAA;
            border-radius: 6px;
            padding: 6px;
        }
        """
    )


class FocusAwarePlainTextEdit(QtWidgets.QPlainTextEdit):
    """QPlainTextEdit that emits editingFinished when focus leaves."""

    editingFinished = QtCore.pyqtSignal()

    def focusOutEvent(self, event: QtGui.QFocusEvent) -> None:  # type: ignore[override]
        super().focusOutEvent(event)
        self.editingFinished.emit()


class CaesarApp(QtWidgets.QWidget):
    """Simple GUI for demonstrating how a Caesar cipher works."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Caesar Cipher: Educational")
        self.setMinimumSize(900, 520)
        self._accent_color = QtGui.QColor("#00d2ff")
        self._muted_color = QtGui.QColor("#1f2933")
        self._text_color = QtGui.QColor("#f5f7fa")
        self._last_history_snapshot: tuple[str, int, str, str, int, int] | None = None
        # Store the most recent transformation while the user is still editing.
        self._pending_history_entry: tuple[str, int, str, str, int, int] | None = None
        self._highlight_indices: set[int] = set()
        self._history_timer = QtCore.QTimer(self)
        self._history_timer.setSingleShot(True)
        self._history_timer.timeout.connect(self.capture_history_snapshot)

        self.build_ui()
        self.wire_events()
        self.info_toggle.setChecked(True)
        self.update_mapping()
        self.run_cipher()

    # UI construction -----------------------------------------------------
    def build_ui(self) -> None:
        """Instantiate widgets and arrange the primary layout."""
        self.input_edit = FocusAwarePlainTextEdit()
        self.input_edit.setPlaceholderText("Enter text…")
        self.input_edit.setToolTip("Type or paste the text you want to transform.")

        self.output_edit = QtWidgets.QPlainTextEdit()
        self.output_edit.setReadOnly(True)
        self.output_edit.setToolTip("Cipher output appears here (read-only).")

        self.shift_spin = QtWidgets.QSpinBox()
        self.shift_spin.setRange(1, 25)
        self.shift_spin.setValue(3)
        self.shift_spin.setToolTip(
            "Shift amount. Encoding uses (index + shift) mod 26; decoding uses (index - shift) mod 26."
        )

        self.encode_btn = QtWidgets.QRadioButton("Encode")
        self.encode_btn.setChecked(True)
        self.encode_btn.setToolTip(
            "Encrypt by shifting letters forward: (index + shift) mod 26."
        )

        self.decode_btn = QtWidgets.QRadioButton("Decode")
        self.decode_btn.setToolTip(
            "Decrypt by shifting letters backward: (index - shift) mod 26."
        )

        self.rot13_btn = QtWidgets.QPushButton("ROT13")
        self.rot13_btn.setObjectName("rot13Btn")
        self.rot13_btn.setToolTip("Set shift to 13 (ROT13 is its own inverse).")
        self.copy_btn = QtWidgets.QPushButton("Copy Result")
        self.copy_btn.setToolTip("Copy the current output text to the clipboard.")
        self.clear_btn = QtWidgets.QPushButton("Clear")
        self.clear_btn.setToolTip("Clear both the input and output text areas.")
        self.reset_btn = QtWidgets.QPushButton("Reset")
        self.reset_btn.setToolTip("Restore defaults: shift=3, encode mode, mapping hidden, fields cleared.")
        self.show_map_chk = QtWidgets.QCheckBox("Show mapping")
        self.show_map_chk.setChecked(True)
        self.show_map_chk.setToolTip("Toggle the alphabet mapping grid for visualization.")

        self.map_table = QtWidgets.QTableWidget(2, 26)
        self.map_table.horizontalHeader().setVisible(False)
        self.map_table.setVerticalHeaderLabels(["Plain", "Cipher"])
        header = self.map_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.map_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.map_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.map_table.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.map_table.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.map_table.verticalHeader().setDefaultSectionSize(42)
        self.map_table.setMinimumHeight(170)
        self.map_table.setStyleSheet("font-size: 16px;")
        self.map_table.setToolTip(
            "Plain alphabet (top row) and cipher alphabet (bottom row). "
            "Highlighted columns reflect letters present in the current text."
        )
        self.history_list = QtWidgets.QListWidget()
        self.history_list.setFixedWidth(260)
        self.history_list.setToolTip("Double-click an item to reuse that result as new input.")

        self.mapping_label = QtWidgets.QLabel()
        self.mapping_label.setObjectName("mappingHint")
        self.mapping_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mapping_label.setWordWrap(True)
        self.mapping_label.setMinimumHeight(28)

        self.info_toggle = QtWidgets.QToolButton()
        self.info_toggle.setText("Show Explanation ▾")
        self.info_toggle.setCheckable(True)
        self.info_toggle.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.info_toggle.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.info_toggle.setToolTip("Toggle a quick refresher on the modular arithmetic behind the shift.")
        self.info_toggle.setArrowType(QtCore.Qt.ArrowType.DownArrow)

        self.info_panel = QtWidgets.QFrame()
        self.info_panel.setObjectName("infoPanel")
        self.info_panel.setVisible(False)
        info_layout = QtWidgets.QVBoxLayout(self.info_panel)
        info_layout.setContentsMargins(18, 12, 18, 14)
        info_layout.setSpacing(10)
        self.info_label = QtWidgets.QLabel()
        self.info_label.setWordWrap(True)
        self.info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.info_label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.info_label.setObjectName("infoLabel")
        info_layout.addWidget(self.info_label)

        # Assemble control row
        control_row = QtWidgets.QHBoxLayout()
        self.shift_label = QtWidgets.QLabel("Shift")
        self.shift_label.setToolTip(
            "Shift amount. Encoding → (index + shift) mod 26. "
            "Decoding → (index - shift) mod 26."
        )
        control_row.addWidget(self.shift_label)
        control_row.addWidget(self.shift_spin)
        control_row.addSpacing(12)
        control_row.addWidget(self.encode_btn)
        control_row.addWidget(self.decode_btn)
        control_row.addSpacing(12)
        control_row.addWidget(self.rot13_btn)
        control_row.addWidget(self.reset_btn)
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
        io_layout.addWidget(self.mapping_label)
        io_layout.addWidget(self.info_toggle, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        io_layout.addWidget(self.info_panel)
        io_layout.addWidget(self.map_table)

        io_splitter.addWidget(io_pane)
        io_splitter.addWidget(self.history_list)
        io_splitter.setSizes([700, 200])

        root_layout = QtWidgets.QVBoxLayout(self)
        root_layout.addLayout(control_row)
        root_layout.addWidget(io_splitter)

    # Wiring ---------------------------------------------------------------
    def wire_events(self) -> None:
        """Connect UI signals to their corresponding slots."""
        self.input_edit.textChanged.connect(self.on_text_changed)
        self.input_edit.editingFinished.connect(self.on_input_finished)
        self.shift_spin.valueChanged.connect(self.on_shift_changed)
        self.encode_btn.toggled.connect(self.on_mode_changed)
        self.decode_btn.toggled.connect(self.on_mode_changed)
        self.show_map_chk.toggled.connect(self.on_toggle_mapping)

        self.rot13_btn.clicked.connect(self.apply_rot13)
        self.copy_btn.clicked.connect(self.copy_result)
        self.clear_btn.clicked.connect(self.clear_all)
        self.reset_btn.clicked.connect(self.reset_defaults)
        self.info_toggle.toggled.connect(self.toggle_info_panel)
        self.history_list.itemActivated.connect(self.reuse_history_item)

    # Helpers --------------------------------------------------------------
    def encode_mode(self) -> bool:
        """Return True when the encode radio button is selected."""
        return self.encode_btn.isChecked()

    def on_text_changed(self) -> None:
        """Update the cipher output and queue a history snapshot after typing."""
        self.run_cipher()
        self.schedule_history_capture()

    def on_input_finished(self) -> None:
        """Persist the most recent result after the input field loses focus."""
        self.maybe_append_history(force=True)

    def on_shift_changed(self, _: int) -> None:
        """Refresh output whenever the shift changes."""
        self.run_cipher()
        self.schedule_history_capture()

    def on_mode_changed(self, _: bool) -> None:
        """Recompute output when the encode/decode mode flips."""
        self.run_cipher()
        self.schedule_history_capture()

    def on_toggle_mapping(self, checked: bool) -> None:
        """Show or hide the alphabet mapping grid."""
        self.map_table.setVisible(checked)
        self.mapping_label.setVisible(checked)
        if checked:
            self.update_mapping()

    def apply_rot13(self) -> None:
        """Apply the ROT13 preset (shift=13 in encode mode)."""
        self.shift_spin.setValue(13)
        self.encode_btn.setChecked(True)
        self.run_cipher()
        self.schedule_history_capture()

    def copy_result(self) -> None:
        """Copy the cipher text into the clipboard."""
        QtWidgets.QApplication.clipboard().setText(self.output_edit.toPlainText())

    def clear_all(self) -> None:
        """Clear input/output fields and keep cursor in sync."""
        self.input_edit.clear()
        self.output_edit.clear()
        self.history_list.clearSelection()
        self._history_timer.stop()
        self.run_cipher()

    def reset_defaults(self) -> None:
        """Restore default settings and clear the workspace."""
        self.shift_spin.setValue(3)
        self.encode_btn.setChecked(True)
        self.show_map_chk.setChecked(False)
        self.info_toggle.setChecked(True)
        self.clear_all()
        self.update_mapping()

    def schedule_history_capture(self) -> None:
        """Debounce history updates so they trigger shortly after typing stops."""
        if not self.input_edit.toPlainText().strip():
            self._history_timer.stop()
            return
        self._history_timer.start(450)

    def capture_history_snapshot(self) -> None:
        """Persist the pending history entry once the debounce timer fires."""
        self.maybe_append_history(force=True)

    def toggle_info_panel(self, checked: bool) -> None:
        """Expand/collapse the modular arithmetic explainer."""
        self.info_panel.setVisible(checked)
        self.info_toggle.setArrowType(
            QtCore.Qt.ArrowType.UpArrow if checked else QtCore.Qt.ArrowType.DownArrow
        )
        self.info_toggle.setText("Hide Explanation ▴" if checked else "Show Explanation ▾")
        if checked:
            self.update_info_text(self.shift_spin.value())

    def reuse_history_item(self, item: QtWidgets.QListWidgetItem) -> None:
        """Inject a previous output back into the input field."""
        stored = item.data(QtCore.Qt.ItemDataRole.UserRole)
        if isinstance(stored, tuple) and len(stored) >= 6:
            label, shift, result, source_text, _, _ = stored
            with QtCore.QSignalBlocker(self.shift_spin):
                self.shift_spin.setValue(shift)
            # Flip the mode so the next run performs the inverse operation.
            if label == "ENC":
                with QtCore.QSignalBlocker(self.decode_btn), QtCore.QSignalBlocker(
                    self.encode_btn
                ):
                    self.decode_btn.setChecked(True)
                self.input_edit.setPlainText(result)
            else:
                with QtCore.QSignalBlocker(self.encode_btn), QtCore.QSignalBlocker(
                    self.decode_btn
                ):
                    self.encode_btn.setChecked(True)
                self.input_edit.setPlainText(result)
        else:
            text = stored if isinstance(stored, str) else item.text().split("|", 1)[-1].strip()
            self.input_edit.setPlainText(text)
        self.input_edit.moveCursor(QtGui.QTextCursor.MoveOperation.End)
        self.input_edit.setFocus()

    # Core logic -----------------------------------------------------------
    def run_cipher(self) -> None:
        """Transform the current text and update output/history widgets."""
        text = self.input_edit.toPlainText()
        shift = self.shift_spin.value()
        encode_mode = self.encode_mode()
        shifted_lower = LOWER[shift:] + LOWER[:shift]
        plain_lookup = {char: idx for idx, char in enumerate(LOWER)}
        cipher_lookup = {char: idx for idx, char in enumerate(shifted_lower)}
        highlight_indices: set[int] = set()
        letter_count = 0
        word_count = len(text.split()) if text.strip() else 0

        try:
            result = caesar(text, shift, encode=encode_mode) if text else ""
        except Exception as exc:  # pragma: no cover - GUI feedback
            result = f"[error] {exc}"

        self.output_edit.setPlainText(result)

        if result and not result.startswith("[error]") and text:
            for original, mapped in zip(text, result):
                lower = original.lower()
                if encode_mode:
                    index = plain_lookup.get(lower)
                else:
                    index = cipher_lookup.get(lower)
                if index is not None:
                    highlight_indices.add(index)
                    letter_count += 1
        else:
            self._pending_history_entry = None
            if not text:
                self._last_history_snapshot = None
            highlight_indices.clear()
            if result.startswith("[error]"):
                word_count = 0
                letter_count = 0
            self._highlight_indices = highlight_indices
            self.update_mapping()
            return

        label = "ENC" if encode_mode else "DEC"
        if letter_count:
            self._pending_history_entry = (label, shift, result, text, letter_count, word_count)
        else:
            self._pending_history_entry = None
        self._highlight_indices = highlight_indices
        self.update_mapping()

    def _preview_text(self, text: str, limit: int = 60) -> str:
        """Return a truncated, single-line preview for the history list."""
        flattened = text.replace("\n", " ").replace("\r", " ").strip()
        if len(flattened) <= limit:
            return flattened
        return flattened[: limit - 1].rstrip() + "…"

    def maybe_append_history(self, force: bool = False) -> None:
        """Add the pending result to history when editing settles."""
        entry = self._pending_history_entry
        if not entry:
            return
        label, shift, result, source_text, letter_count, word_count = entry
        if not result or result.startswith("[error]"):
            return
        if not force and self.input_edit.hasFocus():
            return
        if self._last_history_snapshot == entry:
            return
        # Render a compact label that still exposes mode, shift, and a preview.
        display = (
            f"{label} s={shift} | letters={letter_count} words={word_count} | "
            f"{self._preview_text(source_text)} → {self._preview_text(result)}"
        )
        item = QtWidgets.QListWidgetItem(display)
        item.setData(QtCore.Qt.ItemDataRole.UserRole, entry)
        self.history_list.insertItem(0, item)
        self.history_list.clearSelection()
        self._last_history_snapshot = entry

    def update_info_text(self, shift: int) -> None:
        """Refresh the explanatory text describing the math for the current shift."""
        self.info_label.setText(
            "<h4 style='margin:0 0 8px 0; color:#00ffaa;'>How it works</h4>"
            f"<p style='margin:0 0 6px 0;'><b>Encoding</b>: (index + {shift}) mod 26 &rarr; wraps forward.</p>"
            f"<p style='margin:0 0 10px 0;'><b>Decoding</b>: (index - {shift}) mod 26 &rarr; wraps backward.</p>"
            "<p style='margin:0; color:#d1f5ff;'>Shift values between 1&ndash;25 produce unique rotations; mod 26 keeps results in the 0&ndash;25 range so letters loop around the alphabet.</p>"
        )

    def update_mapping(self) -> None:
        """Populate the mapping table and helper label for the active mode."""
        shift = self.shift_spin.value()
        shifted_lower = LOWER[shift:] + LOWER[:shift]
        encode_mode = self.encode_mode()

        if encode_mode:
            top_row = LOWER
            bottom_row = shifted_lower
            row_labels = ["Plain", "Cipher"]
            source_label = "plain"
            target_label = "cipher"
            source_char = LOWER[0]
            target_char = shifted_lower[0]
            shift_text = f"+{shift}"
            mode_text = "Encode"
        else:
            top_row = shifted_lower
            bottom_row = LOWER
            row_labels = ["Cipher", "Plain"]
            source_label = "cipher"
            target_label = "plain"
            source_char = shifted_lower[0]
            target_char = LOWER[0]
            shift_text = f"-{shift}"
            mode_text = "Decode"
        self.map_table.setVerticalHeaderLabels(row_labels)

        accent_bg = QtGui.QColor(self._accent_color)
        accent_bg.setAlpha(90)
        muted_bg = QtGui.QColor(self._muted_color)
        muted_bg.setAlpha(140)
        highlight_bg = QtGui.QColor("#204e4a")
        highlight_bg.setAlpha(200)
        text_brush = QtGui.QBrush(self._text_color)
        accent_brush = QtGui.QBrush(accent_bg)
        muted_brush = QtGui.QBrush(muted_bg)
        highlight_brush = QtGui.QBrush(highlight_bg)
        highlight_indices = getattr(self, "_highlight_indices", set())

        for index, (top_char, bottom_char) in enumerate(zip(top_row, bottom_row)):
            top_item = QtWidgets.QTableWidgetItem(top_char)
            top_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            top_item.setForeground(text_brush)
            top_item.setBackground(
                highlight_brush if index in highlight_indices else muted_brush
            )

            bottom_item = QtWidgets.QTableWidgetItem(bottom_char)
            bottom_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            bottom_item.setForeground(text_brush)
            bottom_item.setBackground(
                highlight_brush if index in highlight_indices else accent_brush
            )

            self.map_table.setItem(0, index, top_item)
            self.map_table.setItem(1, index, bottom_item)

        self.mapping_label.setText(
            f"{mode_text} mode: {source_label} '{source_char}' → {target_label} '{target_char}' "
            f"(shift {shift_text}, mod 26)"
        )
        self.mapping_label.setStyleSheet(
            f"font-weight:600; padding:4px; color:{self._accent_color.name()};"
        )
        if encode_mode:
            mapping_tip = (
                f"Encoding formula: (index + {shift}) mod 26.\n"
                f"Decoding formula: (index - {shift}) mod 26."
            )
        else:
            mapping_tip = (
                f"Decoding formula: (index - {shift}) mod 26.\n"
                f"Encoding formula: (index + {shift}) mod 26."
            )
        self.mapping_label.setToolTip(mapping_tip)
        self.update_info_text(shift)
        is_visible = self.show_map_chk.isChecked()
        self.mapping_label.setVisible(is_visible)
        self.map_table.setVisible(is_visible)


def main() -> None:
    app = QtWidgets.QApplication([])
    apply_futuristic_theme(app)
    window = CaesarApp()
    window.show()
    app.exec()


if __name__ == "__main__":  # pragma: no cover - GUI entry point
    main()
