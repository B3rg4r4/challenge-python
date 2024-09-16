import datetime as dt

#Criacao de listas para armazenar dados dentro do programa sobre funcionarios e usuarios
listaUsuarios = []
listaVeiculos = []

listaFuncionarios = []

feedbacks = []

#Definicao de creat necessarios dentro do programa

def creat_Cadastro_Usuario(id, nmCompleto = "",dtNascimento = "", email = "", dtCadastro= ""):
    print("Cadastrando um Usuario ")
    dtCadastro = dt.now()
    usuario = {
        "Id" : id,
        "NomeCompleto" : nmCompleto,
        "dtNascimento" : dtNascimento,
        "email" : email,
        "Data de Cadastro" : dtCadastro
        }
    listaUsuarios.append(usuario)
    print("Esse foi o usuario " + listaUsuarios.index(id))
    return len(listaUsuarios)

def creat_Veiculo(id, nmCompleto, placa, problema, dtProblema, dtResolvido="Ainda nao foi resolvido"):
    print("Cadastrando um veiculo ")
    dtProblema = dt.now()
    if id in listaUsuarios or id in listaFuncionarios:
        veiculo = {
        "Dono": nmCompleto,
        "Placa": placa,
        "Problema": problema,
        "Data de Problema": dtProblema,
        "Data de Resolvido": dtResolvido
        }
        listaVeiculos.append(veiculo)
        print("Esse foi o usuario " + listaVeiculos.index(placa))
        return len(listaVeiculos)
    else:
        print("Nao foi possivel cadastrar o veiculo")

def creat_Cadastro_Funcionario(id, nmcompleto, idade , cpf, endereco, email , dtCadastro ):
    dtCadastro= dt.now()
    funcionario = {
        "Id" : id,
        "Nome Completo" : nmcompleto,
        "Idade" : idade,
        "CPF" : cpf,
        "Endereco" : endereco,
        "Email" : email,
        "Data de Cadastro" : dtCadastro
    }
    listaFuncionarios.append(funcionario)
    print("Esse foi o usuario " + listaFuncionarios.index(id))
    return len(listaFuncionarios)

#criacao de read dentro do programa, exibindo os usuarios, veiculos e funcionarios cadastrados

def read_Usuarios(id):
    if id in listaUsuarios:
        indice = listaFuncionarios.index(id)
        print(listaUsuarios[indice])
    else:
        print("Usuario não encontrado")
        return listaUsuarios
    
def read_veiculos(placa):
    if placa in listaVeiculos:
        indice = listaVeiculos.index(placa)
        return print(listaVeiculos[indice])
    else:
        print("Veiculo não encontrado")
        return listaVeiculos

def read_funcionarios(id):
    if id in listaFuncionarios:
        indice = listaFuncionarios.index(id)
        return print(listaFuncionarios[indice])
    else:
        print("Funcionario não encontrado")
        return listaFuncionarios

#criacao de update dentro do programa para atualizar informacoers dentro do programa

def update_cliente(id, nmCompleto = "",dtNascimento = "", email = ""):
    if id in listaUsuarios:
        indice = listaUsuarios.index(id)
        if nmCompleto!= "":
            listaUsuarios[indice].update({"Nome Completo" : nmCompleto})
        if dtNascimento!= "":
            listaUsuarios[indice].update({"Data de Nascimento" : dtNascimento})
        if email != "":
            listaUsuarios[indice].update({"Email" : email})
        return True 
    else:
        return False
    
def update_veiculo (id, nmCompleto="", placa="", problema="", dtProblema="", dtResolvido="Ainda nao foi resolvido"):
    if id in listaUsuarios or id in listaFuncionarios:
        indice = listaVeiculos.index(placa)
        if nmCompleto!= "":
            listaVeiculos[indice].update({"Dono" : nmCompleto})
        if placa != "":
            listaVeiculos[indice].update({"Placa" : placa})
        if problema != "":
            listaVeiculos[indice].update({"Problema" : problema})
        if dtProblema != "":
            listaVeiculos[indice].update({"Data do Problema" : dtProblema})
        if dtResolvido == "Ainda nao foi resolvido":
            listaVeiculos[indice].update({"Data de Resolvido" : dtResolvido})
        return True 
    else:
        return False

def update_Funcionario(id, nmcompleto="", idade="" , cpf="", endereco="", email=""):
    if id in listaFuncionarios:
        indice = listaFuncionarios.index(id)
        if nmcompleto != "":
            listaFuncionarios[indice].update({"Nome Completo" : nmcompleto})
        if idade != "":
            listaFuncionarios[indice].update({"Idade" : idade})
        if cpf != "":
            listaFuncionarios[indice].update({"CPF" : cpf})
        if endereco != "":
            listaFuncionarios[indice].update({"Endereço" : endereco})
        if email != "":
            listaFuncionarios[indice].update({"Email" : email})
        return True
    else:
        return False



#criacao de delete dentro do programa para deletar informacoes

def delete_usuario(id, indice):

    if id in listaFuncionarios:
        listaUsuarios.pop(indice)
        return True
    else:
        return False
    
def delete_funcionario(id, indice):
    if id in listaFuncionarios:
        listaFuncionarios.pop(indice)
        return True
    else:
        return False

def delete_veiculo(id, indice):
    if id in listaFuncionarios:
        listaVeiculos.pop(indice)
        return True
    else:
        return False
    
