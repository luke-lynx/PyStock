from file_manager import FileManager
from pystockui import RemoveItemUI
import json
import os


class RemoveItensEngine:
    def __init__(self):

        self.file_manager = FileManager()

        self.user_file_path = self.file_manager.user_data

        self.removeui = RemoveItemUI()

    def remove_itens(self):
    
        id_nome = self.removeui.welcome_to_remove_item()  # part 1°

        if os.path.exists(self.user_file_path):
            
            with open(self.user_file_path(), "r", encoding="utf8") as f:
                dados = json.load(f)

                for dado in dados:

                    if id_nome in [dado["nome"], dado["id"]]:

                        result = self.removeui.second_part_interface(
                            dado["nome"], dado["quantidade"], dado["id"]
                        )

                        if result in ["s", "sim", "y", "yes"]:
                            dados.remove(dado)
                        
                            with open(self.user_file_path(), "w", encoding="utf8") as f:
                                json.dump(dados, f, indent=4, ensure_ascii=False)
                        else:
                            return None
                        return None
                    else:
                        pass


if __name__ == "__main__":
    remove = RemoveItensEngine()