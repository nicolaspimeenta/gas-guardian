import json
from abc import ABC, abstractmethod

class ControladorBase(ABC):
  def __init__(self, tela: object, entidade: str):
    self.id_row = None
    self.entidade = entidade
    self.tela = tela
    self.conecta_controlador_tela()
    
  @abstractmethod
  def is_form_valido(self, form_data: dict) -> bool:
    pass

  @abstractmethod
  def confirmar(self) -> None:
    pass

  @abstractmethod
  def conecta_controlador_tela(self) -> None:
    pass

  @abstractmethod
  def fill_form(self) -> None:
    pass

  def is_edit(self) -> bool:
    return self.id_row != None

  def abre_tela(self, id_row: int, title: str) -> None:
    self.id_row = id_row
    self.fill_form()
    self.tela.setWindowTitle(title)
    self.tela.show()

  def exclui_registro(self, id_row: int) -> None:
    data = self.carrega_dados(self.entidade)
    del data[id_row]
    self.salva_dados(data)
    self.tela.mostra_mensagem(f'A linha {id_row+1} foi excluída')

  def carrega_dados(self, entidade: str = None) -> list:
    with open(f"dados/{self.entidade if entidade is None else entidade}.json", 'r') as file:
      return json.load(file)

  def salva_dados(self, data: list) -> None:
    with open(f"dados/{self.entidade}.json", 'w') as file:
      json.dump(data, file)