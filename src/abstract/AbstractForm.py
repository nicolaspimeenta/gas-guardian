from src.abstract.AbstractTela import AbstractTela

class AbstractForm(AbstractTela):
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