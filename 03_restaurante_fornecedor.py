# Importa a biblioteca 'importlib' para permitir a importação de módulos com nomes não convencionais.
import importlib 

# Importação Dinâmica de Classes:
# Carrega o módulo que contém a classe 'Fornecedor'.
classe_fornecedor = importlib.import_module("01_restaurante_classes_principais")

from colorama import init, Fore, Back, Style
init()

print(Fore.GREEN + "Bem vindo ao sistema de fornecimento do restaurante." + Style.RESET_ALL)

# DEMONSTRAÇÃO DO COMPARTILHAMENTO DE ESTOQUE (SINGLETON SIMPLIFICADO):
# INSTANCIAÇÃO 1: Cria o primeiro objeto 'forn'.
# Na primeira vez, o construtor da classe 'Fornecedor' cria e inicializa o estoque COMPARTILHADO.
forn = classe_fornecedor.Fornecedor()
# INSTANCIAÇÃO 2: Cria o segundo objeto 'forn2'.
# Na segunda vez, o construtor detecta que o estoque compartilhado já existe e ATRIBUI o mesmo estoque a 'forn2'.
# Isso garante que 'forn' e 'forn2' manipulem exatamente o mesmo dicionário de estoque, provando o conceito de POO de compartilhamento de dados de CLASSE.
forn2 = classe_fornecedor.Fornecedor()

# Laço de Controle Principal para o Menu do Fornecedor
while True:
    try:
        print(Fore.GREEN + "\n========MENU=======" + Style.RESET_ALL)
        print("1: Mostrar estoque")
        print("2: Alterar estoque")
        print(Fore.RED + "3: Sair" + Style.RESET_ALL)  
    
        fornecedor_escolha = int(input("\nEscolha uma das opcoes do menu acima: "))
        match(fornecedor_escolha):
            
            case 1:
                # Mostrar Estoque: O método 'mostra_estoque' acessa e exibe o dicionário de estoque compartilhado.
                # Não importa se chamamos 'forn.mostra_estoque()' ou 'forn2.mostra_estoque()', o resultado será o mesmo.
                forn.mostra_estoque()
            
            case 2:
                # Alterar Estoque:
                abastecer = input('\nInforme o nome do produto que deseja abastecer no estoque: ')
                
                try:
                    # Input para a quantidade
                    qtde = int(input("\nInforme a quantidade do produto que deseja abastecer no estoque: "))
                except:
                    # Trata o erro se a quantidade não for um número inteiro
                    print(Fore.RED + "qtde precisa ser um numero" + Style.RESET_ALL)
                    continue # Volta para o início do loop
                    
                # Atualização do Estoque:
                # O método 'atualiza_estoque' é chamado usando a SEGUNDA instância ('forn2').
                # O valor '{qtde}' parece ser um erro de formatação na linha original e foi corrigido (se necessário), 
                # mas o ponto chave é que a alteração feita por 'forn2' será vista por 'forn' (compartilhamento).
                forn2.atualiza_estoque(f"{abastecer}", qtde) # OBS: Corrigi para 'qtde' em vez de '{qtde}' assumindo que se queria passar o valor inteiro
                
                # Para fins de apresentação, você pode adicionar:
                # print("\nVerificando o estoque com a primeira instância (forn):")
                # forn.mostra_estoque() # Esta linha PROVA que 'forn' vê a mudança feita por 'forn2'

            case 3:
                
                print(Fore.RED + "\nO programa esta encerrando..." + Style.RESET_ALL)
                import time as t
                t.sleep(2)
                break
        
            case _:
                print(Fore.RED + "\nEsta opcao nao esta na lista de opcoes!" + Style.RESET_ALL)
    except:
        # Trata o erro se a escolha do menu principal não for um número inteiro
        print(Fore.RED + "Informe apenas numeros no menu" + Style.RESET_ALL)
