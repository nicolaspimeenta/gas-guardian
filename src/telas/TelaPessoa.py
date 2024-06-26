# UC001: Cadastrar, Visualizar, Editar e Excluir Usuários


from src.abstract.TelaBase import TelaBase
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QLineEdit, QPushButton, QCheckBox

class TelaPessoa(TelaBase):
  def __init__(self):
    super().__init__()
    self.inputNome = QLineEdit()
    self.inputCpf = QLineEdit()
    self.inputCelular = QLineEdit()
    self.inputEmail = QLineEdit()
    self.inputLogin = QLineEdit()
    self.inputSenha = QLineEdit()
    self.isGestor = QCheckBox()
    self.confirmarBtn = QPushButton()
    self.cancelarBtn = QPushButton()
    self.cria_tela(self)

  def cria_tela(self, FormularioPessoa) -> None:
    FormularioPessoa.setObjectName("FormularioPessoa")
    FormularioPessoa.resize(300, 217)
    self.ContainerForm = QtWidgets.QFrame(parent=FormularioPessoa)
    self.ContainerForm.setGeometry(QtCore.QRect(0, 0, 301, 201))
    self.ContainerForm.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerForm.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerForm.setObjectName("ContainerForm")
    self.formLayout = QtWidgets.QFormLayout(self.ContainerForm)
    self.formLayout.setObjectName("formLayout")
    self.inputNome = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputNome.sizePolicy().hasHeightForWidth())
    self.inputNome.setSizePolicy(sizePolicy)
    self.inputNome.setObjectName("InputNome")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputNome)
    self.inputCpf = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputCpf.sizePolicy().hasHeightForWidth())
    self.inputCpf.setSizePolicy(sizePolicy)
    self.inputCpf.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.inputCpf.setObjectName("InputCpf")
    self.inputCpf.setInputMask("000.000.000-00")
    self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputCpf)
    self.label_4 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_4.setObjectName("label_4")
    self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
    self.inputCelular = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputCelular.sizePolicy().hasHeightForWidth())
    self.inputCelular.setSizePolicy(sizePolicy)
    self.inputCelular.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.inputCelular.setObjectName("InputCelular")
    self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputCelular)
    self.inputEmail = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputEmail.sizePolicy().hasHeightForWidth())
    self.inputEmail.setSizePolicy(sizePolicy)
    self.inputEmail.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.inputEmail.setObjectName("InputEmail")
    self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputEmail)
    self.label_3 = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
    self.label_3.setSizePolicy(sizePolicy)
    self.label_3.setObjectName("label_3")
    self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_3)
    self.label_2 = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
    self.label_2.setSizePolicy(sizePolicy)
    self.label_2.setObjectName("label_2")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_2)
    self.label = QtWidgets.QLabel(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
    self.label.setSizePolicy(sizePolicy)
    self.label.setObjectName("label")
    self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
    self.label_5 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_5.setObjectName("label_5")
    self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
    self.inputSenha = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputSenha.sizePolicy().hasHeightForWidth())
    self.inputSenha.setSizePolicy(sizePolicy)
    self.inputSenha.setInputMask("")
    self.inputSenha.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
    self.inputSenha.setObjectName("inputSenha")
    self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputSenha)
    self.label_6 = QtWidgets.QLabel(parent=self.ContainerForm)
    self.label_6.setObjectName("label_6")
    self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_6)
    self.inputLogin = QtWidgets.QLineEdit(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.inputLogin.sizePolicy().hasHeightForWidth())
    self.inputLogin.setSizePolicy(sizePolicy)
    self.inputLogin.setInputMask("")
    self.inputLogin.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    self.inputLogin.setObjectName("inputLogin")
    self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.inputLogin)
    self.isGestor = QtWidgets.QCheckBox(parent=self.ContainerForm)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.isGestor.sizePolicy().hasHeightForWidth())
    self.isGestor.setSizePolicy(sizePolicy)
    self.isGestor.setObjectName("Gestor")
    self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.isGestor)
    self.ContainerBotoes = QtWidgets.QFrame(parent=FormularioPessoa)
    self.ContainerBotoes.setGeometry(QtCore.QRect(0, 180, 301, 44))
    self.ContainerBotoes.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.ContainerBotoes.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.ContainerBotoes.setObjectName("ContainerBotoes")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.ContainerBotoes)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.cancelarBtn = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/cancel.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.cancelarBtn.setIcon(icon)
    self.cancelarBtn.setObjectName("Cancelar")
    self.horizontalLayout.addWidget(self.cancelarBtn)
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    self.confirmarBtn = QtWidgets.QPushButton(parent=self.ContainerBotoes)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../assets/check.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.confirmarBtn.setIcon(icon1)
    self.confirmarBtn.setObjectName("Confirmar")
    self.horizontalLayout.addWidget(self.confirmarBtn)
    self.label_4.setText("Celular")
    self.inputCelular.setInputMask("(00) 00000-0000")
    self.label_3.setText("Email")
    self.label_2.setText("CPF *")
    self.label.setText("Nome *")
    self.label_5.setText("Login *")
    self.label_6.setText("Senha *")
    self.isGestor.setText("Gestor")
    self.cancelarBtn.setText("Cancelar")
    self.confirmarBtn.setText("Confirmar")
    QtCore.QMetaObject.connectSlotsByName(FormularioPessoa)