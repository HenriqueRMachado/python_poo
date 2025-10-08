# Importa a biblioteca 'importlib' para permitir a importação de módulos cujo nome 
# possa não ser uma variável Python válida (como nomes que começam com números).
# É uma técnica para garantir que o código das classes seja carregado.
import importlib 

# Importa módulos para colorir o texto no terminal
from colorama import init, Fore, Back, Style
# Inicializa o colorama
init()

# Importação Dinâmica de Classes:
# Usa importlib para carregar o módulo '01_restaurante_classes_principais.py' (que contém as classes definidas anteriormente).
# O nome 'classe_clientes' agora referencia este módulo importado, permitindo acesso às classes (ex: Pedidos).
classe_clientes = importlib.import_module("01_restaurante_classes_principais")

print(Fore.GREEN + "\nBem vindo ao nosso restaurante!" + Style.RESET_ALL)

# INSTANCIAÇÃO DE OBJETO (Orientação a Objetos):
# Cria-se uma instância (objeto) da classe 'Pedidos'. 
# Este objeto 'pedido_um' agora contém todos os métodos (mostrar_cardapio, fazer_pedido) 
# e atributos (herdados de Pratos e Ingredientes) necessários para interagir com o sistema.
pedido_um = classe_clientes.Pedidos()

# Laço de Controle Principal (Loop Interativo):
# O loop 'while True' mantém o programa em execução, permitindo que o cliente 
# interaja com o menu até que escolha sair ou fazer um pedido.
while True:
    
    try: # Inicia o bloco de tratamento de exceções (try/except) para evitar que o programa trave com entradas inválidas
        
        print(Fore.GREEN + "\n=====MENU====" + Style.RESET_ALL)
        print("1: Mostrar cardapio")
        print("2: Fazer pedido")
        print(Fore.RED + "3: Sair" + Style.RESET_ALL)  
        
        # Solicita a escolha do cliente. O tratamento de erro (try/except) lida com entradas não numéricas.
        cliente_escolha = int(input("\nEscolha uma das opcoes do menu acima: "))

        # Estrutura 'match/case' (a partir do Python 3.10) para controle de fluxo e menu de opções.
        match(cliente_escolha):
            case 1:
                # Chama o método 'mostrar_cardapio' do objeto 'pedido_um'.
                pedido_um.mostrar_cardapio()
            case 2:
                # Chama o método 'fazer_pedido' do objeto.
                pedido_um.fazer_pedido()
                # Interrompe o loop 'while True' após o pedido ser concluído.
                break 
            case 3:
                
                print(Fore.RED + "\nO programa esta encerrando..." + Style.RESET_ALL)
                # Adiciona uma pausa antes de sair (melhor experiência de usuário)
                import time as t
                t.sleep(2)
                # Interrompe o loop, encerrando o programa
                break
            
            case _:
                # Trata opções que não são 1, 2 ou 3.
                print(Fore.RED + "\nEsta opcao nao esta na lista de opcoes!" + Style.RESET_ALL)
    
    # Bloco 'except': Captura erros de valor (ex: quando o usuário digita texto em vez de um número)
    except:
        print(Fore.RED + "Informe apenas numeros no menu" + Style.RESET_ALL)
