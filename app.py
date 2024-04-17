import os

#função -> bloco de código que realiza uma determinada ação

#função para apresentar o nome do programa no console
def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

#função para exibir as opções
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

#função para finalizar o app
def finalizar_app():
    os.system('cls') #cls para o windows, se mac clear o comando
    print('Encerrando o app \n')

#escolhe a opção e chama outras funções
def escolher_opcao():
    #armazena a entrada da op;áo escolhida usando o input
    #a variavel, por convenção, deve ser usando o _ para separar as palavras
    #alterar o tipo da variavel -> variavel = tipo(variavel) ou no input como abaixo
    opcao_escolhida = int(input('Escolha uma opção: '))

    #imprime o valor escolhido armazeando na variavel
    #print('Você escolheu a opção: ', opcao_escolhida)
    #interpolar (juntar strings)= juntar, contatenar um texto e a variavel
    print(f'Você escolheu a opção: {opcao_escolhida}')

    #condição
    if opcao_escolhida == 1 :
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

    #opção com Match (switch case) -> simplificar a lógica do código em situações que envolvem múltiplos padrões complexos:
    #opcao_escolhida = int(input('Escolha uma opção: '))
    #match opcao_escolhida:
    #    case 1:
    #        print('Adicionar restaurante')
    #    case 2:
    #        print('Listar restaurantes')
    #    case 3:
    #        print('Ativar restaurante')
    #    case 4:
    #        print('Finalizar app')
    #    case _:
    #        print('Opção inválida!')




#função para chamar na main
def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

#deixar como arquivo princial, ou seja, main e não será importado por outros 
if __name__ == '__main__':
    main()
