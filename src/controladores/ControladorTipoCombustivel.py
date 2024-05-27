# UC002: Cadastrar, Visualizar, Editar e Excluir Tipos de Combustível

from src.abstract.ControladorBase import ControladorBase
from src.entidades.TipoCombustivel import TipoCombustivel
from src.telas.TelaTipoCombustivel import TelaTipoCombustivel
from src.controladores.ControladorTanque import ControladorTanque
from src.controladores.ControladorBomba import ControladorBomba

class ControladorTipoCombustivel(ControladorBase):
  def __init__(self, tela: TelaTipoCombustivel, entidade: str):
    super().__init__(tela, entidade)
    self.controladorTanque = ControladorTanque()
    self.controladorBomba = ControladorBomba()

  def confirmar(self) -> None:
    tipos_data = self.carrega_dados()
    form_data = {
      'nome': self.tela.inputNome.text().strip(),
      'preco': float(self.tela.inputPreco.cleanText().replace(',', '.'))
    }
    if self.is_form_valido(form_data):
      tipo_combustivel_dto = TipoCombustivel(
        nome=form_data['nome'],
        preco=form_data['preco']
      )
      if self.is_edit():
        self.controladorTanque.atualiza_tipos(antigo_nome=tipos_data[self.id_row]['nome'], novo_nome=form_data['nome'])
        self.controladorBomba.atualiza_tipos(antigo_nome=tipos_data[self.id_row]['nome'], novo_nome=form_data['nome'])
        tipos_data[self.id_row] = tipo_combustivel_dto.transforma_para_dict()
        self.salva_dados(tipos_data)
        self.tela.hide()
      else:
        tipos_data.append(tipo_combustivel_dto.transforma_para_dict())
        self.tela.mostra_mensagem('Um novo Tipo de combustível foi cadastrado.')
        self.salva_dados(tipos_data)
        self.tela.hide()
  
  def is_form_valido(self, form_data: dict) -> bool:
    tipos_data = self.carrega_dados()
    if not (self.is_edit() and form_data['nome'] == tipos_data[self.id_row]['nome']):
      for tipo in tipos_data:
        if tipo['nome'].lower() == form_data['nome'].lower():
          self.tela.mostra_aviso("Tipo de combustível já cadastrado.")
          return False
    
    if not form_data['nome']:
      self.tela.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False

    return True

  def fill_form(self) -> None:
    tipos_data = self.carrega_dados()
    if self.is_edit():
      self.tela.inputNome.setText(tipos_data[self.id_row]['nome'])
      self.tela.inputPreco.setValue(float(tipos_data[self.id_row]['preco']))
    else:
      self.tela.inputNome.clear()
      self.tela.inputPreco.setValue(0.01)

  def exclui_registro(self, id_row: int) -> None:
    tipos_data = self.carrega_dados(entidade='tipos-combustivel')
    tipo_excluido = tipos_data[id]['nome']
    #
    bombas_data = self.carrega_dados(entidade='bombas')
    for bomba in bombas_data:
        bomba['tipos_combustivel'] = [tipo for tipo in bomba['tipos_combustivel'] if tipo != tipo_excluido]
    self.salva_dados(
      data=bombas_data, 
      entidade='bombas'
      )
    #
    self.salva_dados(
      data=[tanque for tanque in self.carrega_dados(entidade='tanques') if tanque['tipo'] != tipo_excluido], 
      entidade='tanques'
      )
    super().exclui_registro(id_row)

  def conecta_controlador_tela(self) -> None:
    self.tela.confirmarBtn.clicked.connect(self.confirmar)
    self.tela.cancelarBtn.clicked.connect(self.tela.hide)
  
