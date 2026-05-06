import mysql.connector
import os

def get_connection(): # PREENCHA COM AS INFORMAÇÕES DO SEU BANCO DE DADOS
  return mysql.connector.connect(
  host = " ",  
  user = " ",  #USER
  password = " ",  #PASSWORD
  database = " ",  #DATABASE
)
    
def create():
  objeto = input("De qual tabela: ").lower()
  os.system("cls")
     
  if objeto == "professor":
    sg = "pro"
  elif objeto == "aluno":
    sg = "aluno"
  else:
    print("coloque algo válido")
    
  iden = int(input("Coloque o ID: "))
  nm = input("Coloque o Nome: ")
  cpf = input("Coloque o CPF: ")
  tl = input("Coloque o Telefone: ")
  ende = input("Coloque o Endereço: ")
  os.system("cls")
  print(f"CONFIRA AS INFORMAÇÕES!\nID: {iden}\nNome: {nm}\nCPF: {cpf}\nTelefone: {tl}\nEndereço: {ende}")
  confirmar = input("Deseja confirmar?(S/N): ").lower()
  if confirmar == "s":
    conexao = get_connection()
    cursor = conexao.cursor()
    insert = f"INSERT INTO {objeto} (id_{sg}, nm_{sg}, cpf_{sg}, tl_{sg}, ende_{sg}) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert, (iden, nm, cpf, tl, ende))
    conexao.commit()
    print("CRIADO COM SUCESSO!")
    
    cursor.close()
    conexao.close()
  
def readcrud():
     objeto = input("De qual tabela: ").lower()
     os.system("cls")
     
     if objeto == "professor":
       id_sg = "id_pro"
     elif objeto == "aluno":
       id_sg = "id_aluno"
  
  
     escolhaid = input("De qual ID: ")
     conexao = get_connection()
     cursor = conexao.cursor()
     exemploe = f"SELECT * FROM {objeto} WHERE {id_sg} = (%s)"
     cursor.execute(exemploe, (escolhaid,))
     select = cursor.fetchone()
     conexao.commit()
     print(f"{objeto}: {select}")
     
     cursor.close()
     conexao.close()
     

def altertable():
     objeto = input("De qual tabela: ").lower()
     os.system("cls")
     
     if objeto == "professor":
      sg = "pro"
      id_sg = "id_pro"
     elif objeto == "aluno":
       sg = "aluno"
       id_sg = "id_aluno"
    
     pr = f"Colunas: (id_{sg}/nm_{sg}/cpf_{sg}/tl_{sg}/ende_{sg})"
     print(pr)
     coluna1 = input("Qual coluna deseja alterar: ")
     escolhaid = input("De qual ID: ")
     conexao = get_connection()
     cursor = conexao.cursor()
     escolha2 = input("O que deseja inserir: ")
     exemploe = f"UPDATE {objeto} SET {coluna1} = (%s) WHERE {id_sg} = (%s)"
     cursor.execute(exemploe, (escolha2,  escolhaid))
     conexao.commit()
     print("Concluido com sucesso!")
     
     cursor.close()
     conexao.close()

     
def delete():
    os.system("cls")
    objeto = input("De qual tabela: ").lower()
    if objeto == "professor":
      id_sg = "id_pro"
    elif objeto == "aluno":
       id_sg = "id_aluno"
    else:
      print("coloque algo válido")
      
    os.system("cls")
    escolhaid = input("Qual id do objeto que deseja excluir: ")
    conexao = get_connection()
    cursor = conexao.cursor()
    delob= f"DELETE FROM {objeto} aluno WHERE {id_sg} = (%s)"
    cursor.execute(delob, (escolhaid,))
    conexao.commit()
    print("Concluido com sucesso!")
     
    cursor.close()
    conexao.close()
    
def exemplo():
     objeto = input("De qual tabela: ").lower()
     os.system("cls")
     
     if objeto == "professor":
      sg = "pro"
      id_sg = "id_pro"
     elif objeto == "aluno":
       sg = "aluno"
       id_sg = "id_aluno"
       
     pr = f"Colunas: (id_{sg}/nm_{sg}/cpf_{sg}/tl_{sg}/ende_{sg})"
     print(pr)
     coluna1 = input("Qual coluna deseja alterar: ")
     escolhaid = input("De qual ID: ")
     conexao = get_connection()
     cursor = conexao.cursor()
     escolha2 = input("O que deseja inserir: ")
     exemploe = f"UPDATE {objeto} SET {coluna1} = (%s) WHERE {id_sg} = (%s)"
     cursor.execute(exemploe, (escolha2,  escolhaid))
     conexao.commit()
     print("Concluido com sucesso!")
     
     cursor.close()
     conexao.close()
  