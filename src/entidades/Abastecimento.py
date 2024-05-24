import datetime

class Abastecimento():
  def __init__(self, id_bomba: str, id_tipo: str, preco: float, litros: float, data: datetime):
    self.id_bomba = id_bomba,
    self.id_tipo = id_tipo,
    self.preco = preco,
    self.litros = litros,
    self.data = data.isoformat()

  def transforma_para_dict(self):
    return {
      'id_bomba': self.id_bomba,
      'id_tipo': self.id_tipo,
      'preco': self.preco,
      'litros': self.litros,
      'data': self.data
    }