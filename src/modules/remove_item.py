from file_manager import FileManager
from pystockui import RemoveItemUI
import os
import json



class RemoveItensEngine:
    def __init__(self):

        self.removeui = RemoveItemUI()

        self.file_manager = FileManager()

        self.user_file_path = self.file_manager.user_data

    def remove_itens(self):

        id_nome = self.removeui.welcome_to_remove_item()  # part 1°

        if os.path.exists(self.user_file_path):

            with open(self.user_data(), "r", encoding="utf8") as f:
                dados = json.load(f)

                for dado in dados:
                    if id_nome in [dado["nome"], dado["id"]]:
                        result = self.second_part_interface(
                            dado["nome"], dado["quantidade"], dado["id"]
                        )
                        if result in ["s", "sim", "y", "yes"]:
                            dados.remove(dado)
                            with open(self.user_data(), "w", encoding="utf8") as f:
                                json.dump(dados, f, indent=4, ensure_ascii=False)
                        else:
                            break
                        break
                    else:
                        pass

    def second_part_interface(self, nome, qtd, id):
        print("-" * 50)
        print(" [!] ITEM ENCONTRADO:")
        print(f"     Nome: {nome} | Qtd: {qtd} | ID: {id}")
        print("-" * 50)
        user_decision = input(" TEM CERTEZA QUE DESEJA REMOVER? (S/N): _").lower()
        return user_decision


if __name__ == "__main__":
    remove = RemoveItensEngine()
    remove.remove_itens()
