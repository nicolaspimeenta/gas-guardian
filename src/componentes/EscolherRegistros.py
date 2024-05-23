from src.abstract.FormBase import TelaBase
from PyQt6 import QtCore, QtGui, QtWidgets

class EscolherRegistrosComponent(TelaBase):
  def __init__(self, entidade: str):
    super().__init__()
    self.entidade = entidade
    self.cria_tela(self)
    self.selecionados = []

  def open(self, selecionados_data: list) -> None:
    registros_data = self.carrega_dados(entidade=self.entidade)
    self.fill_table(registros_data, self.tableRegistros)
    if selecionados_data:
      if self.entidade == 'tipos-combustivel':
        for selecionado in selecionados_data:
          for registro in registros_data:
            if registro['nome'] == selecionado and registro['nome'] and registro not in self.selecionados:
              self.selecionados.append(registro)

      self.fill_table(self.selecionados, self.tableSelecionados)
      
    self.show()

  def adicionar(self) -> None:
    registros_data = self.carrega_dados(entidade=self.entidade)
    selected_row = self.tableRegistros.currentRow()

    if selected_row == -1:
      self.mostra_aviso("Nenhum registro selecionado.")
      return

    if registros_data[selected_row] in self.selecionados:
      self.mostra_aviso("Registro já está na lista de selecionados.")
      return
    
    self.selecionados.append(registros_data[selected_row])
    self.fill_table(self.selecionados, self.tableSelecionados)

  def remover(self) -> None:
    selected_row = self.tableSelecionados.currentRow()

    if selected_row == -1:
      self.mostra_aviso("Nenhum registro selecionado.")
      return
    
    self.selecionados.remove(self.selecionados[selected_row])
    self.fill_table(self.selecionados, self.tableSelecionados)

  def cria_tela(self, ComponentEscolherRegistros) -> None:
    ComponentEscolherRegistros.setObjectName("ComponentEscolherRegistros")
    ComponentEscolherRegistros.resize(823, 240)
    self.tableSelecionados = QtWidgets.QTableWidget(parent=ComponentEscolherRegistros)
    self.tableSelecionados.setGeometry(QtCore.QRect(470, 30, 341, 201))
    self.tableSelecionados.setShowGrid(False)
    self.tableSelecionados.setObjectName("tableSelecionados")
    self.tableSelecionados.setColumnCount(0)
    self.tableSelecionados.setRowCount(0)
    self.tableSelecionados.horizontalHeader().setDefaultSectionSize(135)
    self.tableSelecionados.horizontalHeader().setSortIndicatorShown(True)
    self.tableSelecionados.horizontalHeader().setStretchLastSection(True)
    self.adicionarBtn = QtWidgets.QPushButton(parent=ComponentEscolherRegistros)
    self.adicionarBtn.setGeometry(QtCore.QRect(370, 90, 82, 24))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/right.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.adicionarBtn.setIcon(icon)
    self.adicionarBtn.setObjectName("adicionarBtn")
    self.registrosLabel = QtWidgets.QLabel(parent=ComponentEscolherRegistros)
    self.registrosLabel.setGeometry(QtCore.QRect(10, 0, 142, 32))
    self.registrosLabel.setObjectName("registrosLabel")
    self.selecionadosLabel = QtWidgets.QLabel(parent=ComponentEscolherRegistros)
    self.selecionadosLabel.setGeometry(QtCore.QRect(470, 0, 142, 32))
    self.selecionadosLabel.setObjectName("selecionadosLabel")
    self.removerBtn = QtWidgets.QPushButton(parent=ComponentEscolherRegistros)
    self.removerBtn.setGeometry(QtCore.QRect(370, 120, 82, 24))
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.removerBtn.setIcon(icon1)
    self.removerBtn.setObjectName("removerBtn")
    self.tableRegistros = QtWidgets.QTableWidget(parent=ComponentEscolherRegistros)
    self.tableRegistros.setGeometry(QtCore.QRect(10, 30, 341, 201))
    self.tableRegistros.setShowGrid(False)
    self.tableRegistros.setObjectName("tableRegistros")
    self.tableRegistros.setColumnCount(0)
    self.tableRegistros.setRowCount(0)
    self.tableRegistros.horizontalHeader().setDefaultSectionSize(135)
    self.tableRegistros.horizontalHeader().setSortIndicatorShown(True)
    self.tableRegistros.horizontalHeader().setStretchLastSection(True)
    ComponentEscolherRegistros.setWindowTitle("Escolher Registros")
    self.tableSelecionados.setSortingEnabled(True)
    self.adicionarBtn.setText("Adicionar")
    self.registrosLabel.setText("Registros:")
    self.selecionadosLabel.setText("Selecionados:")
    self.removerBtn.setText("Remover")
    self.tableRegistros.setSortingEnabled(True)
    QtCore.QMetaObject.connectSlotsByName(ComponentEscolherRegistros)
    self.adicionarBtn.clicked.connect(self.adicionar) 
    self.removerBtn.clicked.connect(self.remover)
    if self.entidade == 'tipos-combustivel':
      self.setWindowTitle('Escolher Tipos')
      self.registrosLabel.setText('Tipos de Combustível:')
      self.tableRegistros.setColumnCount(2)
      self.tableRegistros.setRowCount(0)
      item = QtWidgets.QTableWidgetItem()
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
      self.tableRegistros.setHorizontalHeaderItem(0, item)
      item = QtWidgets.QTableWidgetItem()
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
      self.tableRegistros.setHorizontalHeaderItem(1, item)
      self.tableRegistros.horizontalHeader().setDefaultSectionSize(165)
      self.tableRegistros.horizontalHeader().setSortIndicatorShown(True)
      self.tableRegistros.horizontalHeader().setStretchLastSection(True)
      self.tableRegistros.setSortingEnabled(False)
      item = self.tableRegistros.horizontalHeaderItem(0)
      item.setText('Nome')
      item = self.tableRegistros.horizontalHeaderItem(1)
      item.setText('Preço (R$)')
      self.tableSelecionados.setColumnCount(2)
      self.tableSelecionados.setRowCount(0)
      item = QtWidgets.QTableWidgetItem()
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
      self.tableSelecionados.setHorizontalHeaderItem(0, item)
      item = QtWidgets.QTableWidgetItem()
      item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
      self.tableSelecionados.setHorizontalHeaderItem(1, item)
      self.tableSelecionados.horizontalHeader().setDefaultSectionSize(165)
      self.tableSelecionados.horizontalHeader().setSortIndicatorShown(True)
      self.tableSelecionados.horizontalHeader().setStretchLastSection(True)
      self.tableSelecionados.setSortingEnabled(False)
      item = self.tableSelecionados.horizontalHeaderItem(0)
      item.setText('Nome')
      item = self.tableSelecionados.horizontalHeaderItem(1)
      item.setText('Preço (R$)')
