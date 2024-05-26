# UC001: Cadastrar, Visualizar, Editar e Excluir Usuários
# UC002: Cadastrar, Visualizar, Editar e Excluir Tipos de Combustível
# UC003: Cadastrar, Visualizar, Editar e Excluir Tanques de Combustível
# UC005: Cadastrar, Visualizar, Editar os Dados do Posto de Gasolina
# UC006: Cadastrar, Visualizar, Editar e Excluir Bombas de Combustível

from PyQt6 import QtCore, QtGui, QtWidgets
from src.controladores.ControladorPosto import ControladorPosto
from src.controladores.ControladorBomba import ControladorBomba
from src.controladores.ControladorPessoa import ControladorPessoa
from src.controladores.ControladorTanque import ControladorTanque
from src.controladores.ControladorTipoCombustivel import ControladorTipoCombustivel

class Cadastros(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.controladorTanque = ControladorTanque()
    self.controladorPosto = ControladorPosto()
    self.controladorBomba = ControladorBomba()
    self.controladorPessoa = ControladorPessoa()
    self.controladorTipoCombustivel = ControladorTipoCombustivel()
    self.cria_tela(self)

  def tela_inicial(self) -> None:
    self.hide()
    from src.InicialGestor import InicialGestor
    self.inicialGestor = InicialGestor()
    self.inicialGestor.show()

  def abre_form(self, btn: str) -> None:
    tab_ativa = self.tabWidget.currentIndex()
    self.desativar_botoes()

    if tab_ativa == 0: # Bombas
      selected_row = self.BombasTable.currentRow()
      if btn=='Editar' and selected_row == -1:
        self.controladorBomba.tela.mostra_aviso("Selecione uma linha para editar.")
        return
      self.controladorBomba.abre_tela(
        id_row=selected_row if btn=='Editar' else None,
        title=f"Editando Bomba ({selected_row+1})" if btn=='Editar' else "Nova Bomba"
        )
    
    if tab_ativa == 1: # Tanques
      selected_row = self.TanquesTable.currentRow()
      if btn=='Editar' and selected_row == -1:
        self.controladorTanque.tela.mostra_aviso("Selecione uma linha para editar.")
        return
      self.controladorTanque.abre_tela(
        id_row=selected_row if btn=='Editar' else None,
        title=f"Editando Tanque ({selected_row+1})" if btn=='Editar' else "Novo Tanque"
        )
    
    if tab_ativa == 2: # Tipos
      selected_row = self.TiposTable.currentRow()
      if btn=='Editar' and selected_row == -1:
        self.controladorTipoCombustivel.tela.mostra_aviso("Selecione uma linha para editar.")
        return
      self.controladorTipoCombustivel.abre_tela(
        id_row=selected_row if btn=='Editar' else None,
        title=f"Editando Tipo ({selected_row+1})" if btn=='Editar' else "Novo Tipo"
        )

    if tab_ativa == 3: # Pessoas
      selected_row = self.PessoasTable.currentRow()
      if btn=='Editar' and selected_row == -1:
        self.controladorPessoa.tela.mostra_aviso("Selecione uma linha para editar.")
        return
      self.controladorPessoa.abre_tela(
        id_row=selected_row if btn=='Editar' else None,
        title=f"Editando Pessoa ({selected_row+1})" if btn=='Editar' else 'Nova Pessoa'
        )
    
    if tab_ativa == 4: # Posto
      if btn=='Novo':
        self.controladorPosto.tela.mostra_aviso("Não é permitido criar um registro de Posto.")
        return
      self.controladorPosto.abre_tela(
        id_row=0,
        title="Editando Posto"
        )
      
  def fetch_data(self) -> None:
    self.ativar_botoes()
    self.controladorPessoa.tela.fill_table(self.controladorPessoa.carrega_dados(), self.PessoasTable)
    self.controladorTipoCombustivel.tela.fill_table(self.controladorTipoCombustivel.carrega_dados(), self.TiposTable)
    self.controladorTanque.tela.fill_table(self.controladorTanque.carrega_dados(), self.TanquesTable)
    self.controladorBomba.tela.fill_table(self.controladorBomba.carrega_dados(), self.BombasTable)
    self.controladorPosto.tela.fill_table(self.controladorPosto.carrega_dados(), self.PostoTable)
    
  def excluir(self) -> None:
    tab_ativa = self.tabWidget.currentIndex()

    if tab_ativa == 0: # Bombas
      selected_row = self.BombasTable.currentRow()
      if selected_row == -1:
        self.controladorBomba.tela.mostra_aviso("Selecione uma linha para excluir.")
      else:
        self.controladorBomba.exclui_registro(id_row=selected_row)
    
    if tab_ativa == 1: # Tanques
      selected_row = self.TanquesTable.currentRow()
      if selected_row == -1:
        self.controladorBomba.tela.mostra_aviso("Selecione uma linha para excluir.")
      else:
        self.controladorTanque.exclui_registro(id_row=selected_row)
    
    if tab_ativa == 2: # Tipos
      selected_row = self.TiposTable.currentRow()
      if selected_row == -1:
        self.controladorTipoCombustivel.tela.mostra_aviso("Selecione uma linha para excluir.")
      else:
        self.exclui_tipos(id=selected_row)
        self.controladorTipoCombustivel.exclui_registro(id_row=selected_row)
    
    if tab_ativa == 3: # Pessoas
      selected_row = self.PessoasTable.currentRow()
      if selected_row == -1:
        self.controladorPessoa.tela.mostra_aviso("Selecione uma linha para excluir.")
      else:
        self.controladorPessoa.exclui_registro(id_row=selected_row)
    
    if tab_ativa == 4: # Posto
      self.controladorPosto.tela.mostra_aviso("Não é permitido excluir o registro do Posto.")

    self.fetch_data()
    
  def ativar_botoes(self):
    self.NovoBtn.setEnabled(True)
    self.EditarBtn.setEnabled(True)
    self.ExcluirBtn.setEnabled(True)

  def desativar_botoes(self):
    self.NovoBtn.setDisabled(True)
    self.EditarBtn.setDisabled(True)
    self.ExcluirBtn.setDisabled(True)

  def cria_tela(self, Cadastros) -> None:
    Cadastros.setObjectName("Cadastros")
    Cadastros.resize(800, 400)
    Cadastros.setMinimumSize(QtCore.QSize(600, 400))
    Cadastros.setMaximumSize(QtCore.QSize(800, 400))
    self.ContainerTabs = QtWidgets.QFrame(parent=Cadastros)
    self.ContainerTabs.setGeometry(QtCore.QRect(0, 0, 801, 401))
    self.ContainerTabs.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerTabs.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerTabs.setObjectName("ContainerTabs")
    self.tabWidget = QtWidgets.QTabWidget(parent=self.ContainerTabs)
    self.tabWidget.setGeometry(QtCore.QRect(11, 1, 781, 401))
    self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
    self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
    self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
    self.tabWidget.setMovable(True)
    self.tabWidget.setObjectName("tabWidget")
    self.Bombas = QtWidgets.QWidget()
    self.Bombas.setObjectName("Bombas")
    self.BombasTable = QtWidgets.QTableWidget(parent=self.Bombas)
    self.BombasTable.setGeometry(QtCore.QRect(20, 10, 731, 331))
    self.BombasTable.setShowGrid(False)
    self.BombasTable.setObjectName("BombasTable")
    self.BombasTable.setColumnCount(3)
    self.BombasTable.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.BombasTable.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.BombasTable.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.BombasTable.setHorizontalHeaderItem(2, item)
    self.BombasTable.horizontalHeader().setCascadingSectionResizes(False)
    self.BombasTable.horizontalHeader().setDefaultSectionSize(150)
    self.BombasTable.horizontalHeader().setStretchLastSection(True)
    self.BombasTable.verticalHeader().setHighlightSections(True)
    self.tabWidget.addTab(self.Bombas, "")
    self.Tanques = QtWidgets.QWidget()
    self.Tanques.setObjectName("Tanques")
    self.TanquesTable = QtWidgets.QTableWidget(parent=self.Tanques)
    self.TanquesTable.setGeometry(QtCore.QRect(20, 10, 731, 331))
    self.TanquesTable.setShowGrid(False)
    self.TanquesTable.setObjectName("TanquesTable")
    self.TanquesTable.setColumnCount(5)
    self.TanquesTable.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.TanquesTable.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.TanquesTable.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.TanquesTable.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.TanquesTable.setHorizontalHeaderItem(3, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.TanquesTable.setHorizontalHeaderItem(4, item)
    self.TanquesTable.horizontalHeader().setCascadingSectionResizes(False)
    self.TanquesTable.horizontalHeader().setDefaultSectionSize(136)
    self.TanquesTable.horizontalHeader().setMinimumSectionSize(15)
    self.TanquesTable.horizontalHeader().setStretchLastSection(True)
    self.TanquesTable.verticalHeader().setHighlightSections(True)
    self.tabWidget.addTab(self.Tanques, "")
    self.Tipos = QtWidgets.QWidget()
    self.Tipos.setObjectName("Tipos")
    self.TiposTable = QtWidgets.QTableWidget(parent=self.Tipos)
    self.TiposTable.setGeometry(QtCore.QRect(20, 10, 731, 331))
    self.TiposTable.setShowGrid(False)
    self.TiposTable.setObjectName("TiposTable")
    self.TiposTable.setColumnCount(2)
    self.TiposTable.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.TiposTable.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.TiposTable.setHorizontalHeaderItem(1, item)
    self.TiposTable.horizontalHeader().setDefaultSectionSize(165)
    self.TiposTable.horizontalHeader().setSortIndicatorShown(True)
    self.TiposTable.horizontalHeader().setStretchLastSection(True)
    self.tabWidget.addTab(self.Tipos, "")
    self.Pessoas = QtWidgets.QWidget()
    self.Pessoas.setObjectName("Pessoas")
    self.PessoasTable = QtWidgets.QTableWidget(parent=self.Pessoas)
    self.PessoasTable.setGeometry(QtCore.QRect(20, 10, 731, 331))
    self.PessoasTable.setShowGrid(False)
    self.PessoasTable.setObjectName("PessoasTable")
    self.PessoasTable.setColumnCount(7)
    self.PessoasTable.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.PessoasTable.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.PessoasTable.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.PessoasTable.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.PessoasTable.setHorizontalHeaderItem(3, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.PessoasTable.setHorizontalHeaderItem(4, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.PessoasTable.setHorizontalHeaderItem(5, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.PessoasTable.setHorizontalHeaderItem(6, item)
    self.PessoasTable.horizontalHeader().setDefaultSectionSize(90)
    self.PessoasTable.horizontalHeader().setStretchLastSection(True)
    self.tabWidget.addTab(self.Pessoas, "")
    self.Posto = QtWidgets.QWidget()
    self.Posto.setObjectName("Posto")
    self.PostoTable = QtWidgets.QTableWidget(parent=self.Posto)
    self.PostoTable.setGeometry(QtCore.QRect(20, 10, 731, 331))
    self.PostoTable.setShowGrid(False)
    self.PostoTable.setObjectName("PostoTable")
    self.PostoTable.setColumnCount(3)
    self.PostoTable.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.PostoTable.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.PostoTable.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.PostoTable.setHorizontalHeaderItem(2, item)
    self.PostoTable.horizontalHeader().setDefaultSectionSize(135)
    self.PostoTable.horizontalHeader().setSortIndicatorShown(True)
    self.PostoTable.horizontalHeader().setStretchLastSection(True)
    self.tabWidget.addTab(self.Posto, "")
    self.ContainerBotoes = QtWidgets.QFrame(parent=Cadastros)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 363, 801, 41))
    self.ContainerBotoes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerBotoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerBotoes.setObjectName("ContainerBotoes")
    self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ContainerBotoes)
    self.horizontalLayout_2.setObjectName("horizontalLayout_2")
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout_2.addItem(spacerItem)
    self.TelaInicial = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.TelaInicial.setIcon(icon)
    self.TelaInicial.setObjectName("TelaInicial")
    self.horizontalLayout_2.addWidget(self.TelaInicial)
    self.NovoBtn = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/new.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.NovoBtn.setIcon(icon1)
    self.NovoBtn.setObjectName("NovoBtn")
    self.horizontalLayout_2.addWidget(self.NovoBtn)
    self.AtualizarBtn = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/refresh.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.AtualizarBtn.setIcon(icon2)
    self.AtualizarBtn.setObjectName("AtualizarBtn")
    self.horizontalLayout_2.addWidget(self.AtualizarBtn)
    self.EditarBtn = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/edit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.EditarBtn.setIcon(icon3)
    self.EditarBtn.setObjectName("EditarBtn")
    self.horizontalLayout_2.addWidget(self.EditarBtn)
    self.ExcluirBtn = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/delete.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.ExcluirBtn.setIcon(icon4)
    self.ExcluirBtn.setObjectName("ExcluirBtn")
    self.horizontalLayout_2.addWidget(self.ExcluirBtn)
    spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout_2.addItem(spacerItem1)
    Cadastros.setWindowTitle("GasGuardian")
    self.BombasTable.setSortingEnabled(False)
    item = self.BombasTable.horizontalHeaderItem(0)
    item.setText("ID da Bomba")
    item = self.BombasTable.horizontalHeaderItem(1)
    item.setText("Auto-Abastecimento")
    item = self.BombasTable.horizontalHeaderItem(2)
    item.setText("Tipos de Combustível")
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bombas), "Bombas")
    self.TanquesTable.setSortingEnabled(False)
    item = self.TanquesTable.horizontalHeaderItem(0)
    item.setText("ID do Tanque")
    item = self.TanquesTable.horizontalHeaderItem(1)
    item.setText("Tipo de Combustível")
    item = self.TanquesTable.horizontalHeaderItem(2)
    item.setText("Volume Atual (L)")
    item = self.TanquesTable.horizontalHeaderItem(3)
    item.setText("Capacidade Máxima (L)")
    item = self.TanquesTable.horizontalHeaderItem(4)
    item.setText("Porcentagem do Alerta")
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tanques), "Tanques")
    self.TiposTable.setSortingEnabled(False)
    item = self.TiposTable.horizontalHeaderItem(0)
    item.setText("Nome")
    item = self.TiposTable.horizontalHeaderItem(1)
    item.setText("Preço (R$)")
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tipos), "Tipos")
    self.PessoasTable.setSortingEnabled(False)
    item = self.PessoasTable.horizontalHeaderItem(0)
    item.setText("Nome")
    item = self.PessoasTable.horizontalHeaderItem(1)
    item.setText("CPF")
    item = self.PessoasTable.horizontalHeaderItem(2)
    item.setText("Email")
    item = self.PessoasTable.horizontalHeaderItem(3)
    item.setText("Celular")
    item = self.PessoasTable.horizontalHeaderItem(4)
    item.setText("Login")
    item = self.PessoasTable.horizontalHeaderItem(5)
    item.setText("Senha")
    item = self.PessoasTable.horizontalHeaderItem(6)
    item.setText("Gestor")
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pessoas), "Pessoas")
    self.PostoTable.setSortingEnabled(False)
    item = self.PostoTable.horizontalHeaderItem(0)
    item.setText("Nome")
    item = self.PostoTable.horizontalHeaderItem(1)
    item.setText("Chave Pix")
    item = self.PostoTable.horizontalHeaderItem(2)
    item.setText("CNPJ")
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Posto), "Posto")
    self.TelaInicial.setText("Tela Inicial")
    self.NovoBtn.setText("Novo")
    self.AtualizarBtn.setText("Atualizar")
    self.EditarBtn.setText("Editar")
    self.ExcluirBtn.setText("Excluir")
    self.tabWidget.setCurrentIndex(0)
    QtCore.QMetaObject.connectSlotsByName(Cadastros)
    #
    self.buttons_list = self.ContainerBotoes.findChildren(QtWidgets.QPushButton)
    self.TelaInicial.clicked.connect(self.tela_inicial)
    self.NovoBtn.clicked.connect(lambda: self.abre_form("Novo"))
    self.EditarBtn.clicked.connect(lambda: self.abre_form("Editar"))
    self.ExcluirBtn.clicked.connect(self.excluir)
    self.AtualizarBtn.clicked.connect(self.fetch_data)
    self.TanquesTable.itemDoubleClicked.connect(lambda: self.abre_form("Editar"))
    self.PostoTable.itemDoubleClicked.connect(lambda: self.abre_form("Editar"))
    self.TiposTable.itemDoubleClicked.connect(lambda: self.abre_form("Editar"))
    self.BombasTable.itemDoubleClicked.connect(lambda: self.abre_form("Editar"))
    self.PessoasTable.itemDoubleClicked.connect(lambda: self.abre_form("Editar"))
    self.fetch_data()
