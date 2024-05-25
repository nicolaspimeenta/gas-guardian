# UC001: Cadastrar, Visualizar, Editar e Excluir Usuários


from base64 import b64encode
from src.abstract.ControladorBase import ControladorBase
from src.entidades.Pessoa import Pessoa
from src.telas.TelaPessoa import TelaPessoa

class ControladorPessoa(ControladorBase):
  def __init__(self):
    super().__init__(tela=TelaPessoa, entidade='pessoas')

  def confirmar(self) -> None:
    pessoas_data = self.carrega_dados()
    form_data = {
      'nome': self.tela.inputNome.text().strip(),
      'cpf': self.tela.inputCpf.text().strip(),
      'email': self.tela.inputEmail.text().strip(),
      'telefone_celular': self.tela.inputCelular.text().strip(),
      'login': self.tela.inputLogin.text().strip(),
      'senha': self.encode_senha(self.tela.inputSenha.text().strip()),
      'is_gestor': self.tela.isGestor.isChecked()
      }
    if self.is_form_valido(form_data):
      pessoa_dto = Pessoa(
        nome=form_data['nome'],
        cpf=form_data['cpf'],
        email=form_data['email'],
        telefone_celular=form_data['telefone_celular'],
        login=form_data['login'],
        senha=form_data['senha'],
        is_gestor=form_data['is_gestor']
      )
      if self.is_edit():
        pessoas_data[self.id_row] = pessoa_dto.transforma_para_dict()
        self.salva_dados(pessoas_data)
        self.tela.hide()
      else:
        pessoas_data.append(pessoa_dto.transforma_para_dict())
        self.tela.mostra_mensagem('Uma nova Pessoa foi cadastrada.')
        self.salva_dados(pessoas_data)
        self.tela.hide()
  
  def is_form_valido(self, form_data: dict) -> bool:
    pessoas_data = self.carrega_dados()
    if not (self.is_edit() and form_data['cpf'] == pessoas_data[self.id_row]['cpf']):
      for pessoa in pessoas_data:
        if pessoa['cpf'] == form_data['cpf']:
          self.tela.mostra_aviso("Pessoa já cadastrada.")
          return False
        
    if not (self.is_edit() and form_data['login'] == pessoas_data[self.id_row]['login']):
      for pessoa in pessoas_data:
        if pessoa['login'] == form_data['login']:
          self.tela.mostra_aviso("Login já utilizado.")
          return False
        
    if not form_data['nome'] or not form_data['cpf'] or not form_data['login'] or not form_data['senha']:
      self.tela.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False

    return True

  def fill_form(self) -> None:
    pessoas_data = self.carrega_dados()
    if self.is_edit():
      self.tela.inputNome.setText(pessoas_data[self.id_row]['nome'])
      self.tela.inputCpf.setText(pessoas_data[self.id_row]['cpf'])
      self.tela.inputCelular.setText(pessoas_data[self.id_row]['telefone_celular'])
      self.tela.inputEmail.setText(pessoas_data[self.id_row]['email'])
      self.tela.inputLogin.setText(pessoas_data[self.id_row]['login'])
      self.tela.inputSenha.setText(pessoas_data[self.id_row]['senha'])
      self.tela.isGestor.setChecked(bool(pessoas_data[self.id_row]['is_gestor']))
    else:
      self.tela.inputNome.clear()
      self.tela.inputCpf.clear()
      self.tela.inputCelular.clear()
      self.tela.inputEmail.clear()
      self.tela.inputLogin.clear()
      self.tela.inputSenha.clear()
      self.tela.isGestor.setChecked(False)

  def encode_senha(self, senha) -> str:
    pessoas_data = self.carrega_dados()
    if self.is_edit() and pessoas_data[self.id_row]['senha'] == senha:
      return senha
    senha_bytes = senha.encode('utf-8')
    senha_codificada = b64encode(senha_bytes)
    
    return senha_codificada.decode('utf-8')

  def conecta_controlador_tela(self) -> None:
    self.tela.confirmarBtn.clicked.connect(self.confirmar)
    self.tela.cancelarBtn.clicked.connect(self.tela.hide)
  
