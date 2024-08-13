print("Bem vindo ao Porta Car-Fix")

intecao = str(input("O que deseja fazer ? \n Você pode acessar seu perfil digitando '1' \n Você pode ver as opções de planos disponiveis e quais você  tem acesso digitando '2' \n Alguma duvida digite '3'\n Caso queira dar um feedback digite '4' \n "))

while intecao != "1" and intecao != "2" and intecao != "3" and intecao != "4":

    intecao = int(input("Aqui temos algumas opções possiveis dentro do nosso site \n Você pode acessar seu perfil digitando '1' \n Você pode ver as opções de planos disponiveis e quais você  tem acesso digitando '2'  \n Alguma duvida digite '3'\n Caso queira dar um feedbac digite '4' \n "))

if intecao == "1":
    cadastro = str(input("ja tem uma conta ? \n"))
    while cadastro != "sim" and cadastro != "não":
        cadastro = str(input("ja tem uma conta ? \n"))
    if cadastro == "sim":
        email = str(input("Digite seu email: "))
        senha = str(input("Digite sua senha: "))
    else:
        print("Crie sua conta aqui")
        email = str(input("Digite seu email: "))
        senha = str(input("Digite sua senha: "))
    print(f"O email cadastrado foi {email}")
elif intecao == "2":
    planos = str(input("Quer visualizar todos nossos planos ? \n"))
    while planos != "sim" and planos != "não":
         planos = str(input("Quer visualizar todos nossos planos ? \n"))
    if planos == "sim":
        print("Temos o planos de: Cobertura Total, que concede acesso a todos serviços dentro do nosso site \nCobertura Parcial, que vai de acordo com a sua região, automovel, e equipamento\nCobertura Mecânica, nesse plano tera acesso apenas acesso a analise de um mecanico ")
    else:
        print("para vizualiar seus planos faça cadastro")
elif intecao == 3:
    duvida = str(input("digite sua duvida, referente ao auto atendimento, a resposta pode ser rapida ou levar horas: "))

else:
    feedback = str(input("Digite aqui seu feedback para que possamos melhorar nosso serviço e oferecer uma melhor entrega de resultados: "))


