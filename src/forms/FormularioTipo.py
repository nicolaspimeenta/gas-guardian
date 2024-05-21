from src.abstract.AbstractForm import AbstractForm
from PyQt6 import QtCore, QtGui, QtWidgets

class FormularioTipo(AbstractForm):
  def __init__(self):
    super().__init__(entidade='tipos-combustivel')
    self.cria_tela(self)
    self.tipos_data = self.carrega_dados(entidade='tipos-combustivel')

  def confirmar(self) -> None:
    # função chamada ao clicar botão "Confirmar"
    form_data = {
      'nome': self.inputNome.text().strip(), 
      'preco': self.inputPreco.text().strip().replace(',', '.')
    }
    if self.is_form_valido(form_data):
      if self.is_edit():
        self.tipos_data[self.id_row] = form_data
        self.salva_dados(self.tipos_data, entidade='tipos-combustivel')
        self.hide()
      else:
        self.tipos_data.append(form_data)
        QtWidgets.QMessageBox.information(self, "Sucesso", "Um novo Tipo de combustível foi cadastrado.",
        QtWidgets.QMessageBox.StandardButton.Ok)
        self.salva_dados(self.tipos_data, entidade='tipos-combustivel')
        self.hide()

  def is_form_valido(self, form_data) -> bool:
    if not (self.is_edit() and form_data['nome'] == self.tipos_data[self.id_row]['nome']): # apenas checar se tiver mudado o nome ou não for edição
      for tipo in self.tipos_data: # Checa se o tipo de combustível já foi cadastrado
        if tipo['nome'].lower() == form_data['nome'].lower():
          self.mostra_aviso("Tipo já cadastrado.")
          return False
    
    if not form_data['nome'] or not form_data['preco']: # Checa se o formulário foi preenchido
      self.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False
    
    try:
      form_data['preco'] = round(float(form_data['preco']), 2) # Checa se o preço é um número
      form_data['preco'] = "{:.2f}".format(form_data['preco']) # Transforma em uma string com 2 casas decimais
    except:
      self.mostra_aviso("O campo 'Preço' precisa ser um número.")
      return False
    
    if not (float(form_data['preco']) > 0):
        self.mostra_aviso("O campo 'Preço' precisa ser um número maior que 0.")
        return False

    return True
  
  def fill_form(self) -> None:
    if self.is_edit():
      self.inputNome.setText(self.tipos_data[self.id_row]['nome'])
      self.inputPreco.setText(self.tipos_data[self.id_row]['preco'])
    else:
      self.inputNome.clear()
      self.inputPreco.clear()
  
  def cria_tela(self, FormularioTipo) -> None:
    FormularioTipo.setObjectName("FormularioTipo")
    FormularioTipo.resize(260, 120)
    FormularioTipo.setMinimumSize(QtCore.QSize(260, 120))
    FormularioTipo.setMaximumSize(QtCore.QSize(260, 120))
    self.ContainerForm = QtWidgets.QFrame(parent=FormularioTipo)
    self.ContainerForm.setGeometry(QtCore.QRect(0, 10, 260, 60))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.ContainerForm.sizePolicy().hasHeightForWidth())
    self.ContainerForm.setSizePolicy(sizePolicy)
    self.ContainerForm.setMinimumSize(QtCore.QSize(260, 60))
    self.ContainerForm.setMaximumSize(QtCore.QSize(260, 60))
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
    self.inputNome.setObjectName("InputNome")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputNome)
    self.inputPreco = QtWidgets.QLineEdit(parent=self.ContainerForm)
    self.inputPreco.setMaxLength(10)
    self.inputPreco.setObjectName("InputPreco")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputPreco)
    self.ContainerBotoes = QtWidgets.QFrame(parent=FormularioTipo)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 80, 261, 44))
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
    self.label.setText(_translate("FormularioTipo", "Nome *"))
    self.label_2.setText(_translate("FormularioTipo", "Preço *"))
    self.Cancelar.setText(_translate("FormularioTipo", "Cancelar"))
    self.Confirmar.setText(_translate("FormularioTipo", "Confirmar"))
    QtCore.QMetaObject.connectSlotsByName(FormularioTipo)
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.cancelar)
  
