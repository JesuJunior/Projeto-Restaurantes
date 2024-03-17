import os

restaurantes = []

#EVENTOS--------------------------------------------------------

def subtitulo(text):
    os.system('cls')
    print(text, '\n')

def voltar_menu():
    input('\nClique enter para voltar ao menu! ')
    main()
    
def erro(text):
    os.system('cls')
    print('ERRO!\n', text)
    voltar_menu()

#OPÇÕES--------------------------------------------------------

def cadastro():
    subtitulo('CADASTRO DE RESTAURANTES!')
    nome_restaurante = input('Digite o nome do restaurante a ser cadastrado: ')
    categoria_restaurante = input('Qual a categoria do seu restaurante? ')
    dados_restaurante = {'nome' : nome_restaurante, 'categoria' : categoria_restaurante, 'ativo' : False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()


def lista():
    subtitulo('LISTA DOS RESTAURANTES CADASTRADOS')
    print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | STATUS \n')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu()

def ativar():
    subtitulo('ALTERNAR O ESTADO DO RESTAURANTE')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            print(f'Restaurante {nome_restaurante} encontrado!')
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo'] == True:
                print(f'O restaurante {nome_restaurante} foi ativado com sucesso!')
            else: 
                print(f'O restaurante {nome_restaurante} foi desativado com sucesso!')
    if restaurante_encontrado == False:
        erro('RESTAURANTE NÃO ENCONTRADO')
    voltar_menu()

    
def finalizar_programa():
    subtitulo('ENCERRANDO O PROGRAMA')

#MENU--------------------------------------------------------

def mostrar_nome():
    print('𝒮𝒜𝐵𝒪𝑅 𝐸𝒳𝒫𝑅𝐸𝒮𝒮\n')

def mostrar_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastro()
            case  2:
                lista()
            case 3:
                ativar()
            case 4:
                finalizar_programa()
            case _:
                erro()
    except:
        erro('NÚMERO INVÁLIDO!')

#--------------------------------------------------------

def main():
    os.system('cls')
    mostrar_nome()
    mostrar_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()