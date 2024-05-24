import json
from PyQt6.QtWidgets import QTableWidget, QMessageBox, QTableWidgetItem
from src.abstract import ControladorBase, TelaBase

class FormBase(TelaBase, ControladorBase):
  def __init__(self, entidade: str):
    super().__init__()
    self.id_row = None
    self.entidade = entidade

  def carrega_dados(self, entidade: str) -> list:
    with open(f"dados/{entidade}.json", 'r') as file:
      return json.load(file)

  def salva_dados(self, data: list, entidade: str) -> None:
    with open(f"dados/{entidade}.json", 'w') as file:
      json.dump(data, file)

  def open_form(self, id: int, title: str) -> None:
    self.id_row = id
    self.setWindowTitle(title)
    self.fill_form()
    self.show()

  def is_edit(self) -> bool:
    return self.id_row != None
  
  def mostra_aviso(self, messagem: str) -> None:
    QMessageBox.warning(self, "Aviso", messagem,
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