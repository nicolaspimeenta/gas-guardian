from src.abstract.TelaBase import TelaBase
from PyQt6 import QtCore, QtGui, QtWidgets

class InicialGestor(TelaBase):
  def __init__(self):
    super().__init__()
    self.cria_tela(self)

  def cadastros(self) -> None:
    self.hide()
    from src.Cadastros import Cadastros
    self.cadastros = Cadastros()
    self.cadastros.show()

  def desconectar(self) -> None:
    self.hide()
    from src.forms.FormularioLogin import FormularioLogin
    self.formularioLogin = FormularioLogin()
    self.formularioLogin.show()

  def cria_tela(self, InicialGestor) -> None:
    InicialGestor.setObjectName("InicialGestor")
    InicialGestor.setWindowModality(QtCore.Qt.WindowModality.NonModal)
    InicialGestor.resize(600, 400)
    InicialGestor.setMinimumSize(QtCore.QSize(600, 400))
    InicialGestor.setMaximumSize(QtCore.QSize(600, 400))
    self.ContainerButtons = QtWidgets.QFrame(parent=InicialGestor)
    self.ContainerButtons.setGeometry(QtCore.QRect(0, 0, 600, 401))
    self.ContainerButtons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerButtons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerButtons.setObjectName("ContainerButtons")
    self.gridLayout = QtWidgets.QGridLayout(self.ContainerButtons)
    self.gridLayout.setContentsMargins(10, 100, 10, 100)
    self.gridLayout.setObjectName("gridLayout")
    self.Renovacao = QtWidgets.QPushButton(parent=self.ContainerButtons)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.Renovacao.sizePolicy().hasHeightForWidth())
    self.Renovacao.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setBold(False)
    self.Renovacao.setFont(font)
    self.Renovacao.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/plus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Renovacao.setIcon(icon)
    self.Renovacao.setDefault(False)
    self.Renovacao.setFlat(False)
    self.Renovacao.setObjectName("Renovacao")
    self.gridLayout.addWidget(self.Renovacao, 0, 1, 1, 1)
    self.Relatorios = QtWidgets.QPushButton(parent=self.ContainerButtons)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.Relatorios.sizePolicy().hasHeightForWidth())
    self.Relatorios.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setBold(False)
    self.Relatorios.setFont(font)
    self.Relatorios.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/data.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Relatorios.setIcon(icon1)
    self.Relatorios.setDefault(False)
    self.Relatorios.setFlat(False)
    self.Relatorios.setObjectName("Relatorios")
    self.gridLayout.addWidget(self.Relatorios, 0, 0, 1, 1)
    self.Cadastros = QtWidgets.QPushButton(parent=self.ContainerButtons)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.Cadastros.sizePolicy().hasHeightForWidth())
    self.Cadastros.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setBold(False)
    self.Cadastros.setFont(font)
    self.Cadastros.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/cadastros.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Cadastros.setIcon(icon2)
    self.Cadastros.setDefault(False)
    self.Cadastros.setFlat(False)
    self.Cadastros.setObjectName("Cadastros")
    self.gridLayout.addWidget(self.Cadastros, 0, 2, 1, 1)
    self.ContainerBotoes = QtWidgets.QFrame(parent=InicialGestor)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 360, 601, 44))
    self.ContainerBotoes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerBotoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerBotoes.setObjectName("ContainerBotoes")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.ContainerBotoes)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.Desconectar = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/logout.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Desconectar.setIcon(icon3)
    self.Desconectar.setObjectName("Desconectar")
    self.horizontalLayout.addWidget(self.Desconectar)
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    _translate = QtCore.QCoreApplication.translate
    InicialGestor.setWindowTitle(_translate("InicialGestor", "Form"))
    self.Renovacao.setText(_translate("InicialGestor", "REGISTRAR RENOVAÇÃO DE ESTOQUE"))
    self.Relatorios.setText(_translate("InicialGestor", "RELATÓRIOS"))
    self.Cadastros.setText(_translate("InicialGestor", "CADASTROS"))
    self.Desconectar.setText(_translate("InicialGestor", "Desconectar"))
    QtCore.QMetaObject.connectSlotsByName(InicialGestor)
    self.Cadastros.clicked.connect(self.cadastros)
    self.Desconectar.clicked.connect(self.desconectar)