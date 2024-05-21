from src.abstract.TelaBase import TelaBase
from PyQt6 import QtCore, QtGui, QtWidgets


class Cadastros(TelaBase):
  def __init__(self):
    super().__init__()
    self.abre_tela(self)

  def tela_inicial(self) -> None:
    # função chamada ao clicar botão "Tela Inicial"
    self.hide()
    from src.InicialGestor import InicialGestor
    self.inicialGestor = InicialGestor()
    self.inicialGestor.show()

  def abre_form(self, btn: str) -> None:
    # função chamada ao clicar botão "Novo, Editar"
    tab_ativa = self.tabWidget.currentIndex()

    if tab_ativa == 0: # Bombas
      return
    
    if tab_ativa == 1: # Tanques
      return
    
    if tab_ativa == 2: # Tipos
      selected_row = self.TiposTable.currentRow()
      if btn=='Editar' and selected_row == -1:
        self.mostra_aviso("Selecione uma linha para editar.")
        return
      from src.forms.FormTipos import FormTipos
      self.FormTipos = FormTipos(
        id_row=selected_row if btn=='Editar' else None,
        title=f"Editando Tipo ({selected_row+1})" if btn=='Editar' else "Novo Tipo"
        )
      self.FormTipos.show()

    if tab_ativa == 3: # Pessoas
      selected_row = self.PessoasTable.currentRow()
      if btn=='Editar' and selected_row == -1:
        self.mostra_aviso("Selecione uma linha para editar.")
        return
      from src.forms.FormPessoa import FormPessoa
      self.FormPessoa = FormPessoa(
        id_row=selected_row if btn=='Editar' else None,
        title=f"Editando Funcionário ({selected_row+1})" if btn=='Editar' else "Novo Funcionário"
        )
      self.FormPessoa.show()
    
    if tab_ativa == 4: # Usuários
      selected_row = self.UsuariosTable.currentRow()
      if btn=='Editar' and selected_row == -1:
        self.mostra_aviso("Selecione uma linha para editar.")
        return
      from src.forms.FormUsuario import FormUsuario
      self.FormUsuario = FormUsuario(
        id_row=selected_row if btn=='Editar' else None,
        title=f"Editando Usuário ({selected_row+1})" if btn=='Editar' else "Novo Usuário"
        )
      self.FormUsuario.show()
    
    if tab_ativa == 5: # Posto
      if btn=='Novo':
        self.mostra_aviso("Não é permitido criar um registro de Posto.")
        return
      from src.forms.FormPosto import FormPosto
      self.FormPosto = FormPosto()
      self.FormPosto.show()
      
  def fetch_data(self) -> None:
    self.fill_table_from_json("pessoas", self.PessoasTable)
    self.fill_table_from_json("usuarios", self.UsuariosTable)
    self.fill_table_from_json("tipos-combustivel", self.TiposTable)
    self.fill_table_from_json("posto", self.PostoTable)
    
  def excluir(self) -> None:
    # função chamada ao clicar botão "Excluir"
    tab_ativa = self.tabWidget.currentIndex()

    if tab_ativa == 0: # Bombas
      return
    
    if tab_ativa == 1: # Tanques
      return
    
    if tab_ativa == 2: # Tipos
      selected_row = self.TiposTable.currentRow()
      if selected_row == -1:
        self.mostra_aviso("Selecione uma linha para excluir.")
      else:
        self.exclui_linha(entidade="tipos-combustivel", id=selected_row)
    
    if tab_ativa == 3: # Pessoas
      selected_row = self.PessoasTable.currentRow()
      if selected_row == -1:
        self.mostra_aviso("Selecione uma linha para excluir.")
      else:
        self.exclui_linha(entidade="pessoas", id=selected_row)
    
    if tab_ativa == 4: # Usuários
      selected_row = self.UsuariosTable.currentRow()
      if selected_row == -1: 
        self.mostra_aviso("Selecione uma linha para excluir.")
      else:
        self.exclui_user_id(id=selected_row)
        self.exclui_linha(entidade="usuarios", id=selected_row)
    
    if tab_ativa == 5: # Posto
      self.mostra_aviso("Não é permitido excluir o registro do Posto.")
    
  def exclui_linha(self, entidade, id) -> None:
    data = self.carrega_dados(entidade)
    del data[id]
    self.salva_dados(data, entidade)
    QtWidgets.QMessageBox.critical(self, "Aviso", f"A linha {id+1} foi excluída",
    QtWidgets.QMessageBox.StandardButton.Ok)
    self.fetch_data()

  def exclui_user_id(self, id) -> None:
    usuarios_data = self.carrega_dados('usuarios')
    pessoas_data = self.carrega_dados('pessoas')
    for pessoa in pessoas_data:
      if pessoa['user_id'] == usuarios_data[id]['login']:
        pessoa['user_id'] = ''
    self.salva_dados(pessoas_data, 'pessoas')

  def fill_table_from_json(self, entidade, table) -> None:
    data = self.carrega_dados(entidade)
    if data:
      table.setRowCount(0)
      table.setRowCount(len(data))
      for row, info in enumerate(data):
        info_list = info.values()
        for column, item in enumerate(info_list):
          cell_item = QtWidgets.QTableWidgetItem(str(item))
          table.setItem(row, column, cell_item)
    else:
      table.setRowCount(0)

  def abre_tela(self, Cadastros) -> None:
    Cadastros.setObjectName("Cadastros")
    Cadastros.resize(600, 400)
    Cadastros.setMinimumSize(QtCore.QSize(600, 400))
    Cadastros.setMaximumSize(QtCore.QSize(600, 400))
    self.ContainerTabs = QtWidgets.QFrame(parent=Cadastros)
    self.ContainerTabs.setGeometry(QtCore.QRect(0, 0, 600, 401))
    self.ContainerTabs.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerTabs.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerTabs.setObjectName("ContainerTabs")
    self.tabWidget = QtWidgets.QTabWidget(parent=self.ContainerTabs)
    self.tabWidget.setGeometry(QtCore.QRect(11, 1, 581, 401))
    self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
    self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
    self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
    self.tabWidget.setMovable(True)
    self.tabWidget.setObjectName("tabWidget")
    self.Bombas = QtWidgets.QWidget()
    self.Bombas.setObjectName("Bombas")
    self.TableBombas = QtWidgets.QTableWidget(parent=self.Bombas)
    self.TableBombas.setGeometry(QtCore.QRect(20, 10, 541, 331))
    self.TableBombas.setShowGrid(False)
    self.TableBombas.setObjectName("TableBombas")
    self.TableBombas.setColumnCount(3)
    self.TableBombas.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.TableBombas.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.TableBombas.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.TableBombas.setHorizontalHeaderItem(2, item)
    self.TableBombas.horizontalHeader().setCascadingSectionResizes(False)
    self.TableBombas.horizontalHeader().setDefaultSectionSize(150)
    self.TableBombas.horizontalHeader().setStretchLastSection(True)
    self.TableBombas.verticalHeader().setHighlightSections(True)
    self.tabWidget.addTab(self.Bombas, "")
    self.Tanques = QtWidgets.QWidget()
    self.Tanques.setObjectName("Tanques")
    self.TanquesTable = QtWidgets.QTableWidget(parent=self.Tanques)
    self.TanquesTable.setGeometry(QtCore.QRect(20, 10, 541, 331))
    self.TanquesTable.setShowGrid(False)
    self.TanquesTable.setObjectName("TanquesTable")
    self.TanquesTable.setColumnCount(4)
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
    self.TanquesTable.horizontalHeader().setCascadingSectionResizes(False)
    self.TanquesTable.horizontalHeader().setDefaultSectionSize(122)
    self.TanquesTable.horizontalHeader().setMinimumSectionSize(15)
    self.TanquesTable.horizontalHeader().setStretchLastSection(True)
    self.TanquesTable.verticalHeader().setHighlightSections(True)
    self.tabWidget.addTab(self.Tanques, "")
    self.Tipos = QtWidgets.QWidget()
    self.Tipos.setObjectName("Tipos")
    self.TiposTable = QtWidgets.QTableWidget(parent=self.Tipos)
    self.TiposTable.setGeometry(QtCore.QRect(20, 10, 541, 331))
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
    self.PessoasTable.setGeometry(QtCore.QRect(20, 10, 541, 331))
    self.PessoasTable.setShowGrid(False)
    self.PessoasTable.setObjectName("PessoasTable")
    self.PessoasTable.setColumnCount(6)
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
    self.PessoasTable.horizontalHeader().setDefaultSectionSize(90)
    self.PessoasTable.horizontalHeader().setStretchLastSection(True)
    self.tabWidget.addTab(self.Pessoas, "")
    self.Usuarios = QtWidgets.QWidget()
    self.Usuarios.setObjectName("Usuarios")
    self.UsuariosTable = QtWidgets.QTableWidget(parent=self.Usuarios)
    self.UsuariosTable.setGeometry(QtCore.QRect(20, 10, 541, 331))
    self.UsuariosTable.setShowGrid(False)
    self.UsuariosTable.setObjectName("UsuariosTable")
    self.UsuariosTable.setColumnCount(2)
    self.UsuariosTable.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.UsuariosTable.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
    self.UsuariosTable.setHorizontalHeaderItem(1, item)
    self.UsuariosTable.horizontalHeader().setDefaultSectionSize(135)
    self.UsuariosTable.horizontalHeader().setSortIndicatorShown(True)
    self.UsuariosTable.horizontalHeader().setStretchLastSection(True)
    self.tabWidget.addTab(self.Usuarios, "")
    self.Posto = QtWidgets.QWidget()
    self.Posto.setObjectName("Posto")
    self.PostoTable = QtWidgets.QTableWidget(parent=self.Posto)
    self.PostoTable.setGeometry(QtCore.QRect(20, 10, 541, 331))
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
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 363, 601, 41))
    self.ContainerBotoes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerBotoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerBotoes.setObjectName("ContainerBotoes")
    self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ContainerBotoes)
    self.horizontalLayout_2.setObjectName("horizontalLayout_2")
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout_2.addItem(spacerItem)
    self.TelaInicial = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.TelaInicial.setIcon(icon)
    self.TelaInicial.setObjectName("TelaInicial")
    self.horizontalLayout_2.addWidget(self.TelaInicial)
    self.Novo = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/new.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Novo.setIcon(icon1)
    self.Novo.setObjectName("Novo")
    self.horizontalLayout_2.addWidget(self.Novo)
    self.Atualizar = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/refresh.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Atualizar.setIcon(icon2)
    self.Atualizar.setObjectName("Atualizar")
    self.horizontalLayout_2.addWidget(self.Atualizar)
    self.Editar = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/edit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Editar.setIcon(icon3)
    self.Editar.setObjectName("Editar")
    self.horizontalLayout_2.addWidget(self.Editar)
    self.Excluir = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap(".\\telas\\ui\\../../assets/delete.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Excluir.setIcon(icon4)
    self.Excluir.setObjectName("Excluir")
    self.horizontalLayout_2.addWidget(self.Excluir)
    spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout_2.addItem(spacerItem1)
    _translate = QtCore.QCoreApplication.translate
    Cadastros.setWindowTitle(_translate("Cadastros", "GasGuardian"))
    self.TableBombas.setSortingEnabled(False)
    item = self.TableBombas.horizontalHeaderItem(0)
    item.setText(_translate("Cadastros", "Ativa"))
    item = self.TableBombas.horizontalHeaderItem(1)
    item.setText(_translate("Cadastros", "Auto-Abastecimento"))
    item = self.TableBombas.horizontalHeaderItem(2)
    item.setText(_translate("Cadastros", "Tipos de Combustível"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bombas), _translate("Cadastros", "Bombas"))
    self.TanquesTable.setSortingEnabled(False)
    item = self.TanquesTable.horizontalHeaderItem(0)
    item.setText(_translate("Cadastros", "Tipo de Combustível"))
    item = self.TanquesTable.horizontalHeaderItem(1)
    item.setText(_translate("Cadastros", "Volume Atual"))
    item = self.TanquesTable.horizontalHeaderItem(2)
    item.setText(_translate("Cadastros", "Capacidade Máxima"))
    item = self.TanquesTable.horizontalHeaderItem(3)
    item.setText(_translate("Cadastros", "Porcentagem do Alerta"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tanques), _translate("Cadastros", "Tanques"))
    self.TiposTable.setSortingEnabled(False)
    item = self.TiposTable.horizontalHeaderItem(0)
    item.setText(_translate("Cadastros", "Nome"))
    item = self.TiposTable.horizontalHeaderItem(1)
    item.setText(_translate("Cadastros", "Preço"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tipos), _translate("Cadastros", "Tipos"))
    self.PessoasTable.setSortingEnabled(False)
    item = self.PessoasTable.horizontalHeaderItem(0)
    item.setText(_translate("Cadastros", "Nome"))
    item = self.PessoasTable.horizontalHeaderItem(1)
    item.setText(_translate("Cadastros", "CPF"))
    item = self.PessoasTable.horizontalHeaderItem(2)
    item.setText(_translate("Cadastros", "Email"))
    item = self.PessoasTable.horizontalHeaderItem(3)
    item.setText(_translate("Cadastros", "Celular"))
    item = self.PessoasTable.horizontalHeaderItem(4)
    item.setText(_translate("Cadastros", "Usuário"))
    item = self.PessoasTable.horizontalHeaderItem(5)
    item.setText(_translate("Cadastros", "Gestor"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pessoas), _translate("Cadastros", "Funcionários"))
    self.UsuariosTable.setSortingEnabled(False)
    item = self.UsuariosTable.horizontalHeaderItem(0)
    item.setText(_translate("Cadastros", "Login"))
    item = self.UsuariosTable.horizontalHeaderItem(1)
    item.setText(_translate("Cadastros", "Senha"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Usuarios), _translate("Cadastros", "Usuários"))
    self.PostoTable.setSortingEnabled(False)
    item = self.PostoTable.horizontalHeaderItem(0)
    item.setText(_translate("Cadastros", "Nome"))
    item = self.PostoTable.horizontalHeaderItem(1)
    item.setText(_translate("Cadastros", "Chave Pix"))
    item = self.PostoTable.horizontalHeaderItem(2)
    item.setText(_translate("Cadastros", "CNPJ"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Posto), _translate("Cadastros", "Posto"))
    self.TelaInicial.setText(_translate("Cadastros", "Tela Inicial"))
    self.Novo.setText(_translate("Cadastros", "Novo"))
    self.Atualizar.setText(_translate("Cadastros", "Atualizar"))
    self.Editar.setText(_translate("Cadastros", "Editar"))
    self.Excluir.setText(_translate("Cadastros", "Excluir"))
    self.tabWidget.setCurrentIndex(0)
    QtCore.QMetaObject.connectSlotsByName(Cadastros)
    self.buttons_list = self.ContainerBotoes.findChildren(QtWidgets.QPushButton)
    self.TelaInicial.clicked.connect(self.tela_inicial)
    self.Novo.clicked.connect(lambda: self.abre_form("Novo"))
    self.Editar.clicked.connect(lambda: self.abre_form("Editar"))
    self.Excluir.clicked.connect(self.excluir)
    self.Atualizar.clicked.connect(self.fetch_data)
    self.fetch_data()
