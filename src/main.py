from pathlib import Path
from modules import add_item, remove_item, list_item, update_item
import os 
import json
import sys


def main():
    #mensagem de boas vindas
    welcome_to_program()
    #criação de arquivos e confirmaçõa de perguntas essenciais
    ensure_data_file()
    #interface e opções
    interface()


def ensure_data_file():
    response = input("""Antes de começarmos temos um aviso.\nSerá necessario criar um novo arquivo mesmo se o usuario ja possui-lo, deseja continuar?\nDigite S ou N: _""").lower()                     
    
    if response in ["s","sim","yes","y"]:
        with open(user_data(), 'w', encoding='utf8') as f:
            dados = []
            json.dump(dados, f, indent=4, ensure_ascii=False)
            print("\nArquivo criado com sucesso!")
            
        
        base_itens = input("Deseja adicionar 50 itens mais comuns no seu gerenciador?? Digite S o N: _").lower()
        if base_itens in ["s","sim","yes","y"]:
            with open(initial_data(), 'r', encoding='utf8') as f:
                dados = json.load(f)
            
            with open(user_data(), 'w', encoding='utf8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
                print("50 Itens adicionados com sucesso! ")

        else:
            pass
    else:
        sys.exit(2)


def welcome_to_program():
    print("""\n--------------------------------------------------
THE FOOD MANAGER - v0.1
--------------------------------------------------
Bem-vindo ao sistema de gerenciamento de estoque.
Status: Online
--------------------------------------------------\n""")


def user_data():
    caminho_atual = Path(__file__).resolve()

    pasta_src = caminho_atual.parent

    pasta_raiz = pasta_src.parent

    pasta_data = pasta_raiz / "data"

    arquivo_json = pasta_data / "user_data.json"
    return arquivo_json


def initial_data():

    caminho_atual = Path(__file__).resolve()

    pasta_src = caminho_atual.parent

    pasta_raiz = pasta_src.parent

    pasta_data = pasta_raiz / "data"

    arquivo_json = pasta_data / "initial_data.json"
    return arquivo_json


def interface():
    while True:
        print("\n" + "="*50)
        print("MENU PRINCIPAL".center(50))
        print("="*50)
        print("  1. Adicionar Alimento")
        print("  2. Remover Alimento")
        print("  3. Alterar Alimento")
        print("  4. Listar Estoque")
        print("  5. Gerenciar Quantidades")
        print("-"*50)
        print("  0. Sair")
        print("="*50)

        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            add_item.add_item()
        elif opcao == "2":
            remove_item.remove_itens()
        elif opcao == "3":
            update_item.update_item()
        elif opcao == "4":
            list_item.list_all()
        elif opcao == "0":
            print("\nEncerrando...\n")
            break

        else:
            print("\nOpção invalida ou não disponivel nesta versão.\n")


if __name__ == "__main__":
    main()