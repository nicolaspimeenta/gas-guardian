from abc import abstractmethod
from src.abstract.TelaBase import TelaBase

class FormBase(TelaBase):
  def __init__(self, entidade: str):
    super().__init__()
    self.id_row = None
    self.entidade = entidade

  def open_form(self, id: int, title: str) -> None:
    self.id_row = id
    self.setWindowTitle(title)
    self.fill_form()
    self.show()

  def is_edit(self) -> bool:
    return self.id_row != None
  
  @abstractmethod
  def fill_form(self) -> None:
    pass