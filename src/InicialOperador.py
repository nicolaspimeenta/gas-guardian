from src.abstract.TelaBase import TelaBase
from PyQt6 import QtCore, QtGui, QtWidgets
from src.controladores.ControladorAbastecimento import ControladorAbastecimento
from src.telas.TelaAbastecimento import TelaAbastecimento
class InicialOperador(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.controladorAbastecimento = ControladorAbastecimento(tela=TelaAbastecimento(), entidade='abastecimentos')
    self.cria_tela(self)

  def registrar_abastecimento(self) -> None:
    self.controladorAbastecimento.abre_tela(id_row=None, title='Registrar Abastecimento')

  def desconectar(self) -> None:
    self.hide()
    from src.Login import Login
    self.login = Login()
    self.login.show()

  def cria_tela(self, InicialOperador) -> None:
    InicialOperador.setObjectName("InicialOperador")
    InicialOperador.setWindowModality(QtCore.Qt.WindowModality.NonModal)
    InicialOperador.resize(600, 400)
    InicialOperador.setMinimumSize(QtCore.QSize(600, 400))
    InicialOperador.setMaximumSize(QtCore.QSize(600, 400))
    self.ContainerButtons = QtWidgets.QFrame(parent=InicialOperador)
    self.ContainerButtons.setGeometry(QtCore.QRect(0, 0, 600, 401))
    self.ContainerButtons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerButtons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerButtons.setObjectName("ContainerButtons")
    self.gridLayout = QtWidgets.QGridLayout(self.ContainerButtons)
    self.gridLayout.setContentsMargins(10, 100, 10, 100)
    self.gridLayout.setObjectName("gridLayout")
    self.registrarAbastecimentoBtn = QtWidgets.QPushButton(parent=self.ContainerButtons)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.registrarAbastecimentoBtn.sizePolicy().hasHeightForWidth())
    self.registrarAbastecimentoBtn.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setBold(False)
    self.registrarAbastecimentoBtn.setFont(font)
    self.registrarAbastecimentoBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/bomba-combustivel.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.registrarAbastecimentoBtn.setIcon(icon)
    self.registrarAbastecimentoBtn.setDefault(False)
    self.registrarAbastecimentoBtn.setFlat(False)
    self.registrarAbastecimentoBtn.setObjectName("registrarAbastecimentoBtn")
    self.gridLayout.addWidget(self.registrarAbastecimentoBtn, 0, 0, 1, 1)
    self.ContainerBotoes = QtWidgets.QFrame(parent=InicialOperador)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 360, 601, 44))
    self.ContainerBotoes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerBotoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerBotoes.setObjectName("ContainerBotoes")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.ContainerBotoes)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.Desconectar = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/logout.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Desconectar.setIcon(icon1)
    self.Desconectar.setObjectName("Desconectar")
    self.horizontalLayout.addWidget(self.Desconectar)
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    InicialOperador.setWindowTitle("GasGuardian")
    self.registrarAbastecimentoBtn.setText("REGISTRAR ABASTECIMENTO")
    self.Desconectar.setText("Desconectar")
    QtCore.QMetaObject.connectSlotsByName(InicialOperador)
    #
    self.registrarAbastecimentoBtn.clicked.connect(self.registrar_abastecimento)
    self.Desconectar.clicked.connect(self.desconectar)