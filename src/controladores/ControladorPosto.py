# UC005: Cadastrar, Visualizar, Editar os Dados do Posto de Gasolina


from src.abstract.ControladorBase import ControladorBase
from src.telas.TelaPosto import TelaPosto
from src.entidades.Posto import Posto

class ControladorPosto(ControladorBase):
  def __init__(self, tela: TelaPosto, entidade: str):
    super().__init__(tela, entidade)

  def confirmar(self) -> None:
    posto_data = self.carrega_dados()
    form_data = {
      'nome_posto': self.tela.inputNome.text().strip(), 
      'chave_pix': self.tela.inputPix.text().strip(),
      'cnpj': self.tela.inputCnpj.text().strip()
      }
    if self.is_form_valido(form_data):
      posto_dto = Posto(
        nome_posto=form_data['nome_posto'],
        chave_pix=form_data['chave_pix'],
        cnpj=form_data['cnpj']
      )
      posto_data[self.id_row] = posto_dto.transforma_para_dict()
      self.salva_dados(posto_data)
      self.tela.hide()

  def is_form_valido(self, form_data: dict) -> bool:
    if not form_data['nome_posto'] or not form_data['cnpj'] or not form_data['chave_pix']:
      self.tela.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False
    
    return True
  
  def fill_form(self) -> None:
    posto_data = self.carrega_dados()
    self.tela.inputNome.setText(posto_data[self.id_row]['nome_posto'])
    self.tela.inputCnpj.setText(posto_data[self.id_row]['cnpj'])
    self.tela.inputPix.setText(posto_data[self.id_row]['chave_pix'])

  def conecta_controlador_tela(self) -> None:
    self.tela.confirmarBtn.clicked.connect(self.confirmar)
    self.tela.cancelarBtn.clicked.connect(self.tela.hide)
  
