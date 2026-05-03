from pathlib import Path
import json
import os



def update_item():
# 1. Configurações Iniciais
    open_file = user_data_open_file()
    escolha_menu = top_update_interface()

    # Se o usuário escolheu buscar por ID (opção "1")
    if escolha_menu == "1":
        id_busca = id_interface()
        
        # Validação de existência do banco de dados
        if not os.path.exists(open_file):
            print(f"\n [ERRO]: O arquivo '{open_file}' não foi encontrado.")
            input(" Pressione ENTER para voltar...")
            return

        # 2. Leitura do Banco de Dados
        with open(open_file, 'r', encoding='utf8') as file:
            try:
                dados = json.load(file)
            except json.JSONDecodeError:
                print(" [ERRO]: Falha ao ler o banco de dados (Arquivo corrompido).")
                return

        item_encontrado = False

        # 3. Busca e Processamento
        for item in dados:
            if item["id"] == id_busca:
                item_encontrado = True
                loading(id_busca)
                located(item["id"], item["nome"], item["quantidade"])
                
                # Coleta as novas informações 
                novo_nome, nova_qtd = mudar_nome_quantidade(item["nome"], item["quantidade"])
                
                # 4. Interface de Resumo e Confirmação
                print("\n" + "="*70)
                print(f"{'RESUMO DAS ALTERAÇÕES':^70}")
                print("="*70)
                print(f" NOME      : {item['nome']:<25}  -->  {novo_nome}")
                print(f" QUANTIDADE: {item['quantidade']:<25}  -->  {nova_qtd}")
                print("-" * 70)
                
                confirmar = input(" DESEJA GRAVAR ESTAS ALTERAÇÕES PERMANENTEMENTE? (s/n): ").lower()
                
                if confirmar in ["s", "sim", "y", "yes"]:
                    # Atualiza os dados na memória
                    item["nome"] = novo_nome
                    item["quantidade"] = nova_qtd
                    
                    # 5. Salvamento Físico (Sobrescreve o arquivo com a lista atualizada)
                    print("\n [!] Gravando dados no banco...")
                    with open(open_file, 'w', encoding='utf8') as file:
                        json.dump(dados, file, indent=4, ensure_ascii=False)
                    
                    print(" [OK] Update concluído com sucesso!")
                else:
                    print("\n [!] Alteração descartada pelo usuário.")
                
                break # Sai do loop após encontrar o ID

        if not item_encontrado:
            print(f"\n [SISTEMA]: O ID '{id_busca}' não foi localizado no banco.")

        print("\n Pressione ENTER para voltar ao menu principal...")
        input()


def mudar_nome_quantidade(nome_atual, qtd_atual):
    print(f"\n{'>>> ALTERAÇÃO DE DADOS':^30}")
    
    # 1. Lógica para o Nome
    alterar_n = input(f" Deseja alterar o nome '{nome_atual}'? (s/n): ").lower()
    if alterar_n in ["s", "sim", "y", "yes"]:
        novo_nome = input(" Digite o novo nome: ")
        confirma = input(f" [CONFIRMAÇÃO]: Salvar '{novo_nome}'? (s/n): ").lower()
        if confirma in ["s", "sim", "y", "yes"]:
            nome_atual = novo_nome
            print(" [SISTEMA]: Nome atualizado.")

    # 2. Lógica para a Quantidade
    alterar_q = input(f" Deseja alterar a quantidade ({qtd_atual})? (s/n): ").lower()
    if alterar_q in ["s", "sim", "y", "yes"]:
        try:
            nova_qtd = int(input(" Digite a nova quantidade: "))
            qtd_atual = nova_qtd
            print(" [SISTEMA]: Quantidade atualizada.")
        except ValueError:
            print(" [ERRO]: Valor inválido. A quantidade não foi alterada.")

    return nome_atual, qtd_atual


def located(id_, nome, quantidade):
    print("-"*70)
    print(" [ ITEM LOCALIZADO COM SUCESSO ]")
    print("-"*70)
    print(f" ID        : {id_}")
    print(f" NOME      : {nome}")
    print(f" QUANTIDADE: {quantidade}")
    print(f"-"*70)


def loading(id_):
    print("[ SISTEMA ]: Consultando base de dados .json...")
    print(f"[ STATUS  ]: Buscando correspondências para '{id_}' ...")
    print("-"*70)


def top_update_interface():
    print("="*70)
    print("SISTEMA DE ATUALIZAÇÃO (v0.1.4)".center(70))
    print("="*70)
    print(" Como deseja localizar o item para edição?\n")
    print(" [1] Buscar por ID (Exato)\n"
    " [2] Buscar por NOME (Palavra-chave)\n"
    " [0] Cancelar e Voltar\n")
    option = input(" Digite sua opção: _")
    return option


def id_interface():
    print("-"*70)
    print(" >>> BUSCA POR IDENTIFICADOR (ID)")
    print("-"*70)
    id_ = int(input(" Digite o ID do item (ex: 1, 42): _"))
    return id_


def user_data_open_file():
    caminho_atual = Path(__file__).resolve()

    pasta_modules = caminho_atual.parent
    
    pasta_src = pasta_modules.parent

    pasta_principal = pasta_src.parent

    pasta_data = pasta_principal / "data"

    arquivo_json = pasta_data / "user_data.json"
    return arquivo_json

if __name__ =="__main__":
    update_item()