# UC003: Cadastrar, Visualizar, Editar e Excluir Tanques de Combustível

class Tanque():
  def __init__(self, id_tanque: str, tipo_combustivel: str, volume_atual: float, capacidade_maxima: float, porcentagem_alerta: int):
    self.id_tanque = id_tanque
    self.tipo_combustivel = tipo_combustivel
    self.volume_atual = volume_atual
    self.capacidade_maxima = capacidade_maxima
    self.porcentagem_alerta = porcentagem_alerta

  def transforma_para_dict(self) -> dict[str, str | float | int]:
    return {
      'id_tanque': self.id_tanque,
      'tipo_combustivel': self.tipo_combustivel,
      'volume_atual': self.volume_atual,
      'capacidade_maxima': self.capacidade_maxima,
      'porcentagem_alerta': self.porcentagem_alerta
    }