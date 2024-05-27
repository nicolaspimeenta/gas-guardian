# UC008: Registrar um Abastecimento

from datetime import datetime

class Abastecimento():
  def __init__(self, id_bomba: str, id_tipo: str, preco: float, litros: float, data: datetime):
    self.id_bomba = id_bomba
    self.id_tipo = id_tipo
    self.preco = preco
    self.litros = litros
    self.data = data

  def transforma_para_dict(self) -> dict[str, str]:
    return {
      'id_bomba': self.id_bomba,
      'id_tipo': self.id_tipo,
      'preco': "{:.2f}".format(self.preco),
      'litros': "{:.2f}".format(self.litros),
      'data': self.data
    }