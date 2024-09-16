from crudPorto import *
#Importando informacoes e funcoes dentro da classe de crud para utilizacao dentro da aplicacao principal
#dentro do crud esta armazenado listas, tuplas, dicionarios entre outros

#print para receber o usuario no programa
print("Bem vindo ao Porta Car-Fix \n A Central de auxilio aos Motoristas feita para voce")

while True:
    intencao = int(input("Digite o que deseja fazer \n1 para adicionar informacoes\n2 para ver as listas\n3 para atualizar dados\n4 para deletar dados\n5 para fechar o programa: "))
    while intencao != 1 or intencao != 2 or intencao != 3 or intencao != 4 or intencao !=5:
        print("Opcao invalida, tente digitar apenas 1,2,3 ou 4")
        intencao = int(input("Digite o que deseja fazer \n1 para adicionar informacoes\n2 para ver as listas\n3 para atualizar dados\n4 para deletar dados: "))
    if intencao == 1:
        op1 = int(input("O que deseja adicionar?\n1 para usuario\n2 para veiculo\n3 para funcionario\n4 para sair\n"))
        while op1 != 1 or op1 != 2 or op1 != 3 or op1 != 4:
            print("Opcao invalida, tente digitar apenas 1,2 ou 3 para acessar as informacoes")
            op1 = int(input("O que deseja adicionar?\n1 para usuario\n2 para veiculo\n3 para funcionario\n4 para sair\n"))
        if op1 == 1:
            id = input("Digite o codigod de identificacao do cliente: ")
            nmCompleto = input("Digite o nome completo do cliente: ")
            dtNascimento = input("Digite a data de nascimento do cliente: ")
            email = input("Digite o email do usuario: ")

            creat_Cadastro_Usuario(id=id, nmCompleto=nmCompleto, dtNascimento=dtNascimento, email=email)
            print("Cadastro realizado com sucesso!")
        if op1 ==2:
            id= input("Digite o id de quem esta cadastrando o veiculo: ")
            dono = input("Digite o nome do completo do dono do carro: ")
            placa = input("Digite a placa do carro: ")
            problema= input("Digite qual o problema do veiculo: ")

            creat_Veiculo(id=id,nmCompleto=dono,placa=placa, problema=problema)
            print("Cadastro de veiculo concluido")

        if op1 == 3:
            id = input("Digite o codigo de identificacao do funcionario")
            nmCompleto = input("Digite o nome completo do funcionario")
            idade = input("Digite a idade completa do funcionario")
            cpf= input("Digite o cpf do funcionario")
            endereco= input("Digite o endereco do funcionario")
            email = input("Digite o email do funcionario")
            if idade < 18:
                print("Idade invalida, o funcionario precisa ter mais de 18 anos")
            creat_Cadastro_Funcionario(id=id, nmCompleto= nmCompleto,idade=idade, cpf=cpf, endereco=endereco, email=email)
            print("Cadastro de funcionario concluido")
        if op1 == 4:
            print("Voltando")
            break
          
    if intencao == 2:
        op2 = input ("Digite qual lista quer ver \n1 Para cliente\n2 para veiculos\n3 para funcionario\n4 para sair do programa")
        while op2 != 1 and op2 != 2 and op2 != 3 and op2 != 4:
            print("opcao invalida")
            op2 = input ("Digite qual lista quer ver \n1 Para cliente\n2 para veiculos\n3 para funcionario\n4 para sair do programa")
        if op2 == 1:
            id = input ("Digite o id de quem vai visualizar a lista de usuarios")
            read_funcionarios(id=id)
        if op2 ==2:
            id = input ("Digite o id de quem vai visualizar a lista de veiculos")
            placa= input("Digite a plca do carro que quer visualizar ")
            read_veiculos(id=id, placa=placa)
        if op2 ==3 :
            id = input("Digite o id do funcionario ")
            read_funcionarios(id=id)
        if op2 == 4:
            print("Voltando")
            break
    if intencao == 3 :
        op3 = int(input("Qual informações voce quer mudar ?\n1 para cliente\n2 para veiculo\n3 para funcionario\n 4 para voltar "))
        while op3 != 1 or op3 != 2 or op3 != 3 or op3 != 4:
            print("opcao invalida")
            op3 = int(input("Qual informações voce quer mudar ?\n1 para cliente\n2 para veiculo\n3 para funcionario\n 4 para voltar "))
        if op3 == 1:
            id=input("coloque o id do cliente")
            i = input("O que deseja alterar no usuario ?\n 1 nome\n2 data de nascimento\n3 email ?\n")
            while i != 1 or i != 2 or i != 3:
                print("opcao invalida") 
                i = input("O que deseja alterar no usuario ?\n 1 nome\n2 data de nascimento\n3 email ?\n")
            if i ==1:
                attNome = input("Digite o nome completo que deseja colocar")
            if i == 2 :
                attDtNascimento = input("coloque a nova data de nascimento")
            if i ==3 :
               attEmail = input("digite o novo email que deseja colocar")
            update_cliente(id=id, nmCompleto=attNome, dtNascimento=attDtNascimento, email=attEmail)
            print("informações atualizadas")
            if i == 4:
                print("voltando")
                break

        if op3 == 2:
            id= input("Digite o seu id ")

            i2 = input("O que deseja alterar no veiculo ?\n 1 nome do dono\n2 placa\n3 problema \n4 dia que ocorreu o Problema\n5 estado atual do veiculo\n 6 para sair ")
            while i2 != 1 or i2 != 2 or i2 != 3 or i2 != 4 or i2 != 5:
                print("opcao invalida") 
                i2 = input("O que deseja alterar no veiculo ?\n 1 nome do dono\n2 placa\n3 problema \n4 dia que ocorreu o Problema\n5 estado atual do veiculo\n6 para sair ")
            if i2 ==1:
                attDono = input("Digite o novo nome do dono ")
            if i2 ==2:
                attPlaca= input("Digite a placa")
            if i2 ==3:
                attProblema= input("DIgite qual o problema ")
            if i2 ==4:
                attDiaProblema = input("Digite o dia do problema ")
            if i2 ==5:
                attSituacao = input("Digite a situacao atual do veiculo")
            if i2 ==6:
                print("voltando")
                break
            update_veiculo(id= id,nmCompleto=attDono, placa=attPlaca, problema=attProblema, dtProblema=attDiaProblema,dtResolvido=attSituacao)

        if op3 == 3:
            id = input("Digite o id de funcionario que vai alterar")
            i3 = input("O que deseja alterar no funcionario ?\n 1 nome do funcionario\n2 idade\n3 cpf \n4 endereco \n5 email\n 6 para sair ")
            while i3 != 1 or i3 != 2 or i3 != 3 or i3 != 4 or i3 != 5:
                print("opcao invalida") 
                i3 = input("O que deseja alterar no funcionario ?\n 1 nome do funcionario\n2 idade\n3 cpf \n4 endereco \n5 email\n 6 para sair ")
            if i3 ==1:
                attNome = input("Digite o nome do funcionario")
            if i3 == 2:
                attIdade = input("Digite a idade do funcionario")
            if i3 ==3:
                attCpf = input("Digite o cpf do funcionario")
            if i3 == 4:
                attEndereco = input("Digite o endereco do funcionario ")
            if i3 == 5:
                attEmail = input("Digite o email do funcionario ")
            if i3 == 6:
                print("Voltando")
                break
            update_Funcionario(id, nmCompleto=attNome, idade=attIdade , cpf=attCpf, endereco=attEndereco, email=attEmail)
        if op3 ==4 :
            print("voltando")
            break 
    if intencao == 4:
            id= input("Digite o seu id ")

            i4 = input("O que deseja deletar ?\n 1 usuario\n2 funcionario\n3 veiculo\n4 para sair")
            while i4 != 1 or i4 != 2 or i4 != 3 or i4 != 4 or i4 != 5:
                print("opcao invalida") 
                i4 = input("O que deseja deletar ?\n 1 usuario\n2 funcionario\n3 veiculo\n4 para sair")

            if i4 == 1:
                id = input("Digite o id")
                indice = input("Digite o indice de quem vai ser excluido")
                delete_usuario(id=id, indice=indice)

            if i4 ==2:
                id = input("digite o id ")
                indice = input("Digite o indice do funcionario que deseja excluir ")
                delete_funcionario(id = id, indice=indice)

            if i4 ==3:
                id = input("Digite seu id ")
                indice = input("Digite o indice do carro que deseja excluir")

            if i4 == 4:
                print("Voltando")
                break
    if intencao == 5:
        print("Fechando programa")
        break