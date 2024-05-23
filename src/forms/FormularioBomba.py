# UC006: Cadastrar, Visualizar, Editar e Excluir Bombas de Combustível

from src.abstract.AbstractForm import AbstractForm
from PyQt6 import QtCore, QtGui, QtWidgets
from src.componentes.EscolherRegistros import EscolherRegistrosComponent

class FormularioBomba(AbstractForm):
  def __init__(self):
    super().__init__(entidade='bombas')
    self.cria_tela(self)
    self.escolherTiposComponent = EscolherRegistrosComponent(entidade='tipos-combustivel')

  def confirmar(self) -> None:
    bombas_data = self.carrega_dados(entidade='bombas')
    form_data = {
      'id_bomba': self.inputId.text().strip(),
      'is_auto_abastecimento': self.isAutoAbastecimento.isChecked(),
      'tipos_combustivel': self.mapTiposSelecionados(self.escolherTiposComponent.selecionados)
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
    if self.is_edit():
      self.inputId.setText(bombas_data[self.id_row]['id_bomba'])
      self.isAutoAbastecimento.setChecked(bool(bombas_data[self.id_row]['is_auto_abastecimento']))
    else:
      self.inputId.clear()
      self.isAutoAbastecimento.setChecked(False)

  def escolherTipo(self) -> None:
    bombas_data = self.carrega_dados(entidade='bombas')
    if self.is_edit():
      self.escolherTiposComponent.open(selecionados_data=bombas_data[self.id_row]['tipos_combustivel'])
    else:
      self.escolherTiposComponent.open(selecionados_data=None)

  def mapTiposSelecionados(self, tiposSelecionados: list) -> None:
    tipos_mapeados = []
    for tipo in tiposSelecionados:
      tipos_mapeados.append(tipo['nome'])
    return tipos_mapeados
  
  def cria_tela(self, FormularioBomba) -> None:
    FormularioBomba.setObjectName("FormularioBomba")
    FormularioBomba.resize(401, 142)
    self.ContainerForm = QtWidgets.QFrame(parent=FormularioBomba)
    self.ContainerForm.setGeometry(QtCore.QRect(0, 0, 401, 141))
    self.ContainerForm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerForm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerForm.setObjectName("ContainerForm")
    self.formLayout = QtWidgets.QFormLayout(self.ContainerForm)
    self.formLayout.setObjectName("formLayout")
    self.label = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
    self.label.setSizePolicy(sizePolicy)
    self.label.setObjectName("label")
    self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
    self.inputId = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputId.sizePolicy().hasHeightForWidth())
    self.inputId.setSizePolicy(sizePolicy)
    self.inputId.setObjectName("inputId")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputId)
    self.escolherTipoBtn = QtWidgets.QPushButton(parent=self.ContainerForm)
    self.escolherTipoBtn.setObjectName("escolherTipoBtn")
    self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.escolherTipoBtn)
    self.isAutoAbastecimento = QtWidgets.QCheckBox(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.isAutoAbastecimento.sizePolicy().hasHeightForWidth())
    self.isAutoAbastecimento.setSizePolicy(sizePolicy)
    self.isAutoAbastecimento.setObjectName("isAutoAbastecimento")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.isAutoAbastecimento)
    self.ContainerBotoes = QtWidgets.QFrame(parent=FormularioBomba)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 100, 401, 41))
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
    FormularioBomba.setWindowTitle("Nova Pessoa")
    self.label.setText("ID da Bomba *")
    self.escolherTipoBtn.setText("Escolher Tipos de Combustível da Bomba")
    self.isAutoAbastecimento.setText("Auto-abastecimento")
    self.Cancelar.setText("Cancelar")
    self.Confirmar.setText("Confirmar")
    QtCore.QMetaObject.connectSlotsByName(FormularioBomba)
    self.Confirmar.clicked.connect(self.confirmar)
    self.Cancelar.clicked.connect(self.hide)
    self.escolherTipoBtn.clicked.connect(self.escolherTipo)
  
