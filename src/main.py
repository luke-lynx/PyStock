from pathlib import Path
from modules import add_item, remove_item, list_item, update_item
import os 
import json
import sys


def main():
    #welcome_to_program >>> PyStockUI
    
    
    
    #initial_screen_opening_data_saving()
    #interface e opções
    interface()

def initial_screen_opening_data_saving():
    create_new = input("""Antes de começarmos temos um aviso.\nSerá necessario criar um novo arquivo mesmo se o usuario ja possui-lo, deseja continuar?\nDigite S ou N: _""").lower()    
    if create_new in ["n","nao","no","n"]:
        print("\nEncerrando...\n")
        sys.exit()
    else:
        pass
        
    home_screen_open_file()

def home_screen_open_file():
    response = input("""Antes de começarmos temos um aviso.\nSerá necessario criar um novo arquivo mesmo se o usuario ja possui-lo, deseja continuar?\nDigite S ou N: _""").lower()
    
    if response in ["s","sim","yes","y"]:
        with open(user_data(), 'w', encoding='utf8') as f:
            dados = []
            json.dump(dados, f, indent=4, ensure_ascii=False)
            
            print("\nArquivo criado com sucesso!")
            return dados

def add_50_items():
        base_itens = input("Deseja adicionar 50 itens mais comuns no seu gerenciador?? Digite S o N: _").lower()
        
        if base_itens in ["s","sim","yes","y"]:
            with open(initial_data(), 'r', encoding='utf8') as f:
                dados = json.load(f)
            
            with open(user_data(), 'w', encoding='utf8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
                print("50 Itens adicionados com sucesso! ")

        else:
            pass






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

        acoes = {
            "1": add_item.add_item,
            "2": remove_item.remove_itens,
            "3": update_item.update_item,
            "4": list_item.list_all,
        }

        while True:
            opcao = input("Escolha uma opcao: ")

            if opcao == "0":
                print("\nEncerrando...\n")
                break


            acao_escolhida = acoes.get(opcao)


            if acao_escolhida:
                acao_escolhida() 
            else:
                print("\nOpção inválida...\n")



if __name__ == "__main__":
    main()