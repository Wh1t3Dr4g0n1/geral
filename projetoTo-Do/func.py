import json, os
from pathlib import Path

arq_json = "tarefas.json"
path_json = Path(__file__).parent
caminho_pasta = path_json / arq_json

tarefas = []

def add():
  nome = input("Digite a tarefa: ")
  tarefa = {
    "Nome": nome,
    "Feito": False
    }
  tarefas.append(tarefa)
  salvar()

  
def lista():
  print("Tarefas:")
  for i, tarefa in enumerate(tarefas):
    status = "X" if tarefa["Feito"] else " "
    print(f"{i+1}, [{status}] {tarefa['Nome']}")   
  if not tarefas:
    print("Sem tarefas.")

def conc():
  lista()
  numero = int(input("Numero da tarefa: "))
  tarefas[numero - 1]["Feito"] = True
  os.system("cls")
  lista()
  salvar()
  
def rem():
  lista()
  numero = int(input("Qual numero da tarefa: "))
  tarefas.pop(numero - 1)
  salvar()
      
def salvar():
  with open(caminho_pasta, "w") as arquivo:
    json.dump(tarefas, arquivo, indent=4)
    
def carregar():
  global tarefas
  
  try: 
    with open(caminho_pasta, "r") as arquivo:
      tarefas = json.load(arquivo)
      
  except FileNotFoundError:
    tarefas = []