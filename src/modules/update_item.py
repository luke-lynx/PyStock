from file_manager import FileManager
from pystockui import UpdateItemUI
import time
import json
import os


class UpdateItemEngine:
    def __init__(self):
        self.file_manager = FileManager()
        self.user_file_path = self.file_manager.user_data
        self.ui = UpdateItemUI()
        self.update_item_main()

    def update_item_main(self):
        while True:
            user_choice = self.ui.top_update_interface()

            if user_choice == "0":
                print(f"\n{self.ui.RED}Update cancelled. Returning to main menu...{self.ui.RESET}")
                time.sleep(1)
                return
                
            elif user_choice == "1":
                id_busca = self.ui.search_by_id_interface()
                if id_busca is not None:
                    self.search_by_id(id_busca)
                    return   
            else:
                print(f"\n{self.ui.RED}Invalid option. Please select a valid option.{self.ui.RESET}")
                time.sleep(1.5)

    def search_by_id(self, id_busca):
        if not os.path.exists(self.user_file_path):
            print(f"\n {self.ui.RED}[ERROR]: The file '{self.user_file_path}' was not found.{self.ui.RESET}")
            input(" Press ENTER to return...")
            return
        
        with open(self.user_file_path, "r", encoding="utf8") as file:
            try:
                dados = json.load(file)
            except json.JSONDecodeError:
                print(f"\n{self.ui.RED}[ERROR]: Failed to read the database (Corrupted file).{self.ui.RESET}")
                input(" Press ENTER to return...")
                return
            
        found_item = False
        
        for item in dados:
            if item["id"] == id_busca:
                found_item = True
                
                if self.ui.located(item["id"], item["nome"], item["quantidade"]):
                    new_name, new_quantity = self.ui.edit_interface(item["nome"], item["quantidade"])
                    
                    confirm_user_change = self.ui.final_confirmation(
                        item["id"], item["nome"], item["quantidade"], new_name, new_quantity
                    )
                   
                    if confirm_user_change:
                        item["nome"] = new_name
                        item["quantidade"] = new_quantity
                        self.save_to_database(dados)
                    else:
                        print(f"\n{self.ui.YELLOW}[!] Update aborted. Changes were discarded.{self.ui.RESET}")
                        time.sleep(1.5)
                else:
                    print(f"\n{self.ui.YELLOW}[!] Item mismatched. Returning to main menu...{self.ui.RESET}")
                    time.sleep(1.5)
                break

        if not found_item:
            print(f"\n{self.ui.RED}[ERROR]: Item not found. Please check the ID and try again.{self.ui.RESET}")
            time.sleep(1.5)

    def save_to_database(self, dados_atualizados):
        print(f"\n {self.ui.YELLOW}[*] Committing changes to database file...{self.ui.RESET}")
        try:
            with open(self.user_file_path, "w", encoding="utf8") as file:
                json.dump(dados_atualizados, file, indent=4, ensure_ascii=False)
            print(f" {self.ui.GREEN}[SUCCESS]: Item updated successfully!{self.ui.RESET}")
            time.sleep(1.5)
        except Exception as e:
            print(f" {self.ui.RED}[ERROR]: Could not write to file. Details: {e}{self.ui.RESET}")
            input(" Press ENTER to continue...")


if __name__ == "__main__":
    engine = UpdateItemEngine()