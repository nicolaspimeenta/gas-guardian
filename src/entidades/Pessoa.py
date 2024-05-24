class Pessoa():
  def __init__(self, nome: str, cpf: str, email: str, telefone_celular: str, login: str, senha: str, is_gestor: bool):
    self.nome = nome
    self.cpf = cpf
    self.email = email
    self.telefone_celular = telefone_celular
    self.login = login
    self.senha = senha
    self.is_gestor = is_gestor

  def transforma_para_dict(self) -> dict[str, str | bool]:
    return {
      'nome': self.nome,
      'cpf': self.cpf,
      'email': self.email,
      'telefone_celular': self.telefone_celular,
      'login': self.login,
      'login': self.senha,
      'is_gestor': self.is_gestor
    }