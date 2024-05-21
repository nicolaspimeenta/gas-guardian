from src.abstract.TelaBase import TelaBase
from PyQt6 import QtCore, QtGui, QtWidgets

class InicialGlobal(TelaBase):
  def __init__(self):
    super().__init__()
    self.abre_tela(self)

  def iniciar_abastecimento(self):
    # função chamada ao clicar botão "INICIAR ABASTECIMENTO"
    print(self.IniciarAbastecimento)

  def acessa_sistema(self):
    # função chamada ao clicar botão "Acessar Sistema"
    self.hide()
    from src.forms.FormLogin import Login
    self.login = Login()
    self.login.show()

  def abre_tela(self, InicialGlobal):
    InicialGlobal.setObjectName("InicialGlobal")
    InicialGlobal.resize(600, 400)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(InicialGlobal.sizePolicy().hasHeightForWidth())
    InicialGlobal.setSizePolicy(sizePolicy)
    InicialGlobal.setMinimumSize(QtCore.QSize(600, 400))
    InicialGlobal.setMaximumSize(QtCore.QSize(600, 400))
    InicialGlobal.setAutoFillBackground(False)
    InicialGlobal.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Portuguese, QtCore.QLocale.Country.Brazil))
    self.ContainerBtnIniciarAbastecimento = QtWidgets.QFrame(parent=InicialGlobal)
    self.ContainerBtnIniciarAbastecimento.setGeometry(QtCore.QRect(-1, -1, 600, 400))
    self.ContainerBtnIniciarAbastecimento.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerBtnIniciarAbastecimento.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerBtnIniciarAbastecimento.setObjectName("ContainerBtnIniciarAbastecimento")
    self.gridLayout = QtWidgets.QGridLayout(self.ContainerBtnIniciarAbastecimento)
    self.gridLayout.setContentsMargins(100, 100, 100, 100)
    self.gridLayout.setObjectName("gridLayout")
    self.IniciarAbastecimento = QtWidgets.QPushButton(parent=self.ContainerBtnIniciarAbastecimento)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.IniciarAbastecimento.sizePolicy().hasHeightForWidth())
    self.IniciarAbastecimento.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setBold(False)
    self.IniciarAbastecimento.setFont(font)
    self.IniciarAbastecimento.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\telas\\../assets/bomba-combustivel.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.IniciarAbastecimento.setIcon(icon)
    self.IniciarAbastecimento.setDefault(False)
    self.IniciarAbastecimento.setFlat(False)
    self.IniciarAbastecimento.setObjectName("IniciarAbastecimento")
    self.gridLayout.addWidget(self.IniciarAbastecimento, 0, 0, 1, 1)
    self.ContainerBtnAcessarSistema = QtWidgets.QFrame(parent=InicialGlobal)
    self.ContainerBtnAcessarSistema.setGeometry(QtCore.QRect(20, 360, 581, 44))
    self.ContainerBtnAcessarSistema.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerBtnAcessarSistema.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerBtnAcessarSistema.setObjectName("ContainerBtnAcessarSistema")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.ContainerBtnAcessarSistema)
    self.horizontalLayout.setObjectName("horizontalLayout")
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    self.AcessaSistema = QtWidgets.QPushButton(parent=self.ContainerBtnAcessarSistema)
    self.AcessaSistema.setObjectName("AcessaSistema")
    self.horizontalLayout.addWidget(self.AcessaSistema)
    _translate = QtCore.QCoreApplication.translate
    InicialGlobal.setWindowTitle(_translate("InicialGlobal", "GasGuardian"))
    self.IniciarAbastecimento.setText(_translate("InicialGlobal", "INICIAR ABASTECIMENTO"))
    self.AcessaSistema.setText(_translate("InicialGlobal", "Acessar Sistema"))
    QtCore.QMetaObject.connectSlotsByName(InicialGlobal)
    self.IniciarAbastecimento.clicked.connect(self.iniciar_abastecimento)
    self.AcessaSistema.clicked.connect(self.acessa_sistema)