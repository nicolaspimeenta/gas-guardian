# UC005: Editar os Dados do Posto de Gasolina

from validate_docbr import CNPJ
from src.abstract.FormBase import FormBase
from PyQt6 import QtCore, QtGui, QtWidgets

class FormularioPosto(FormBase):
  def __init__(self):
    super().__init__(entidade='posto')
    self.cria_tela(self)

  def confirmar(self) -> None:
    posto_data = self.carrega_dados(entidade='posto')
    form_data = {
      'nomePosto': self.inputNome.text().strip(), 
      'chavePix': self.inputPix.text().strip(),
      'cnpj': self.inputCnpj.text().strip()
      }
    if self.is_form_valido(form_data):
      posto_data[self.id_row] = form_data
      self.salva_dados(posto_data, entidade='posto')
      self.hide()

  def is_form_valido(self, form_data) -> bool:
    if not form_data['nomePosto'] or not form_data['cnpj'] or not form_data['chavePix']: # Checa se o formulário foi preenchido
      self.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False
    try:
      cnpj = CNPJ()
      if not cnpj.validate(form_data['cnpj']):
        raise ValueError
    except:
      self.mostra_aviso("CNPJ Inválido")
      return False
    
    return True
  
  def fill_form(self) -> None:
    posto_data = self.carrega_dados(entidade='posto')
    self.inputNome.setText(posto_data[self.id_row]['nomePosto'])
    self.inputCnpj.setText(posto_data[self.id_row]['cnpj'])
    self.inputPix.setText(posto_data[self.id_row]['chavePix'])
  
  def cria_tela(self, FormularioPosto) -> None:
    FormularioPosto.setObjectName("FormularioPosto")
    FormularioPosto.resize(260, 150)
    FormularioPosto.setMinimumSize(QtCore.QSize(260, 150))
    FormularioPosto.setMaximumSize(QtCore.QSize(260, 150))
    self.ContainerForm = QtWidgets.QFrame(parent=FormularioPosto)
    self.ContainerForm.setGeometry(QtCore.QRect(0, 0, 261, 241))
    self.ContainerForm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerForm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerForm.setObjectName("ContainerForm")
    self.formLayout = QtWidgets.QFormLayout(self.ContainerForm)
    self.formLayout.setObjectName("formLayout")
    self.label = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label.setObjectName("label")
    self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
    self.label_2 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_2.setObjectName("label_2")
    self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_2)
    self.inputNome = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputNome.sizePolicy().hasHeightForWidth())
    self.inputNome.setSizePolicy(sizePolicy)
    self.inputNome.setObjectName("InputNome")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputNome)
    self.inputCnpj = QtWidgets.QLineEdit(parent=self.ContainerForm)
    self.inputCnpj.setMaxLength(100)
    self.inputCnpj.setObjectName("InputCnpj")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputCnpj)
    self.label_3 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_3.setObjectName("label_3")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
    self.inputPix = QtWidgets.QLineEdit(parent=self.ContainerForm)
    self.inputPix.setObjectName("InputPix")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.inputPix)
    self.ContainerBotoes = QtWidgets.QFrame(parent=FormularioPosto)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 113, 261, 41))
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
    _translate = QtCore.QCoreApplication.translate
    self.inputCnpj.setInputMask(_translate("FormularioPosto", "00.000.000/0000-00"))
    FormularioPosto.setWindowTitle(_translate("FormularioPosto", "Dados do Posto"))
    self.label.setText(_translate("FormularioPosto", "Nome *"))
    self.label_2.setText(_translate("FormularioPosto", "CNPJ *"))
    self.label_3.setText(_translate("FormularioPosto", "Chave PIX *"))
    self.Cancelar.setText(_translate("FormularioPosto", "Cancelar"))
    self.Confirmar.setText(_translate("FormularioPosto", "Confirmar"))
    QtCore.QMetaObject.connectSlotsByName(FormularioPosto)
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.hide)