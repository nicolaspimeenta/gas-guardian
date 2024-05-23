# UC008: Registrar um Abastecimento

from src.abstract.FormBase import FormBase
from PyQt6 import QtCore, QtGui, QtWidgets
import datetime

class FormularioAbastecimento(FormBase):
  def __init__(self):
    super().__init__(entidade='abastecimentos')
    self.cria_tela(self)

  def confirmar(self) -> None:
    abastecimento_data = self.carrega_dados(entidade='abastecimentos')
    novo_abastecimento = {
      'id_bomba': self.inputBomba.currentText(),
      'id_tipo': self.inputTipo.currentText(),
      'preco': self.inputPreco.cleanText(),
      'litros': self.inputLitros.text().strip(),
      'data': datetime.datetime.now().isoformat()
    }
    abastecimento_data.append(novo_abastecimento)
    QtWidgets.QMessageBox.information(self, "Sucesso", "Um novo Abastecimento foi cadastrado.",
    QtWidgets.QMessageBox.StandardButton.Ok)
    self.salva_dados(abastecimento_data, entidade='abastecimentos')
    self.hide()
  
  def fill_form(self) -> None:
    self.inputBomba.clear()
    self.inputTipo.clear()
    self.inputPreco.setValue(0.01)
    self.inputLitros.clear()
    self.inputBomba.addItems(
      bomba['id_bomba'] for bomba in self.carrega_dados(entidade='bombas') if bool(bomba['is_auto_abastecimento']) is False
    )

  def bomba_changed(self) -> None:
    self.inputTipo.clear()
    for bomba in self.carrega_dados(entidade='bombas'):
      if bomba['id_bomba'] == self.inputBomba.currentText():
        self.inputTipo.addItems(bomba['tipos_combustivel'])

  def preco_changed(self) -> None:
    tipos_data = self.carrega_dados(entidade='tipos-combustivel')
    for tipo in tipos_data:
      if tipo['nome'] == self.inputTipo.currentText():
        preco_tipo = float(tipo['preco'])

    self.inputLitros.setText(str( round(self.inputPreco.value() / preco_tipo, 2) ))
  
  def cria_tela(self, FormularioAbastecimento) -> None:
    FormularioAbastecimento.setObjectName("FormularioAbastecimento")
    FormularioAbastecimento.resize(300, 202)
    self.ContainerForm = QtWidgets.QFrame(parent=FormularioAbastecimento)
    self.ContainerForm.setGeometry(QtCore.QRect(0, 0, 301, 201))
    self.ContainerForm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerForm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerForm.setObjectName("ContainerForm")
    self.formLayout = QtWidgets.QFormLayout(self.ContainerForm)
    self.formLayout.setObjectName("formLayout")
    self.inputBomba = QtWidgets.QComboBox(parent=self.ContainerForm)
    self.inputBomba.setEnabled(True)
    self.inputBomba.setObjectName("inputBomba")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.inputBomba)
    self.label_2 = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
    self.label_2.setSizePolicy(sizePolicy)
    self.label_2.setObjectName("label_2")
    self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
    self.label_3 = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
    self.label_3.setSizePolicy(sizePolicy)
    self.label_3.setObjectName("label_3")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
    self.inputTipo = QtWidgets.QComboBox(parent=self.ContainerForm)
    self.inputTipo.setEnabled(True)
    self.inputTipo.setObjectName("inputTipo")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.inputTipo)
    self.label = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
    self.label.setSizePolicy(sizePolicy)
    self.label.setObjectName("label")
    self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label)
    self.label_4 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_4.setObjectName("label_4")
    self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
    self.inputPreco = QtWidgets.QDoubleSpinBox(parent=self.ContainerForm)
    self.inputPreco.setMinimum(0.01)
    self.inputPreco.setMaximum(9999.99)
    self.inputPreco.setSingleStep(0.5)
    self.inputPreco.setObjectName("inputPreco")
    self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputPreco)
    self.inputLitros = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputLitros.sizePolicy().hasHeightForWidth())
    self.inputLitros.setSizePolicy(sizePolicy)
    self.inputLitros.setReadOnly(True)
    self.inputLitros.setObjectName("inputLitros")
    self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputLitros)
    self.ContainerBotoes = QtWidgets.QFrame(parent=FormularioAbastecimento)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 160, 301, 44))
    self.ContainerBotoes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerBotoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerBotoes.setObjectName("ContainerBotoes")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.ContainerBotoes)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.Cancelar = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/cancel.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Cancelar.setIcon(icon)
    self.Cancelar.setObjectName("Cancelar")
    self.horizontalLayout.addWidget(self.Cancelar)
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    self.Confirmar = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/check.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Confirmar.setIcon(icon1)
    self.Confirmar.setObjectName("Confirmar")
    self.horizontalLayout.addWidget(self.Confirmar)
    FormularioAbastecimento.setWindowTitle("Nova Pessoa")
    self.label_2.setText("Bomba")
    self.label_3.setText("Tipo de combustivel")
    self.label.setText("Litros abastecidos")
    self.label_4.setText("Preço")
    self.Cancelar.setText("Cancelar")
    self.Confirmar.setText("Confirmar")
    QtCore.QMetaObject.connectSlotsByName(FormularioAbastecimento)
    self.inputBomba.currentIndexChanged.connect(self.bomba_changed)
    self.inputPreco.textChanged.connect(self.preco_changed)
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.hide)
  
