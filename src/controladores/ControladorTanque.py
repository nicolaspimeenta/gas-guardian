# UC003: Cadastrar, Visualizar, Editar e Excluir Tanques de Combustível


from src.abstract.ControladorBase import ControladorBase
from src.telas.TelaTanque import TelaTanque
from src.entidades.Tanque import Tanque

class ControladorTanque(ControladorBase):
  def __init__(self, tela: TelaTanque, entidade: str):
    super().__init__(tela, entidade)

  def confirmar(self) -> None:
    tanques_data = self.carrega_dados()
    form_data = {
      'id_tanque': self.tela.inputId.text().strip(), 
      'tipo_combustivel': self.tela.inputTipo.currentText(),
      'volume_atual': tanques_data[self.id_row]['volume_atual'] if self.is_edit() else 0,
      'capacidade_maxima': float(self.tela.inputCapacidade.cleanText().replace(',', '.')),
      'porcentagem_alerta': int(self.tela.inputPorcentagem.cleanText())
    }
    if self.is_form_valido(form_data):
      tanque_dto = Tanque(
        id_tanque=form_data['id_tanque'],
        tipo_combustivel=form_data['tipo_combustivel'],
        volume_atual=form_data['volume_atual'],
        capacidade_maxima=form_data['capacidade_maxima'],
        porcentagem_alerta=form_data['porcentagem_alerta']
      )
      if self.is_edit():
        tanques_data[self.id_row] = tanque_dto.transforma_para_dict()
        self.salva_dados(tanques_data)
        self.tela.hide()
      else:
        tanques_data.append(tanque_dto.transforma_para_dict())
        self.tela.mostra_mensagem('Um novo Tanque foi cadastrado.')
        self.salva_dados(tanques_data)
        self.tela.hide()

  def is_form_valido(self, form_data: dict) -> bool:
    tanques_data = self.carrega_dados()
    if not (self.is_edit() and form_data['id_tanque'] == tanques_data[self.id_row]['id_tanque']):
      for tanque in tanques_data:
        if tanque['id_tanque'].lower() == form_data['id_tanque'].lower():
          self.tela.mostra_aviso("Tanque já cadastrado.")
          return False
    
    if not form_data['id_tanque'] or not form_data['tipo_combustivel']:
      self.tela.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False

    return True
  
  def fill_form(self) -> None:
    tanques_data = self.carrega_dados()
    self.tela.inputTipo.clear()
    self.tela.inputTipo.addItems(
      tipo['nome'] for tipo in self.carrega_dados(entidade='tipos-combustivel')
    )

    if self.is_edit():
      self.tela.inputId.setText(tanques_data[self.id_row]['id_tanque'])
      self.tela.inputCapacidade.setValue(float(tanques_data[self.id_row]['capacidade_maxima']))
      self.tela.inputPorcentagem.setValue(int(tanques_data[self.id_row]['porcentagem_alerta']))
      self.tela.inputTipo.setCurrentText(tanques_data[self.id_row]['tipo_combustivel'])
    else:
      self.tela.inputId.clear()
      self.tela.inputCapacidade.setValue(1)
      self.tela.inputPorcentagem.setValue(1)

  def atualiza_tipos(self, antigo_nome: str, novo_nome: str):
    tanques_data = self.carrega_dados()
    for tanque in tanques_data:
      if antigo_nome == tanque['tipo_combustivel']:
        tanque['tipo_combustivel'] = novo_nome
    self.salva_dados(tanques_data)

  def conecta_controlador_tela(self) -> None:
    self.tela.confirmarBtn.clicked.connect(self.confirmar)
    self.tela.cancelarBtn.clicked.connect(self.tela.hide)


  
