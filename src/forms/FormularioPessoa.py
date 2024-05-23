from base64 import b64encode
from validate_docbr import CPF
from src.abstract.AbstractForm import AbstractForm
from PyQt6 import QtCore, QtGui, QtWidgets

class FormularioPessoa(AbstractForm):
  def __init__(self):
    super().__init__(entidade='pessoas')
    self.cria_tela(self)

  def confirmar(self) -> None:
    pessoas_data = self.carrega_dados(entidade='pessoas')
    form_data = {
      'nome': self.inputNome.text().strip(),
      'cpf': self.inputCpf.text().strip(),
      'email': self.inputEmail.text().strip(),
      'telefoneCelular': self.inputCelular.text().strip(),
      'login': self.inputLogin.text().strip(),
      'senha': self.encode_senha(self.inputSenha.text().strip()),
      'is_gestor': self.isGestor.isChecked()
      }
    if self.is_form_valido(form_data):
      if self.is_edit():
        pessoas_data[self.id_row] = form_data
        self.salva_dados(pessoas_data, entidade='pessoas')
        self.hide()
      else:
        pessoas_data.append(form_data)
        QtWidgets.QMessageBox.information(self, "Sucesso", "Uma nova Pessoa foi cadastrada.",
        QtWidgets.QMessageBox.StandardButton.Ok)
        self.salva_dados(pessoas_data, entidade='pessoas')
        self.hide()

  def is_form_valido(self, form_data) -> bool:
    pessoas_data = self.carrega_dados(entidade='pessoas')
    if not (self.is_edit() and form_data['cpf'] == pessoas_data[self.id_row]['cpf']):
      for pessoa in pessoas_data:
        if pessoa['cpf'] == form_data['cpf']:
          self.mostra_aviso("Pessoa já cadastrada.")
          return False
    
    # Checa se o formulário foi preenchido
    if not form_data['nome'] or not form_data['cpf'] or not form_data['login'] or not form_data['senha']:
      self.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False

    try:
      cpf = CPF()
      if not cpf.validate(form_data['cpf']):
        raise ValueError
    except:
      self.mostra_aviso("CPF Inválido")
      return False

    return True
  
  def fill_form(self) -> None:
    pessoas_data = self.carrega_dados(entidade='pessoas')
    if self.is_edit():
      self.inputNome.setText(pessoas_data[self.id_row]['nome'])
      self.inputCpf.setText(pessoas_data[self.id_row]['cpf'])
      self.inputCelular.setText(pessoas_data[self.id_row]['telefoneCelular'])
      self.inputEmail.setText(pessoas_data[self.id_row]['email'])
      self.inputLogin.setText(pessoas_data[self.id_row]['login'])
      self.inputSenha.setText(pessoas_data[self.id_row]['senha'])
      self.isGestor.setChecked(bool(pessoas_data[self.id_row]['is_gestor']))
    else:
      self.inputNome.clear()
      self.inputCpf.clear()
      self.inputCelular.clear()
      self.inputEmail.clear()
      self.inputLogin.clear()
      self.inputSenha.clear()
      self.isGestor.setChecked(False)
  
  def encode_senha(self, senha) -> str:
    pessoas_data = self.carrega_dados(entidade='pessoas')
    if self.is_edit() and pessoas_data[self.id_row]['senha'] == senha:
      return senha
    senha_bytes = senha.encode('utf-8')
    senha_codificada = b64encode(senha_bytes)
    
    return senha_codificada.decode('utf-8')
  
  def cria_tela(self, FormularioPessoa) -> None:
    FormularioPessoa.setObjectName("FormularioPessoa")
    FormularioPessoa.resize(300, 217)
    self.ContainerForm = QtWidgets.QFrame(parent=FormularioPessoa)
    self.ContainerForm.setGeometry(QtCore.QRect(0, 0, 301, 201))
    self.ContainerForm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerForm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerForm.setObjectName("ContainerForm")
    self.formLayout = QtWidgets.QFormLayout(self.ContainerForm)
    self.formLayout.setObjectName("formLayout")
    self.inputNome = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputNome.sizePolicy().hasHeightForWidth())
    self.inputNome.setSizePolicy(sizePolicy)
    self.inputNome.setObjectName("InputNome")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputNome)
    self.inputCpf = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputCpf.sizePolicy().hasHeightForWidth())
    self.inputCpf.setSizePolicy(sizePolicy)
    self.inputCpf.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.inputCpf.setObjectName("InputCpf")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputCpf)
    self.label_4 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_4.setObjectName("label_4")
    self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
    self.inputCelular = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputCelular.sizePolicy().hasHeightForWidth())
    self.inputCelular.setSizePolicy(sizePolicy)
    self.inputCelular.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.inputCelular.setObjectName("InputCelular")
    self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputCelular)
    self.inputEmail = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputEmail.sizePolicy().hasHeightForWidth())
    self.inputEmail.setSizePolicy(sizePolicy)
    self.inputEmail.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.inputEmail.setObjectName("InputEmail")
    self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputEmail)
    self.label_3 = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
    self.label_3.setSizePolicy(sizePolicy)
    self.label_3.setObjectName("label_3")
    self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_3)
    self.label_2 = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
    self.label_2.setSizePolicy(sizePolicy)
    self.label_2.setObjectName("label_2")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_2)
    self.label = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
    self.label.setSizePolicy(sizePolicy)
    self.label.setObjectName("label")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
    self.label_5 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_5.setObjectName("label_5")
    self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
    self.inputSenha = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputSenha.sizePolicy().hasHeightForWidth())
    self.inputSenha.setSizePolicy(sizePolicy)
    self.inputSenha.setInputMask("")
    self.inputSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
    self.inputSenha.setObjectName("inputSenha")
    self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputSenha)
    self.label_6 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_6.setObjectName("label_6")
    self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_6)
    self.inputLogin = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputLogin.sizePolicy().hasHeightForWidth())
    self.inputLogin.setSizePolicy(sizePolicy)
    self.inputLogin.setInputMask("")
    self.inputLogin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.inputLogin.setObjectName("inputLogin")
    self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputLogin)
    self.isGestor = QtWidgets.QCheckBox(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.isGestor.sizePolicy().hasHeightForWidth())
    self.isGestor.setSizePolicy(sizePolicy)
    self.isGestor.setObjectName("Gestor")
    self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.isGestor)
    self.ContainerBotoes = QtWidgets.QFrame(parent=FormularioPessoa)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 180, 301, 44))
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
    self.label_4.setText(_translate("FormularioPessoa", "Celular"))
    self.inputCelular.setInputMask(_translate("FormularioPessoa", "(00) 00000-0000"))
    self.label_3.setText(_translate("FormularioPessoa", "Email"))
    self.label_2.setText(_translate("FormularioPessoa", "CPF *"))
    self.label.setText(_translate("FormularioPessoa", "Nome *"))
    self.label_5.setText(_translate("FormularioPessoa", "Login *"))
    self.label_6.setText(_translate("FormularioPessoa", "Senha *"))
    self.isGestor.setText(_translate("FormularioPessoa", "Gestor"))
    self.Cancelar.setText(_translate("FormularioPessoa", "Cancelar"))
    self.Confirmar.setText(_translate("FormularioPessoa", "Confirmar"))
    QtCore.QMetaObject.connectSlotsByName(FormularioPessoa)
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.cancelar)
