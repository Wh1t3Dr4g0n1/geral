import func
import os

func.carregar()

while True:
    os.system("cls")
    print("Digite o numero do que deseja.")
    choice = int(input("1. Adicionar Tarefas.\n2. Lista Tarefas.\n3. Marcar Tarefa Como Concluída. \n4. Remover Tarefa.\n5. Sair..\nEscolha: "))
    if choice == 1:
      os.system("cls")
      func.add()
      input("Tarefa Adicionada!")
    elif choice == 2:
      os.system("cls")
      func.lista()
      input("voltar..")
    elif choice == 3:
      os.system("cls")
      func.conc()
      input("tarefa marcada como concluída..")
    elif choice == 4:
      os.system("cls")
      func.rem()
      input("tarefa removida..")
    elif choice == 5:
      os.system("cls")
      break