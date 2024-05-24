# UC008: Registrar um Abastecimento

from src.abstract.ControladorBase import ControladorBase
from src.telas.TelaTanque import TelaTanque
from src.entidades.Bomba import Bomba

class ControladorTanque(ControladorBase):
  def __init__(self):
    super().__init__(tela=TelaTanque, entidade='tanques')

  def confirmar(self) -> None:
    tanques_data = self.carrega_dados()
    form_data = {
      'id_tanque': self.tela.inputId.text().strip(), 
      'tipo': self.tela.inputTipo.currentText(),
      'volume_atual': tanques_data[self.id_row]['volume_atual'] if self.is_edit() else 0,
      'capacidade_maxima': self.tela.inputCapacidade.text().strip().replace(',', '.'),
      'porcentagem_alerta': self.tela.inputPorcentagem.cleanText()
    }
    if self.is_form_valido(form_data):
      if self.is_edit():
        tanques_data[self.id_row] = form_data
        self.salva_dados(tanques_data)
        self.tela.hide()
      else:
        tanques_data.append(form_data)
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
    
    if not form_data['id_tanque'] or not form_data['capacidade_maxima']:
      self.tela.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False
    
    try:
      float(form_data['capacidade_maxima'])
    except:
      self.tela.mostra_aviso("O campo 'Capacidade Máxima' precisa ser um número.")
      return False
    
    if not (float(form_data['capacidade_maxima']) > 0):
        self.tela.mostra_aviso("O campo 'Capacidade Máxima' precisa ser um número maior que 0.")
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
      self.tela.inputCapacidade.setText(tanques_data[self.id_row]['capacidade_maxima'])
      self.tela.inputPorcentagem.setValue(int(tanques_data[self.id_row]['porcentagem_alerta']))
      self.tela.inputTipo.setCurrentText(tanques_data[self.id_row]['tipo'])
    else:
      self.tela.inputId.clear()
      self.tela.inputCapacidade.clear()
      self.tela.inputPorcentagem.clear()

  def conecta_controlador_tela(self) -> None:
    self.tela.confirmarBtn.clicked.connect(self.confirmar)
    self.tela.cancelarBtn.clicked.connect(self.tela.hide)
  
