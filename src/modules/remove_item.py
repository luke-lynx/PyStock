import file_manager as file_manager_
from pystockui import RemoveItemUI
import json
import os

class RemoveItensEngine:
    def __init__(self):

        self.file_manager = file_manager_.FileManager()

        self.user_file_path = self.file_manager.user_data

        self.removeui = RemoveItemUI()

        self.remove_itens()


    def remove_itens(self):
        
            id_name = self.removeui.welcome_to_remove_item() 

            if id_name is None:
                return

            if os.path.exists(self.user_file_path):
                with open(self.file_manager.user_data, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError as e:
                        print(
                            f"{self.removeui.RED}Error: Failed to parse user data file: {self.removeui.GREEN} {e.msg} in line {e.lineno} column {e.colno}{self.removeui.RESET}"
                        )
                        return
                    
                    item_encontrado = False
                    
                    for item in data:
 
                        nome_no_json = str(item.get("nome")).lower()
                        
                        if item.get("id") == id_name or nome_no_json == str(id_name):
                            item_encontrado = True
                            confirm = self.removeui.confirm_remove_item(item.get("nome"), item.get("quantidade"), item.get("id"))  # Part 2°
                            
                            if confirm in ["s", "sim", "y", "yes"]:
                                data.remove(item)
                                
                                with open(self.file_manager.user_data, "w", encoding="utf-8") as f:
                                    json.dump(data, f, indent=4, ensure_ascii=False)
                                print(f"{self.removeui.GREEN}Item removed successfully!{self.removeui.RESET}")
                            
                            else:
                                print(f"{self.removeui.RED}Removal cancelled. Returning to main menu...{self.removeui.RESET}")
                            
                            return

            
                    if not item_encontrado:
                        print(f"{self.removeui.RED}Error: Item not found. Please check the ID or name and try again.{self.removeui.RESET}")
                        return
            else:
                print(f"{self.removeui.RED}Error: User data file not found.{self.removeui.RESET}")
                return


if __name__ == "__main__":
    remove = RemoveItensEngine()