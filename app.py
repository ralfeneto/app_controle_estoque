listaPecas = []
# ----------- Começo cadastra peca -----------
def cadastrarPeca(codigoId):
     print("Bem-vindo ao cadastro de peças ")
     print("O Codigo da peça a ser Cadastrada é: {}".format(codigoId))
     nome = input("Digite o nome da peça: \n")
     fabricante = input("Digite o fabricante da peça: \n")
     valor = input("Digite o valor da peça: \n")
     dicionarioPeca = {"codigoId": codigoId, "nome": nome,"fabricante": fabricante, "valor": valor}
# importante passa o (), pelo copy ser um atributo
     listaPecas.append(dicionarioPeca.copy())
# ----------- Começo consulta peca -----------
def consultarPeca():
 while True:
    try:
      print("Bem-vindo ao consulta de peças ")
      opConsultar = int(input("Entre com a opção desejada:\n1- Consultar Todas Peças\n2- Consulta peça por Codigo\n3- Consultar peça por Fabricante\n4- Retornar\n>>"))
      if opConsultar == 1:
        print("Bem vindo consultar todos")
        for pecas in listaPecas: # selecionar cada dicionario
            for key, value in pecas.items(): # selecionar cada campo do dicionario
              print("{} : {}".format(key, value))
      elif opConsultar == 2:
        print("Consulta por Codigo")
        entrada = int(input("Digite o Codigo desejado: \n"))
        for pecas in listaPecas:
          if(pecas['codigoId'] == entrada):
                  for key, value in pecas.items():
                    print("{} : {}".format(key, value))
          elif opConsultar == 3:
            print("Consulta por Fabricante")
            entrada = input("Digite o Fabricante desejado: \n")
        for pecas in listaPecas:
         if(pecas['fabricante'] == entrada):
            for key, value in pecas.items():
              print("{} : {}".format(key, value))
         elif opConsultar == 4:
            break
         else:
          print("Pare de digitar números invalidos")
    except ValueError:
         print("Pare de Digitar valores não inteiros")
# ----------- Começo remove peca -----------
def removerPeca():
  print("Remover por codigo")
  entrada = int(input("Digite o codigo do produto a excluir: \n"))
  for pecas in listaPecas:
    if(pecas['codigoId'] == entrada):
      listaPecas.remove(pecas)
      print("Peça removida!")
# ----------- Começo main -----------
print("Bem-vindo ao programa controle de peças da loja RN Automotivos ")
codigoPeca = 0
while True:
    try:
      opcao = int(input("Digite a opção desejada: \n1- Cadastrar Peça\n2-Consultar Peça\n3- Remover Peça\n4- Sair\n>>"))
      if opcao == 1:
        codigoPeca = codigoPeca + 1
        cadastrarPeca(codigoPeca)
      elif opcao == 2:
        consultarPeca()
      elif opcao == 3:
        removerPeca()
      elif opcao == 4:
        print("Programa finalizado")
        break
      else:
        print("Pare de digitar números invalidos")
        continue
    except ValueError:
      print("Pare de Digitar valores não inteiros")
