from base64 import b64encode
import json
import re
from validate_docbr import CPF
from src.abstract.FormBase import FormBase
from PyQt6 import QtCore, QtGui, QtWidgets

class FormPessoa(FormBase):
  def __init__(self, id_row: int, title: str):
    super().__init__(id_row=id_row, title=title, dados='pessoas')
    self.abre_tela(self)

  def confirmar(self) -> None:
    # função chamada ao clicar botão "Confirmar"
    pessoas_data = self.carrega_dados(entidade='pessoas')
    form_data = {
      'nome': self.InputNome.text().strip(), 
      'cpf': self.InputCpf.text().strip(),
      'email': self.InputEmail.text().strip(),
      'telefoneCelular': self.InputCelular.text().strip(),
      'login': self.InputUsuario.text().strip(),
      'senha': self.inputSenha.text().strip(),
      'gestor': self.Gestor.isChecked()
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
    if not (self.is_edit() and form_data['cpf'] == pessoas_data[self.id_row]['cpf']): # apenas checar se tiver mudado o cpf ou não for edição
      for pessoa in pessoas_data: # Checa se o Pessoa já foi cadastrado
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
  
  def encode_senha(self, senha) -> str:
    if self.is_edit() and self.pessoas_data[self.id_row]['senha'] == senha: 
      return senha
    senha_bytes = senha.encode('utf-8')
    senha_codificada = b64encode(senha_bytes)
    
    return senha_codificada.decode('utf-8')
  
  def abre_tela(self, FormPessoa) -> None:
    FormPessoa.setObjectName("FormPessoa")
    FormPessoa.resize(297, 217)
    self.ContainerForm = QtWidgets.QFrame(parent=FormPessoa)
    self.ContainerForm.setGeometry(QtCore.QRect(0, 0, 301, 201))
    self.ContainerForm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerForm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerForm.setObjectName("ContainerForm")
    self.formLayout = QtWidgets.QFormLayout(self.ContainerForm)
    self.formLayout.setObjectName("formLayout")
    self.InputNome = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.InputNome.sizePolicy().hasHeightForWidth())
    self.InputNome.setSizePolicy(sizePolicy)
    self.InputNome.setObjectName("InputNome")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.InputNome)
    self.InputCpf = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.InputCpf.sizePolicy().hasHeightForWidth())
    self.InputCpf.setSizePolicy(sizePolicy)
    self.InputCpf.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.InputCpf.setObjectName("InputCpf")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.InputCpf)
    self.label_4 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_4.setObjectName("label_4")
    self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
    self.InputCelular = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.InputCelular.sizePolicy().hasHeightForWidth())
    self.InputCelular.setSizePolicy(sizePolicy)
    self.InputCelular.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.InputCelular.setObjectName("InputCelular")
    self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.InputCelular)
    self.InputEmail = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.InputEmail.sizePolicy().hasHeightForWidth())
    self.InputEmail.setSizePolicy(sizePolicy)
    self.InputEmail.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.InputEmail.setObjectName("InputEmail")
    self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.InputEmail)
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
    self.Gestor = QtWidgets.QCheckBox(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.Gestor.sizePolicy().hasHeightForWidth())
    self.Gestor.setSizePolicy(sizePolicy)
    self.Gestor.setObjectName("Gestor")
    self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Gestor)
    self.ContainerBotoes = QtWidgets.QFrame(parent=FormPessoa)
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
    FormPessoa.setWindowTitle(_translate("FormPessoa", "Nova Pessoa"))
    self.label_4.setText(_translate("FormPessoa", "Celular"))
    self.InputCelular.setInputMask(_translate("FormPessoa", "(00) 00000-0000"))
    self.label_3.setText(_translate("FormPessoa", "Email"))
    self.label_2.setText(_translate("FormPessoa", "CPF *"))
    self.label.setText(_translate("FormPessoa", "Nome *"))
    self.label_5.setText(_translate("FormPessoa", "Login *"))
    self.label_6.setText(_translate("FormPessoa", "Senha *"))
    self.Gestor.setText(_translate("FormPessoa", "Gestor"))
    self.Cancelar.setText(_translate("FormPessoa", "Cancelar"))
    self.Confirmar.setText(_translate("FormPessoa", "Confirmar"))
    QtCore.QMetaObject.connectSlotsByName(FormPessoa)
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.cancelar)
    pessoas_data = self.carrega_dados(entidade='pessoas')
    if self.is_edit():
      self.InputNome.setText(pessoas_data[self.id_row]['nome'])
      self.InputCpf.setText(pessoas_data[self.id_row]['cpf'])
      self.InputCelular.setText(pessoas_data[self.id_row]['telefoneCelular'])
      self.InputEmail.setText(pessoas_data[self.id_row]['email'])
      self.inputLogin.setText(pessoas_data[self.id_row]['login'])
      self.inputSenha.setText(pessoas_data[self.id_row]['senha'])
      self.Gestor.setChecked(bool(pessoas_data[self.id_row]['gestor']))
