# UC008: Registrar um Abastecimento

from datetime import datetime
from src.abstract.ControladorBase import ControladorBase
from src.entidades.Abastecimento import Abastecimento
from src.telas.TelaAbastecimento import TelaAbastecimento

class ControladorAbastecimento(ControladorBase):
  def __init__(self):
    super().__init__()
    self.telaAbastecimento = TelaAbastecimento()
    self.conecta_controlador_tela()

  def confirmar(self) -> None:
    abastecimento_data = self.carrega_dados(entidade='abastecimentos')
    form_data = {
      'id_bomba': self.telaAbastecimento.inputBomba.currentText(),
      'id_tipo': self.telaAbastecimento.inputTipo.currentText(),
      'preco': self.telaAbastecimento.inputPreco.cleanText(),
      'litros': self.telaAbastecimento.inputLitros.text().strip()
    }
    abastecimento_dto = Abastecimento(
      id_bomba=form_data['id_bomba'],
      id_tipo=form_data['id_tipo'],
      preco=form_data['preco'],
      litros=form_data['litros'],
      data=datetime.now().isoformat()
    )
    abastecimento_data.append(abastecimento_dto.transforma_para_dict())
    self.telaAbastecimento.mostra_mensagem("Um novo Abastecimento foi registrado")
    self.salva_dados(abastecimento_data, entidade='abastecimentos')
    self.hide()
  
  def fill_form(self) -> None:
    self.telaAbastecimento.inputBomba.clear()
    self.telaAbastecimento.inputTipo.clear()
    self.telaAbastecimento.inputLitros.clear()
    self.telaAbastecimento.inputPreco.setValue(0.01)
    self.telaAbastecimento.inputBomba.addItems(
      bomba['id_bomba'] for bomba in self.carrega_dados(entidade='bombas') if bool(bomba['is_auto_abastecimento']) is False
    )

  def bomba_changed(self) -> None:
    self.telaAbastecimento.inputTipo.clear()
    for bomba in self.carrega_dados(entidade='bombas'):
      if bomba['id_bomba'] == self.telaAbastecimento.inputBomba.currentText():
        self.telaAbastecimento.inputTipo.addItems(bomba['tipos_combustivel'])

  def preco_changed(self) -> None:
    tipos_data = self.carrega_dados(entidade='tipos-combustivel')
    for tipo in tipos_data:
      if tipo['nome'] == self.telaAbastecimento.inputTipo.currentText():
        preco_tipo = float(tipo['preco'])
    self.telaAbastecimento.inputLitros.setText(str( round(float(self.telaAbastecimento.inputPreco.text().replace(',', '.')) / preco_tipo, 2) ))

  def conecta_controlador_tela(self) -> None:
    self.telaAbastecimento.inputBomba.currentIndexChanged.connect(self.bomba_changed)
    self.telaAbastecimento.inputPreco.textChanged.connect(self.preco_changed)
    self.telaAbastecimento.confirmarBtn.clicked.connect(self.confirmar)
    self.telaAbastecimento.cancelarBtn.clicked.connect(self.hide)
  
