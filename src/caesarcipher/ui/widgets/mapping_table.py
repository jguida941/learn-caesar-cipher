"""Mapping table widget for the Caesar cipher UI."""

from __future__ import annotations

from typing import cast

from PyQt6 import QtCore, QtGui, QtWidgets

from caesarcipher.config import defaults
from caesarcipher.core.crypto import LOWER


class MappingTableWidget(QtWidgets.QTableWidget):
    """Two-row table showing plain/cipher alphabet mapping."""

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(2, len(LOWER), parent)
        self._accent = QtGui.QColor(defaults.ACCENT_COLOR)
        self._muted_top = QtGui.QColor("#082f29")
        self._muted_bottom = QtGui.QColor("#0b2030")
        self._text = QtGui.QColor(defaults.TEXT_COLOR)
        self._highlight_top = QtGui.QColor("#00FFAA")
        self._highlight_top.setAlpha(245)
        self._highlight_bottom = QtGui.QColor("#ffa94d")
        self._highlight_bottom.setAlpha(240)

        header = cast(QtWidgets.QHeaderView, self.horizontalHeader())
        header.setVisible(False)
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        v_header = cast(QtWidgets.QHeaderView, self.verticalHeader())
        v_header.setVisible(True)
        v_header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Fixed)
        v_header.setMinimumSectionSize(0)
        v_header.setDefaultSectionSize(68)
        v_header.setStyleSheet(
            """
            QHeaderView::section {
                color: #00FFAA;
                background: rgba(0, 255, 170, 0.08);
                font-weight: 600;
                padding-left: 10px;
                padding-right: 8px;
                border: none;
            }
            """
        )
        self.setVerticalHeaderLabels(["Plain", "Cipher"])
        self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.setShowGrid(False)
        font = QtGui.QFont(self.font())
        font.setPointSize(16)
        font.setBold(True)
        font.setLetterSpacing(QtGui.QFont.SpacingType.AbsoluteSpacing, 2.1)
        self.setFont(font)
        self.setFixedHeight(220)
        self.setStyleSheet(
            """
            QTableWidget {
                background: #0b1512;
                border: 2px solid #12352d;
                border-radius: 12px;
                gridline-color: rgba(0, 0, 0, 0);
            }
            QTableWidget::item {
                padding: 4px 2px;
            }
            """
        )

        self._highlight_indices: set[int] = set()

    def set_highlights(self, indices: set[int]) -> None:
        """Store the indices to highlight on next update."""
        self._highlight_indices = indices

    def update_mapping(self, shifted: str, *, encode_mode: bool) -> None:
        """Render the alphabet rows with optional highlights."""
        top_row = LOWER if encode_mode else shifted
        bottom_row = shifted if encode_mode else LOWER
        self.setVerticalHeaderLabels(["Plain", "Cipher"] if encode_mode else ["Cipher", "Plain"])

        highlight_brush_top = QtGui.QBrush(self._highlight_top)
        highlight_brush_bottom = QtGui.QBrush(self._highlight_bottom)
        muted_brush_top = QtGui.QBrush(self._muted_top)
        muted_brush_bottom = QtGui.QBrush(self._muted_bottom)
        text_brush = QtGui.QBrush(self._text)

        for index, (top_char, bottom_char) in enumerate(zip(top_row, bottom_row)):
            top_item = QtWidgets.QTableWidgetItem(top_char)
            top_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            top_item.setForeground(text_brush)
            top_item.setBackground(
                highlight_brush_top if index in self._highlight_indices else muted_brush_top
            )
            top_item.setSizeHint(QtCore.QSize(top_item.sizeHint().width(), 70))

            bottom_item = QtWidgets.QTableWidgetItem(bottom_char)
            bottom_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            bottom_item.setForeground(text_brush)
            bottom_item.setBackground(
                highlight_brush_bottom if index in self._highlight_indices else muted_brush_bottom
            )
            bottom_item.setSizeHint(QtCore.QSize(bottom_item.sizeHint().width(), 70))

            self.setItem(0, index, top_item)
            self.setItem(1, index, bottom_item)

        # no-op; height fixed via minimum height to mirror legacy UI


__all__ = ["MappingTableWidget"]
