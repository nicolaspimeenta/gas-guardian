# UC008: Registrar um Abastecimento

from datetime import datetime
from src.abstract.ControladorBase import ControladorBase
from src.entidades.Abastecimento import Abastecimento
from src.telas.TelaAbastecimento import TelaAbastecimento

class ControladorAbastecimento(ControladorBase):
  def __init__(self, tela: TelaAbastecimento, entidade: str):
    super().__init__(tela, entidade)

  def confirmar(self) -> None:
    abastecimento_data = self.carrega_dados()
    form_data = {
      'id_bomba': self.tela.inputBomba.currentText(),
      'id_tipo': self.tela.inputTipo.currentText(),
      'preco': float(self.tela.inputPreco.cleanText().replace(',', '.')),
      'litros': float(self.tela.inputLitros.text().strip())
    }
    abastecimento_dto = Abastecimento(
      id_bomba=form_data['id_bomba'],
      id_tipo=form_data['id_tipo'],
      preco=form_data['preco'],
      litros=form_data['litros'],
      data=datetime.now().isoformat()
    )
    abastecimento_data.append(abastecimento_dto.transforma_para_dict())
    self.tela.mostra_mensagem("Um novo Abastecimento foi registrado")
    self.salva_dados(abastecimento_data)
    self.tela.hide()
  
  def fill_form(self) -> None:
    self.tela.inputBomba.clear()
    self.tela.inputTipo.clear()
    self.tela.inputLitros.clear()
    self.tela.inputPreco.setValue(0.01)
    self.tela.inputBomba.addItems(
      bomba['id_bomba'] for bomba in self.carrega_dados(entidade='bombas') if bool(bomba['is_auto_abastecimento']) is False
    )

  def bomba_changed(self) -> None:
    self.tela.inputTipo.clear()
    for bomba in self.carrega_dados(entidade='bombas'):
      if bomba['id_bomba'] == self.tela.inputBomba.currentText():
        self.tela.inputTipo.addItems(bomba['tipos_combustivel'])

  def preco_changed(self) -> None:
    tipos_data = self.carrega_dados(entidade='tipos-combustivel')
    preco_tipo = None
    for tipo in tipos_data:
      if tipo['nome'] == self.tela.inputTipo.currentText():
        preco_tipo = float(tipo['preco'])
      self.tela.inputLitros.setText(str( round(float(self.tela.inputPreco.cleanText().replace(',', '.')) / preco_tipo if preco_tipo else 0, 2) ))

  def conecta_controlador_tela(self) -> None:
    self.tela.inputBomba.currentIndexChanged.connect(self.bomba_changed)
    self.tela.inputPreco.textChanged.connect(self.preco_changed)
    self.tela.confirmarBtn.clicked.connect(self.confirmar)
    self.tela.cancelarBtn.clicked.connect(self.tela.hide)

  def is_form_valido(self) -> None:
    pass
  
