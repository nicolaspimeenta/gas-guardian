from src.abstract.FormBase import FormBase
from PyQt6 import QtCore, QtGui, QtWidgets

class FormTipos(FormBase):
  def __init__(self, id_row: int, title: str):
    super().__init__(id_row=id_row, title=title, dados='tipos-combustivel')
    self.abre_tela(self)

  def confirmar(self) -> None:
    # função chamada ao clicar botão "Confirmar"
    tipos_data = self.carrega_dados(entidade='tipos-combustivel')
    form_data = {'nome': self.InputNome.text().strip(), 'preco': self.InputPreco.text().strip()}
    if self.is_form_valido(form_data):
      if self.is_edit():
        tipos_data[self.id_row] = form_data
        self.salva_dados(tipos_data, entidade='tipos-combustivel')
        self.hide()
      else:
        tipos_data.append(form_data)
        QtWidgets.QMessageBox.information(self, "Sucesso", "Um novo Tipo de combustível foi cadastrado.",
        QtWidgets.QMessageBox.StandardButton.Ok)
        self.salva_dados(tipos_data, entidade='tipos-combustivel')
        self.hide()

  def is_form_valido(self, form_data) -> bool:
    tipos_data = self.carrega_dados(entidade='tipos-combustivel')
    if not (self.is_edit() and form_data['nome'] == tipos_data[self.id_row]['nome']): # apenas checar se tiver mudado o nome ou não for edição
      for tipo in tipos_data: # Checa se o tipo de combustível já foi cadastrado
        if tipo['nome'].lower() == form_data['nome'].lower():
          self.mostra_aviso("Tipo já cadastrado.")
          return False
    
    if not form_data['nome'] or not form_data['preco']: # Checa se o formulário foi preenchido
      self.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False
    
    try:
      form_data['preco'] = round(float(form_data['preco'].replace(',', '.')), 2) # Checa se o preço é um número
      form_data['preco'] = "{:.2f}".format(form_data['preco']) # Transforma em uma string com 2 casas decimais
    except:
      self.mostra_aviso("O campo 'Preço' precisa ser um número.")
      return False
    
    if not (float(form_data['preco']) > 0):
        self.mostra_aviso("O campo 'Preço' precisa ser um número maior que 0.")
        return False

    return True
  
  def abre_tela(self, FormTipos) -> None:
    FormTipos.setObjectName("FormTipos")
    FormTipos.resize(260, 120)
    FormTipos.setMinimumSize(QtCore.QSize(260, 120))
    FormTipos.setMaximumSize(QtCore.QSize(260, 120))
    self.ContainerForm = QtWidgets.QFrame(parent=FormTipos)
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
    self.InputNome = QtWidgets.QLineEdit(parent=self.ContainerForm)
    self.InputNome.setObjectName("InputNome")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.InputNome)
    self.InputPreco = QtWidgets.QLineEdit(parent=self.ContainerForm)
    self.InputPreco.setMaxLength(10)
    self.InputPreco.setObjectName("InputPreco")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.InputPreco)
    self.ContainerBotoes = QtWidgets.QFrame(parent=FormTipos)
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
    FormTipos.setWindowTitle(_translate("FormTipos", self.title))
    self.label.setText(_translate("FormTipos", "Nome *"))
    self.label_2.setText(_translate("FormTipos", "Preço *"))
    self.Cancelar.setText(_translate("FormTipos", "Cancelar"))
    self.Confirmar.setText(_translate("FormTipos", "Confirmar"))
    QtCore.QMetaObject.connectSlotsByName(FormTipos)
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.cancelar)
    tipos_data = self.carrega_dados(entidade='tipos-combustivel')
    if self.is_edit():
      self.InputNome.setText(tipos_data[self.id_row]['nome'])
      self.InputPreco.setText(tipos_data[self.id_row]['preco'])
  
