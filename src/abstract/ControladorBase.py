import json

class ControladorBase():
  def carrega_dados(self, entidade: str) -> list:
    with open(f"dados/{entidade}.json", 'r') as file:
      return json.load(file)

  def salva_dados(self, data: list, entidade: str) -> None:
    with open(f"dados/{entidade}.json", 'w') as file:
      json.dump(data, file)