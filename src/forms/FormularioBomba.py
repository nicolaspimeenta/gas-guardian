from src.abstract.AbstractForm import AbstractForm
from PyQt6 import QtCore, QtGui, QtWidgets
from src.componentes.EscolherRegistros import EscolherRegistrosComponent

class FormularioBomba(AbstractForm):
  def __init__(self):
    super().__init__(entidade='bombas')
    self.cria_tela(self)
    self.bombas_data = self.carrega_dados(entidade='bombas')
    self.escolherTiposComponent = EscolherRegistrosComponent(entidade='tipos-combustivel')

  def confirmar(self) -> None:
    # função chamada ao clicar botão "Confirmar"
    form_data = {
      'id_bomba': self.inputId.text().strip(),
      'is_auto_abastecimento': self.isAutoAbastecimento.isChecked(),
      'tipos_combustivel': []
    }
    if self.is_form_valido(form_data):
      if self.is_edit():
        self.bombas_data[self.id_row] = form_data
        self.salva_dados(self.bombas_data, entidade='bombas')
        self.hide()
      else:
        self.bombas_data.append(form_data)
        QtWidgets.QMessageBox.information(self, "Sucesso", "Uma nova Bomba foi cadastrada.",
        QtWidgets.QMessageBox.StandardButton.Ok)
        self.salva_dados(self.bombas_data, entidade='bombas')
        self.hide()

  def is_form_valido(self, form_data) -> bool:
    if not (self.is_edit() and form_data['id_bomba'] == self.bombas_data[self.id_row]['id_bomba']):
      for tanque in self.bombas_data:
        if tanque['id_tanque'].lower() == form_data['id_tanque'].lower():
          self.mostra_aviso("Tanque já cadastrado.")
          return False
    
    if not form_data['id_tanque'] or not form_data['capacidade_maxima']:
      self.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False
    
    try:
      float(form_data['capacidade_maxima'])
    except:
      self.mostra_aviso("O campo 'Capacidade Máxima' precisa ser um número.")
      return False
    
    if not (float(form_data['capacidade_maxima']) > 0):
        self.mostra_aviso("O campo 'Capacidade Máxima' precisa ser um número maior que 0.")
        return False

    return True
  
  def fill_form(self) -> None:
    if self.is_edit():
      self.inputId.setText(self.bombas_data[self.id_row]['id_tanque'])
      self.inputCapacidade.setText(self.bombas_data[self.id_row]['capacidade_maxima'])
      self.inputPorcentagem.setSpecialValueText(self.bombas_data[self.id_row]['porcentagem_alerta'])
      self.inputTipo.setCurrentText(self.bombas_data[self.id_row]['tipo'])
    else:
      self.inputId.clear()
      self.inputCapacidade.clear()
      self.inputPorcentagem.clear()

  def escolherTipo(self) -> None:
    self.escolherTiposComponent.open()
  
  def cria_tela(self, FormularioBomba) -> None:
    FormularioBomba.setObjectName("FormularioBomba")
    FormularioBomba.resize(302, 140)
    self.ContainerForm = QtWidgets.QFrame(parent=FormularioBomba)
    self.ContainerForm.setGeometry(QtCore.QRect(0, 0, 301, 101))
    self.ContainerForm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerForm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerForm.setObjectName("ContainerForm")
    self.formLayout = QtWidgets.QFormLayout(self.ContainerForm)
    self.formLayout.setObjectName("formLayout")
    self.inputId = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputId.sizePolicy().hasHeightForWidth())
    self.inputId.setSizePolicy(sizePolicy)
    self.inputId.setObjectName("inputId")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputId)
    self.label = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
    self.label.setSizePolicy(sizePolicy)
    self.label.setObjectName("label")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
    self.escolherTipoBtn = QtWidgets.QPushButton(parent=self.ContainerForm)
    self.escolherTipoBtn.setObjectName("escolherTipoBtn")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.escolherTipoBtn)
    self.isAutoAbastecimento = QtWidgets.QCheckBox(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.isAutoAbastecimento.sizePolicy().hasHeightForWidth())
    self.isAutoAbastecimento.setSizePolicy(sizePolicy)
    self.isAutoAbastecimento.setObjectName("isAutoAbastecimento")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.isAutoAbastecimento)
    self.ContainerBotoes = QtWidgets.QFrame(parent=FormularioBomba)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 100, 301, 41))
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
    FormularioBomba.setWindowTitle(_translate("FormularioBomba", "Nova Pessoa"))
    self.label.setText(_translate("FormularioBomba", "ID da Bomba *"))
    self.escolherTipoBtn.setText(_translate("FormularioBomba", "Escolher Tipos de Combustível da Bomba"))
    self.isAutoAbastecimento.setText(_translate("FormularioBomba", "Auto-abastecimento"))
    self.Cancelar.setText(_translate("FormularioBomba", "Cancelar"))
    self.Confirmar.setText(_translate("FormularioBomba", "Confirmar"))
    QtCore.QMetaObject.connectSlotsByName(FormularioBomba)
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.cancelar)
    self.escolherTipoBtn.clicked.connect(self.escolherTipo)
  
