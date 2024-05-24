class Posto():
  def __init__(self, nome_posto: str, chave_pix: str, cnpj: str):
    self.nome_posto = nome_posto
    self.chave_pix = chave_pix
    self.cnpj = cnpj

  def transforma_para_dict(self) -> dict[str, str]:
    return {
      'nome_posto': self.nome_posto, 
      'chave_pix': self.chave_pix,
      'cnpj': self.cnpj
    }