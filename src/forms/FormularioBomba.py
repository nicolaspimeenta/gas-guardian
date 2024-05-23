# UC006: Cadastrar, Visualizar, Editar e Excluir Bombas de Combustível

from src.abstract.FormBase import FormBase
from PyQt6 import QtCore, QtGui, QtWidgets

class FormularioBomba(FormBase):
  def __init__(self):
    super().__init__(entidade='bombas')
    self.tiposSelecionados = []
    self.cria_tela(self)

  def confirmar(self) -> None:
    bombas_data = self.carrega_dados(entidade='bombas')
    form_data = {
      'id_bomba': self.inputId.text().strip(),
      'is_auto_abastecimento': self.isAutoAbastecimento.isChecked(),
      'tipos_combustivel': [tipo['nome'] for tipo in self.tiposSelecionados]
    }
    if self.is_form_valido(form_data):
      if self.is_edit():
        bombas_data[self.id_row] = form_data
        self.salva_dados(bombas_data, entidade='bombas')
        self.hide()
      else:
        bombas_data.append(form_data)
        QtWidgets.QMessageBox.information(self, "Sucesso", "Uma nova Bomba foi cadastrada.",
        QtWidgets.QMessageBox.StandardButton.Ok)
        self.salva_dados(bombas_data, entidade='bombas')
        self.hide()

  def is_form_valido(self, form_data) -> bool:
    bombas_data = self.carrega_dados(entidade='bombas')
    if not (self.is_edit() and form_data['id_bomba'] == bombas_data[self.id_row]['id_bomba']):
      for bomba in bombas_data:
        if bomba['id_bomba'].lower() == form_data['id_bomba'].lower():
          self.mostra_aviso("Bomba já cadastrada.")
          return False
    
    if not form_data['id_bomba']:
      self.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False
    
    if not len(form_data['tipos_combustivel']):
      self.mostra_aviso("Selecione pelo menos um tipo de combustível.")
      return False
    
    return True
  
  def fill_form(self) -> None:
    bombas_data = self.carrega_dados(entidade='bombas')
    self.fill_table(data=self.carrega_dados(entidade='tipos-combustivel'), table=self.tableTipos)
    self.tiposSelecionados = []
    if self.is_edit():
      for tipo in self.carrega_dados(entidade='tipos-combustivel'):
        for tipo_bomba in bombas_data[self.id_row]['tipos_combustivel']:
          if tipo['nome'] == tipo_bomba:
            self.tiposSelecionados.append(tipo)
      self.inputId.setText(bombas_data[self.id_row]['id_bomba'])
      self.isAutoAbastecimento.setChecked(bool(bombas_data[self.id_row]['is_auto_abastecimento']))
      self.fill_table(
        data=self.tiposSelecionados,
        table=self.tableSelecionados
        )
    else:
      self.inputId.clear()
      self.isAutoAbastecimento.setChecked(False)
      self.tableSelecionados.setRowCount(0)


  def adicionar(self) -> None:
    tipos_data = self.carrega_dados(entidade='tipos-combustivel')
    selected_row = self.tableTipos.currentRow()

    if selected_row == -1:
      self.mostra_aviso("Nenhum tipo de combustível selecionado.")
      return

    if tipos_data[selected_row] in self.tiposSelecionados:
      self.mostra_aviso("Esse combustível já está na lista de selecionados.")
      return
    
    self.tiposSelecionados.append(tipos_data[selected_row])
    self.fill_table(self.tiposSelecionados, self.tableSelecionados)

  def remover(self) -> None:
    selected_row = self.tableSelecionados.currentRow()

    if selected_row == -1:
      self.mostra_aviso("Nenhum tipo de combustível selecionado.")
      return
    
    self.tiposSelecionados.remove(self.tiposSelecionados[selected_row])
    self.fill_table(self.tiposSelecionados, self.tableSelecionados)
  
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
    self.Cancelar = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/cancel.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Cancelar.setIcon(icon2)
    self.Cancelar.setObjectName("Cancelar")
    self.horizontalLayout.addWidget(self.Cancelar)
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    self.Confirmar = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/check.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.Confirmar.setIcon(icon3)
    self.Confirmar.setObjectName("Confirmar")
    self.horizontalLayout.addWidget(self.Confirmar)
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
    self.Cancelar.setText("Cancelar")
    self.Confirmar.setText("Confirmar")
    QtCore.QMetaObject.connectSlotsByName(FormularioBomba)
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.hide)
    self.adicionarBtn.clicked.connect(self.adicionar)
    self.removerBtn.clicked.connect(self.remover)
    self.tableTipos.itemDoubleClicked.connect(self.adicionar)
    self.tableSelecionados.itemDoubleClicked.connect(self.remover)
  
