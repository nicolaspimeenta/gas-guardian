import json
from PyQt6 import QtWidgets

class AbstractTela(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()

  def mostra_aviso(self, messagem: str) -> None:
    QtWidgets.QMessageBox.warning(self, "Aviso", messagem,
    QtWidgets.QMessageBox.StandardButton.Ok)

  def carrega_dados(self, entidade: str) -> list:
    with open(f"dados/{entidade}.json", 'r') as file:
      return json.load(file)

  def salva_dados(self, data: list, entidade: str) -> None:
    with open(f"dados/{entidade}.json", 'w') as file:
      json.dump(data, file)

  def cancelar(self) -> None:
    self.hide()

  def fill_table(self, data: list, table: QtWidgets.QTableWidget) -> None:
    if data:
      table.setRowCount(0)
      table.setRowCount(len(data))
      for row, info in enumerate(data):
        info_list = info.values()
        for column, item in enumerate(info_list):
          if item is list:
            for i in item:
              i = i[0]
          cell_item = QtWidgets.QTableWidgetItem(str(item))
          table.setItem(row, column, cell_item)
    else:
      table.setRowCount(0)