
#print para receber o usuario no programa
print("Bem vindo ao Porta Car-Fix")

#Criação de listas para armazenar e organizar dados inseridos pelo usuario
emails = []
nomes = []
placas = []
feedbacks = []
duvidas = []

#função para caso o usuario escolha fazer cadastro no programa
def cadastro():
    while True:
        cadastro = str(input("ja tem uma conta ? \n"))
        #laço caso o usuario escolha uma função que não esta presente nas opções
        while cadastro != "sim" and cadastro != "não":
            cadastro = str(input("ja tem uma conta ? \n"))
        if cadastro == "sim":
            email = str(input("Digite seu email: "))
            senha = str(input("Digite sua senha: "))
        else:

            print("Crie sua conta aqui")

            nomes.append(str(input("Digite seu nome:\n")))
            emails.append(str(input("Digite seu email:\n")))
            senha = str(input("Digite sua senha:\n"))
            confirmSenha = str(input("Confirme sua senha:\n"))
            while senha != confirmSenha:
                print("ERRO!Algum campo foi preenchido errado ")
                senha = str(input("Digite sua senha:\n"))
                confirmSenha = (str(input("Confirme sua senha:\n")))
            print("Seu cadastro foi realizado com sucesso!")
            cadastrarVeiculo = str(input("Deseja cadastrar algum veiculo ?"))
            match cadastrarVeiculo:
                case "sim":
                    placas.append(str(input("Para Começarmos, digite os digitos da sua placa:\n")))
                case "não":
                    print("Tudo bem !! Obrigado por utilizar o Porta Car-Fix, volte sempre que precisar de uma ajuda com seus veiculos ")
                case _:
                    print("Opção não cadastrada")


            print(f"O email cadastrado foi {emails}")

##função para alterar alguma informação cadastrada
def mudarInfor ():
    print("Escolha a informação que deseja alterar:")

#função caso o usuario escolha ver os planos do nosso serviço
def planos():
    while True:
        planos = str(input("Quer visualizar todos nossos planos ? \n"))
        #laço caso o usuario escolha uma opção que não esta disponivel
        while planos != "sim" and planos != "não":
            planos = str(input("Quer visualizar todos nossos planos ? \n"))
        if planos == "sim":
            print("Temos o planos de: Cobertura Total, que concede acesso a todos serviços dentro do nosso site \nCobertura Parcial, que vai de acordo com a sua região, automovel, e equipamento\nCobertura Mecânica, nesse plano tera acesso apenas acesso a analise de um mecanico ")
        else:
            print("para vizualiar seus planos faça cadastro")
            
        break

#função caso o usuario escolha mandar uma duvida para a central de atendimento
def duvida():
    while True:
        duvidas = str(input("digite sua duvida, referente ao auto atendimento, a resposta pode ser rapida ou levar horas: "))
        break

#função caso o usuario queira dar um feedback para a empresa
def feedback():
    while True:
        feedbacks = str(input("Digite aqui seu feedback para que podemos melhorar nosso serviço e oferecer uma melhor entrega de resultados: "))
        break

while True:

    intencao = str(input("O que deseja fazer ? \n Você pode acessar seu perfil digitando '1' \n Você pode ver as opções de planos disponiveis e quais você tem acesso digitando '2' \n Alguma duvida digite '3'\n Caso queira dar um feedback digite '4' \n "))
    
    while intencao != "1" and intencao != "2" and intencao != "3" and intencao != "4":
    #laço de repetiçao para caso o usuario insira uma opção não cadastrada
        intencao  = str(input("Aqui temos algumas opções possiveis dentro do nosso site\n Você pode acessar seu perfil digitando '1', caso queira mudar alguma informção de cadastro digite 'alterar'\n Você pode ver as opções de planos disponiveis e quais você  tem acesso digitando '2'\n Alguma duvida digite '3'\n Caso queira dar um feedback digite '4' \n "))
    match intencao:
        case "1":cadastro()

        case "2":planos()

        case "3":duvida()

        case "4":feedback()

        case _:
            print("Opção não cadastrada")
