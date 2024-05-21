from src.abstract.AbstractForm import AbstractForm
from PyQt6 import QtCore, QtGui, QtWidgets

class FormularioTanques(AbstractForm):
  def __init__(self):
    super().__init__(entidade='tanques')
    self.cria_tela(self)
    self.tanques_data = self.carrega_dados(entidade='tanques')

  def confirmar(self) -> None:
    # função chamada ao clicar botão "Confirmar"
    form_data = {
      'id_tanque': self.inputId.text().strip(), 
      'tipo': self.inputTipo.currentText(),
      'volume_atual': self.tanques_data[self.id_row]['volume_atual'] if self.is_edit() else 0,
      'capacidade_maxima': self.inputCapacidade.text().strip().replace(',', '.'),
      'porcentagem_alerta': self.inputPorcentagem.cleanText(),
    }
    if self.is_form_valido(form_data):
      if self.is_edit():
        self.tanques_data[self.id_row] = form_data
        self.salva_dados(self.tanques_data, entidade='tanques')
        self.hide()
      else:
        self.tanques_data.append(form_data)
        QtWidgets.QMessageBox.information(self, "Sucesso", "Um novo Tanque foi cadastrado.",
        QtWidgets.QMessageBox.StandardButton.Ok)
        self.salva_dados(self.tanques_data, entidade='tanques')
        self.hide()

  def is_form_valido(self, form_data) -> bool:
    if not (self.is_edit() and form_data['id_tanque'] == self.tanques_data[self.id_row]['id_tanque']):
      for tanque in self.tanques_data: # Checa se o tanque de combustível já foi cadastrado
        if tanque['id_tanque'].lower() == form_data['id_tanque'].lower():
          self.mostra_aviso("Tanque já cadastrado.")
          return False
    
    if not form_data['id_tanque'] or not form_data['capacidade_maxima'] : # Checa se o formulário foi preenchido
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
    self.inputTipo.clear()
    self.inputTipo.addItems(
      tipo['nome'] for tipo in self.carrega_dados(entidade='tipos-combustivel')
    )

    if self.is_edit():
      self.inputId.setText(self.tanques_data[self.id_row]['id_tanque'])
      self.inputCapacidade.setText(self.tanques_data[self.id_row]['capacidade_maxima'])
      self.inputPorcentagem.setSpecialValueText(self.tanques_data[self.id_row]['porcentagem_alerta'])
      self.inputTipo.setCurrentText(self.tanques_data[self.id_row]['tipo'])
    else:
      self.inputId.clear()
      self.inputCapacidade.clear()
      self.inputPorcentagem.clear()
  
  def cria_tela(self, FormularioTanque) -> None:
    FormularioTanque.setObjectName("FormularioTanque")
    FormularioTanque.resize(300, 162)
    self.ContainerForm = QtWidgets.QFrame(parent=FormularioTanque)
    self.ContainerForm.setGeometry(QtCore.QRect(0, 10, 301, 151))
    self.ContainerForm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerForm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerForm.setObjectName("ContainerForm")
    self.formLayout = QtWidgets.QFormLayout(self.ContainerForm)
    self.formLayout.setObjectName("formLayout")
    self.label = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
    self.label.setSizePolicy(sizePolicy)
    self.label.setObjectName("label")
    self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
    self.inputId = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputId.sizePolicy().hasHeightForWidth())
    self.inputId.setSizePolicy(sizePolicy)
    self.inputId.setObjectName("inputId")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputId)
    self.label_3 = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
    self.label_3.setSizePolicy(sizePolicy)
    self.label_3.setObjectName("label_3")
    self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_3)
    self.inputPorcentagem = QtWidgets.QSpinBox(parent=self.ContainerForm)
    self.inputPorcentagem.setMinimum(1)
    self.inputPorcentagem.setObjectName("inputPorcentagem")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputPorcentagem)
    self.label_2 = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
    self.label_2.setSizePolicy(sizePolicy)
    self.label_2.setObjectName("label_2")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
    self.inputCapacidade = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputCapacidade.sizePolicy().hasHeightForWidth())
    self.inputCapacidade.setSizePolicy(sizePolicy)
    self.inputCapacidade.setObjectName("inputCapacidade")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputCapacidade)
    self.label_4 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_4.setObjectName("label_4")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_4)
    self.inputTipo = QtWidgets.QComboBox(parent=self.ContainerForm)
    self.inputTipo.setEnabled(True)
    self.inputTipo.setObjectName("inputTipo")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputTipo)
    self.ContainerBotoes = QtWidgets.QFrame(parent=FormularioTanque)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 120, 301, 44))
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
    self.label.setText(_translate("FormularioTanque", "ID do Tanque *"))
    self.label_3.setText(_translate("FormularioTanque", "Porcentagem de Alerta *"))
    self.label_2.setText(_translate("FormularioTanque", "Capacidade máxima (L) *"))
    self.label_4.setText(_translate("FormularioTanque", "Tipo de Combustível *"))
    self.Cancelar.setText(_translate("FormularioTanque", "Cancelar"))
    self.Confirmar.setText(_translate("FormularioTanque", "Confirmar"))
    QtCore.QMetaObject.connectSlotsByName(FormularioTanque)
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.cancelar)
  
