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
              