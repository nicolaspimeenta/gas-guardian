from src.abstract.TelaBase import TelaBase

class FormBase(TelaBase):
  def __init__(self, id_row: int, title: str, dados: str):
    super().__init__()
    self.id_row = id_row
    self.title = title
    self.dados = dados

  def is_edit(self) -> bool:
    return self.id_row != None
  
  def cancelar(self) -> None:
    self.hide()