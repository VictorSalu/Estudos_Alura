import os

restaurantes = ['temakeria', 'mcdonalds']

def banner():

    print("""
      
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      """)

def opcoes():
    
    print('1. Cadastro de restaurante')
    print('2. Lista de restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')




def finalizar_programa():
    exibir_subtitulo('Encerrando programa\n')
    

def voltar_menu_principal():
    input('\nDigite uma tecla para retornar ')
    main()
    
def opcao_inavlida():
        print('Opção inválida!\n')
        voltar_menu_principal()        

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} foi cadastrado com sucesso ! ')
    voltar_menu_principal()

def lista_de_restaurantes():
    exibir_subtitulo('Listar os restaurantes:\n')
    
    
    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_menu_principal()

def escolher_opcoes():
    try:
        escolha = int(input('Escolha uma opção: '))
        if escolha == 1:
            cadastrar_novo_restaurante()
        elif escolha == 2:
            lista_de_restaurantes()
        elif escolha == 3:
            print('Ativar restaurante')    
        else:
            finalizar_programa()
    except:
        opcao_inavlida()    

def main():
    os.system('cls')
    banner()
    opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()