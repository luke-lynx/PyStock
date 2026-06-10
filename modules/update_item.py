import sys
from pathlib import Path

# Add parent directory to path to allow imports from root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pystockui import UpdateItemUI
import time

class UpdateItemEngine:
    def __init__(self, data_base):
        self.data_base = data_base
        self.ui = UpdateItemUI()

    def execute(self):
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

        data = self.data_base.db_fetch_all()
            
        found_item = False
        
        for item in data:
            if item["id"] == id_busca:
                found_item = True
                
                if self.ui.located(item["id"], item["name"], item["quantity"]):
                    new_name, new_quantity, new_price = self.ui.edit_interface(item["name"], item["quantity"], item["price"])
                    
                    confirm_user_change = self.ui.final_confirmation(
                        item["id"], item["name"], item["quantity"], item["price"], new_name, new_quantity, new_price
                    )
                   
                    if confirm_user_change:
                        self.save_to_database(item["id"], new_name, new_quantity, new_price)

                    else:
                        print(f"\n{self.ui.YELLOW}[!] Update aborted. Changes were discarded.{self.ui.RESET}")
                        time.sleep(1.5)
                        return None
                else:
                    print(f"\n{self.ui.YELLOW}[!] Item mismatched. Returning to main menu...{self.ui.RESET}")
                    time.sleep(1.5)
                return None

        if not found_item:
            print(f"\n{self.ui.RED}[ERROR]: Item not found. Please check the ID and try again.{self.ui.RESET}")
            time.sleep(1.5)

    def save_to_database(self, id, new_name, new_quantity, new_price):
        print(f"\n {self.ui.YELLOW}[*] Committing changes to database file...{self.ui.RESET}")
        self.id = id
        self.new_name = new_name
        self.new_quantity = new_quantity
        self.new_price = new_price
        self.data_base.db_update_item(self.id, self.new_name, self.new_quantity, self.new_price)
        print(f" {self.ui.GREEN}[SUCCESS]: Item updated successfully!{self.ui.RESET}")
        time.sleep(1.5)
    
        input(" Press ENTER to continue...")


if __name__ == "__main__":
    engine = UpdateItemEngine()