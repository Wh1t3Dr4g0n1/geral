#Registro de Aluno
#crud de aluno

import crud1
import os

os.system("cls")

print("READ/CREATE/UPDATE/DELETE/EXEMPLO")

choice1 = input("o que deseja: ").lower()

if choice1 == "exemplo":
  os.system("cls")
  crud1.exemplo()

if choice1 == "read":
  os.system("cls")
  crud1.readcrud()
  #FAZER UM READ COM BD
elif choice1 == "create":
  os.system("cls")
  crud1.create()
  
  #FAZER UM CREATE COM BD
elif choice1 == "update":
  crud1.altertable()
  
  #FAZER UM UPDATE COM BD
elif choice1 == "delete":
  crud1.delete()
  #FAZER UM DELETE COM BD
else:
  print("senta e chora")
  


