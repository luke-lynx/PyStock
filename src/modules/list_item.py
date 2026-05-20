from pathlib import Path
import time
import os 
import json

def list_all():

    caminho_atual = Path(__file__).resolve()
    pasta_modules = caminho_atual.parent
    pasta_src = pasta_modules.parent
    pasta_principal = pasta_src.parent
    pasta_data = pasta_principal / "data"
    

    arquivo_json = pasta_data / "user_data.json"

    if os.path.exists(arquivo_json):
        with open(arquivo_json, 'r', encoding='utf8') as f:
            data_base_json = json.load(f)
            
            # --- Interface CLI ---
            os.system('cls' if os.name == 'nt' else 'clear')
            print("="*75)
            print(f"{'ESTOQUE ATUAL':^75}")
            print("="*75)
            

            print(f"{'ID':<4} | {'NOME DO ALIMENTO':<30} | {'QTD':<6} | {'CATEGORIA':<15} | {'STATUS'}")
            print("-"*75)

            for data in data_base_json:
               
                qtd = data.get('quantidade', 0)
                if qtd == 0:
                    status = "ESGOTADO"
                elif qtd <= 5:
                    status = "BAIXO"
                else:
                    status = "OK"

                
                print(f"{data.get('id', '??'):<4} | "
                      f"{data.get('nome', 'Sem Nome')[:30]:<30} | "
                      f"{qtd:<6} | "
                      f"{data.get('categoria', 'Geral'):<15} | "
                      f"{status}")

            print("-"*75)
            print(f"Total de itens listados: {len(data_base_json)}")
            print("="*75)
            input("\nPressione Enter para voltar ao menu...")

    else:
        print(f"\n[!] Erro: Arquivo {arquivo_json.name} não encontrado.")
        time.sleep(2)
        return 1

if __name__ == "__main__":
    list_all()