# UC006: Cadastrar, Visualizar, Editar e Excluir Bombas de Combustível


class Bomba():
  def __init__(self, id_bomba: str, is_auto_abastecimento: bool, tipos_combustivel: list[str]):
    self.id_bomba = id_bomba
    self.is_auto_abastecimento = is_auto_abastecimento
    self.tipos_combustivel = tipos_combustivel

  def transforma_para_dict(self) -> dict[str, str | bool | list[str]]:
    return {
      'id_bomba': self.id_bomba,
      'is_auto_abastecimento': self.is_auto_abastecimento,
      'tipos_combustivel': self.tipos_combustivel
    }