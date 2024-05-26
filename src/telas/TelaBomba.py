# UC006: Cadastrar, Visualizar, Editar e Excluir Bombas de Combustível


from src.abstract.TelaBase import TelaBase
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QLineEdit, QTableWidget, QPushButton, QCheckBox

class TelaBomba(TelaBase):
  def __init__(self):
    super().__init__()
    self.inputId = QLineEdit()
    self.isAutoAbastecimento = QCheckBox()
    self.tableSelecionados = QTableWidget()
    self.tableTipos = QTableWidget()
    self.confirmarBtn = QPushButton()
    self.cancelarBtn = QPushButton()
    self.cria_tela(self)

  def cria_tela(self, FormularioBomba) -> None:
    FormularioBomba.setObjectName("FormularioBomba")
    FormularioBomba.resize(822, 343)
    self.ContainerForm = QtWidgets.QFrame(parent=FormularioBomba)
    self.ContainerForm.setGeometry(QtCore.QRect(0, 0, 821, 421))
    self.ContainerForm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerForm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerForm.setObjectName("ContainerForm")
    self.label = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label.setGeometry(QtCore.QRect(10, 10, 76, 16))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
    self.label.setSizePolicy(sizePolicy)
    self.label.setObjectName("label")
    self.inputId = QtWidgets.QLineEdit(parent=self.ContainerForm)
    self.inputId.setGeometry(QtCore.QRect(10, 30, 133, 22))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputId.sizePolicy().hasHeightForWidth())
    self.inputId.setSizePolicy(sizePolicy)
    self.inputId.setObjectName("inputId")
    self.isAutoAbastecimento = QtWidgets.QCheckBox(parent=self.ContainerForm)
    self.isAutoAbastecimento.setGeometry(QtCore.QRect(160, 30, 132, 20))
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.isAutoAbastecimento.sizePolicy().hasHeightForWidth())
    self.isAutoAbastecimento.setSizePolicy(sizePolicy)
    self.isAutoAbastecimento.setObjectName("isAutoAbastecimento")
    self.removerBtn = QtWidgets.QPushButton(parent=self.ContainerForm)
    self.removerBtn.setGeometry(QtCore.QRect(370, 180, 82, 24))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.removerBtn.setIcon(icon)
    self.removerBtn.setObjectName("removerBtn")
    self.tableSelecionados = QtWidgets.QTableWidget(parent=self.ContainerForm)
    self.tableSelecionados.setGeometry(QtCore.QRect(470, 90, 341, 201))
    self.tableSelecionados.setShowGrid(False)
    self.tableSelecionados.setObjectName("tableSelecionados")
    self.tableSelecionados.setColumnCount(2)
    self.tableSelecionados.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.tableSelecionados.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.tableSelecionados.setHorizontalHeaderItem(1, item)
    self.tableSelecionados.horizontalHeader().setDefaultSectionSize(135)
    self.tableSelecionados.horizontalHeader().setSortIndicatorShown(True)
    self.tableSelecionados.horizontalHeader().setStretchLastSection(True)
    self.adicionarBtn = QtWidgets.QPushButton(parent=self.ContainerForm)
    self.adicionarBtn.setGeometry(QtCore.QRect(370, 150, 82, 24))
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/right.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.adicionarBtn.setIcon(icon1)
    self.adicionarBtn.setObjectName("adicionarBtn")
    self.tableTipos = QtWidgets.QTableWidget(parent=self.ContainerForm)
    self.tableTipos.setGeometry(QtCore.QRect(10, 90, 341, 201))
    self.tableTipos.setShowGrid(False)
    self.tableTipos.setObjectName("tableTipos")
    self.tableTipos.setColumnCount(2)
    self.tableTipos.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.tableTipos.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.tableTipos.setHorizontalHeaderItem(1, item)
    self.tableTipos.horizontalHeader().setDefaultSectionSize(135)
    self.tableTipos.horizontalHeader().setSortIndicatorShown(True)
    self.tableTipos.horizontalHeader().setStretchLastSection(True)
    self.registrosLabel = QtWidgets.QLabel(parent=self.ContainerForm)
    self.registrosLabel.setGeometry(QtCore.QRect(10, 60, 142, 32))
    self.registrosLabel.setObjectName("registrosLabel")
    self.selecionadosLabel = QtWidgets.QLabel(parent=self.ContainerForm)
    self.selecionadosLabel.setGeometry(QtCore.QRect(470, 60, 142, 32))
    self.selecionadosLabel.setObjectName("selecionadosLabel")
    self.ContainerBotoes = QtWidgets.QFrame(parent=self.ContainerForm)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 300, 821, 41))
    self.ContainerBotoes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerBotoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerBotoes.setObjectName("ContainerBotoes")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.ContainerBotoes)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.cancelarBtn = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/cancel.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.cancelarBtn.setIcon(icon2)
    self.cancelarBtn.setObjectName("Cancelar")
    self.horizontalLayout.addWidget(self.cancelarBtn)
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    self.confirmarBtn = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/check.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.confirmarBtn.setIcon(icon3)
    self.confirmarBtn.setObjectName("Confirmar")
    self.horizontalLayout.addWidget(self.confirmarBtn)
    FormularioBomba.setWindowTitle("Nova Pessoa")
    self.label.setText("ID da Bomba *")
    self.isAutoAbastecimento.setText("Auto-abastecimento")
    self.removerBtn.setText("Remover")
    self.tableSelecionados.setSortingEnabled(True)
    item = self.tableSelecionados.horizontalHeaderItem(0)
    item.setText("Nome")
    item = self.tableSelecionados.horizontalHeaderItem(1)
    item.setText("Preço (R$)")
    self.adicionarBtn.setText("Adicionar")
    self.tableTipos.setSortingEnabled(True)
    item = self.tableTipos.horizontalHeaderItem(0)
    item.setText("Nome")
    item = self.tableTipos.horizontalHeaderItem(1)
    item.setText("Preço (R$)")
    self.registrosLabel.setText("Tipos de Combustíveis:")
    self.selecionadosLabel.setText("Selecionados:")
    self.cancelarBtn.setText("Cancelar")
    self.confirmarBtn.setText("Confirmar")
    QtCore.QMetaObject.connectSlotsByName(FormularioBomba)