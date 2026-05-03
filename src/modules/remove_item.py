from pathlib import Path
import os 
import json
import sys


def remove_itens():
    id_nome = first_part_interface()
    if os.path.exists(user_data()):
        with open(user_data(), 'r', encoding='utf8') as f:
            dados = json.load(f)
            for dado in dados:
                if id_nome in [dado["nome"], dado["id"]]:
                    result = second_part_interface(dado["nome"], dado["quantidade"], dado["id"])
                    if result in ["s", "sim", "y", "yes"]:
                        dados.remove(dado)
                        with open(user_data(), 'w', encoding='utf8') as f:
                            json.dump(dados, f, indent=4, ensure_ascii=False)
                    else:
                        break
                    break
                else:
                    pass


def user_data():
    caminho_atual = Path(__file__).resolve()

    pasta_modules = caminho_atual.parent
    
    pasta_src = pasta_modules.parent

    pasta_principal = pasta_src.parent

    pasta_data = pasta_principal / "data"

    arquivo_json = pasta_data / "user_data.json"
    return arquivo_json


def first_part_interface():
    print("\n" + "="*50)
    print("REMOVER ITEM DO ESTOQUE".center(50))
    print("="*50)
    while True:
        id_nome = input("Escolha entre ID ou Nome : ").lower()
        if id_nome == 'nome':
            nome =input("\n > Digite o Nome do item: ")
            return nome
        elif id_nome == 'id':
            id = int(input("\n > Digite o ID do item: "))
            return id
        else:
            print("ERROR")


def second_part_interface(nome, qtd, id):
    print("-"*50)
    print(" [!] ITEM ENCONTRADO:")
    print(f"     Nome: {nome} | Qtd: {qtd} | ID: {id}")
    print("-"*50)
    user_decision = input(" TEM CERTEZA QUE DESEJA REMOVER? (S/N): _").lower()
    return user_decision


if __name__ == "__main__":
    remove_itens()
