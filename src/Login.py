# UC009: Efetuar login

from base64 import b64decode
from PyQt6 import QtCore, QtGui, QtWidgets
from src.abstract.FormBase import FormBase
from src.InicialGestor import InicialGestor
from src.InicialGlobal import InicialGlobal
from src.InicialOperador import InicialOperador

class Login(FormBase):
  def __init__(self):
    super().__init__(entidade=None)
    self.inicialGestor = InicialGestor()
    self.inicialGlobal = InicialGlobal()
    self.inicialOperador = InicialOperador()
    self.cria_tela(self)

  def confirmar(self) -> None:
    login_digitado = self.inputLogin.text()
    senha_digitado = self.inputSenha.text()
    pessoas_data = self.carrega_dados('pessoas')
    pessoa_logado = None

    for pessoa in pessoas_data:
      if pessoa['login'].strip().lower() == login_digitado.strip().lower() and self.decode_senha(pessoa['senha']) == senha_digitado:
        pessoa_logado = pessoa

    if pessoa_logado is None:
      self.mostra_aviso("Usuário ou senha incorretos.")
      return

    if bool(pessoa_logado['is_gestor']):
      self.hide()
      self.inicialGestor.show()
    else:
      self.hide()
      self.inicialOperador.show()
      return

  def cancelar(self) -> None:
    self.hide()
    self.inicialGlobal.show()

  def decode_senha(self, senha) -> str:
    senha_bytes = b64decode(senha)
    senha_original = senha_bytes.decode('utf-8')
    return senha_original
  
  def cria_tela(self, Login) -> None:
    Login.setObjectName("Login")
    Login.resize(600, 400)
    self.ContainerLogin = QtWidgets.QFrame(parent=Login)
    self.ContainerLogin.setGeometry(QtCore.QRect(210, 130, 153, 114))
    self.ContainerLogin.setFrameShape(QtWidgets.QFrame.Shape.Box)
    self.ContainerLogin.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerLogin.setObjectName("ContainerLogin")
    self.formLayout = QtWidgets.QFormLayout(self.ContainerLogin)
    self.formLayout.setObjectName("formLayout")
    self.LabelLogin = QtWidgets.QLabel(parent=self.ContainerLogin)
    self.LabelLogin.setObjectName("LabelLogin")
    self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.LabelLogin)
    self.inputLogin = QtWidgets.QLineEdit(parent=self.ContainerLogin)
    self.inputLogin.setMaxLength(100)
    self.inputLogin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.inputLogin.setObjectName("InputLogin")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.inputLogin)
    self.LabelSenha = QtWidgets.QLabel(parent=self.ContainerLogin)
    self.LabelSenha.setObjectName("LabelSenha")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.LabelSenha)
    self.inputSenha = QtWidgets.QLineEdit(parent=self.ContainerLogin)
    self.inputSenha.setMaxLength(100)
    self.inputSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
    self.inputSenha.setObjectName("InputSenha")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.inputSenha)
    self.ContainerBotoes = QtWidgets.QFrame(parent=Login)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 360, 601, 44))
    self.ContainerBotoes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerBotoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerBotoes.setObjectName("ContainerBotoes")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.ContainerBotoes)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.Cancelar = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/cancel.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Cancelar.setIcon(icon)
    self.Cancelar.setObjectName("Cancelar")
    self.horizontalLayout.addWidget(self.Cancelar)
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    self.Confirmar = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/check.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Confirmar.setIcon(icon1)
    self.Confirmar.setObjectName("Confirmar")
    self.horizontalLayout.addWidget(self.Confirmar)
    Login.setWindowTitle("GasGuardian")
    self.LabelLogin.setText("Login")
    self.LabelSenha.setText("Senha")
    self.Cancelar.setText("Cancelar")
    self.Confirmar.setText("Confirmar")
    QtCore.QMetaObject.connectSlotsByName(Login)
    #
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.hide)