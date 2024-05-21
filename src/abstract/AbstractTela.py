import json
from PyQt6 import QtCore, QtGui, QtWidgets

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