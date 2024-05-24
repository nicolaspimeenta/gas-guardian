class TipoCombustivel():
  def __init__(self, nome: str, preco: float):
    self.nome = nome
    self.preco = preco

  def transforma_para_dict(self) -> dict[str, str]:
    return {
      'nome': self.nome,
      'preco': "{:.2f}".format(self.preco)
    }