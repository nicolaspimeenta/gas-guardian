import json
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QMessageBox, QTableWidgetItem

class TelaBase(QMainWindow):
  def __init__(self):
    super().__init__()

  def mostra_aviso(self, messagem: str) -> None:
    QMessageBox.warning(self, "Aviso", messagem,
    QMessageBox.StandardButton.Ok)

  def mostra_mensagem(self, mensagem: str) -> None:
    QMessageBox.information(self, "Sucesso", mensagem,
    QMessageBox.StandardButton.Ok)

  def fill_table(self, data: list, table: QTableWidget) -> None:
    if data:
      table.setRowCount(0)
      table.setRowCount(len(data))
      for row, info in enumerate(data):
        info_list = info.values()
        for column, item in enumerate(info_list):
          if item is list:
            for i in item:
              i = i[0]
          cell_item = QTableWidgetItem(str(item))
          table.setItem(row, column, cell_item)
    else:
      table.setRowCount(0)