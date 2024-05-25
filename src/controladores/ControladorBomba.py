# UC006: Cadastrar, Visualizar, Editar e Excluir Bombas de Combustível


from src.abstract.ControladorBase import ControladorBase
from src.telas.TelaBomba import TelaBomba
from src.entidades.Bomba import Bomba

class ControladorBomba(ControladorBase):
  def __init__(self):
    super().__init__(tela=TelaBomba, entidade='bombas')
    self.tiposSelecionados = []

  def confirmar(self) -> None:
    bombas_data = self.carrega_dados()
    form_data = {
      'id_bomba': self.tela.inputId.text().strip(),
      'is_auto_abastecimento': self.tela.isAutoAbastecimento.isChecked(),
      'tipos_combustivel': [tipo['nome'] for tipo in self.tiposSelecionados]
    }
    if self.is_form_valido(form_data):
      bomba_dto = Bomba(
        id_bomba=form_data['id_bomba'],
        is_auto_abastecimento=form_data['is_auto_abastecimento'],
        tipos_combustivel=form_data['tipos_combustivel']
      )
      if self.is_edit():
        bombas_data[self.id_row] = bomba_dto.transforma_para_dict()
        self.salva_dados(bombas_data)
        self.tela.hide()
      else:
        bombas_data.append(bomba_dto.transforma_para_dict())
        self.tela.mostra_mensagem('Uma nova Bomba foi cadastrada.')
        self.salva_dados(bombas_data)
        self.tela.hide()

  def is_form_valido(self, form_data: dict) -> bool:
    bombas_data = self.carrega_dados()
    if not (self.is_edit() and form_data['id_bomba'] == bombas_data[self.id_row]['id_bomba']):
      for bomba in bombas_data:
        if bomba['id_bomba'].lower() == form_data['id_bomba'].lower():
          self.tela.mostra_aviso("Bomba já cadastrada.")
          return False
    
    if not form_data['id_bomba']:
      self.tela.mostra_aviso("Preencha todos os campos obrigatórios.")
      return False
    
    if not len(form_data['tipos_combustivel']):
      self.tela.mostra_aviso("Selecione pelo menos um tipo de combustível.")
      return False
    
    return True
  
  def fill_form(self) -> None:
    bombas_data = self.carrega_dados()
    self.tela.fill_table(data=self.carrega_dados(entidade='tipos-combustivel'), table=self.tela.tableTipos)
    self.tiposSelecionados = []
    if self.is_edit():
      for tipo in self.carrega_dados(entidade='tipos-combustivel'):
        for tipo_bomba in bombas_data[self.id_row]['tipos_combustivel']:
          if tipo['nome'] == tipo_bomba:
            self.tiposSelecionados.append(tipo)
      self.tela.inputId.setText(bombas_data[self.id_row]['id_bomba'])
      self.tela.isAutoAbastecimento.setChecked(bool(bombas_data[self.id_row]['is_auto_abastecimento']))
      self.tela.fill_table(data=self.tiposSelecionados, table=self.tela.tableSelecionados)
    else:
      self.tela.inputId.clear()
      self.tela.isAutoAbastecimento.setChecked(False)
      self.tela.tableSelecionados.setRowCount(0)

  def adicionar(self) -> None:
    tipos_data = self.carrega_dados(entidade='tipos-combustivel')
    selected_row = self.tela.tableTipos.currentRow()

    if selected_row == -1:
      self.tela.mostra_aviso("Nenhum tipo de combustível selecionado.")
      return

    if tipos_data[selected_row] in self.tiposSelecionados:
      self.tela.mostra_aviso("Esse combustível já está na lista de selecionados.")
      return
    
    self.tiposSelecionados.append(tipos_data[selected_row])
    self.tela.fill_table(self.tiposSelecionados, self.tela.tableSelecionados)

  def remover(self) -> None:
    selected_row = self.tela.tableSelecionados.currentRow()

    if selected_row == -1:
      self.tela.mostra_aviso("Nenhum tipo de combustível selecionado.")
      return
    
    self.tiposSelecionados.remove(self.tiposSelecionados[selected_row])
    self.tela.fill_table(self.tiposSelecionados, self.tela.tableSelecionados)

  def atualiza_tipos(self, antigo_nome: str, novo_nome: str):
    bombas_data = self.carrega_dados()
    for bomba in bombas_data:
      if antigo_nome in bomba['tipos_combustivel']:
        bomba['tipos_combustivel'] = [novo_nome if x == antigo_nome else x for x in bombas_data]

    self.salva_dados(bombas_data)

  def conecta_controlador_tela(self) -> None:
    self.tela.confirmarBtn.clicked.connect(self.confirmar)
    self.tela.cancelarBtn.clicked.connect(self.tela.hide)
    self.tela.adicionarBtn.clicked.connect(self.adicionar)
    self.tela.removerBtn.clicked.connect(self.remover)
    self.tela.tableTipos.itemDoubleClicked.connect(self.adicionar)
    self.tela.tableSelecionados.itemDoubleClicked.connect(self.remover)
  
