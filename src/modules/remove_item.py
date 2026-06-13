import sys
from pathlib import Path

# 13/06/2026
# linha 36-60 busca de item, validação e remoção do banco de dados chamandos self.data_base


# Add parent directory to path to allow imports from root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pystockui import RemoveItemUI
import time

class RemoveItensEngine:
    def __init__(self, data_base):
        self.data_base = data_base
        self.removeui = RemoveItemUI()

    def execute(self):
        self.remove_itens()

    def remove_itens(self):

            # Item name or ID input
            self.removeui.welcome_to_remove_item_interface()
            
            id_name_input = self.item_name_id_input()
            if id_name_input is None:
                return

            # Search for the item by ID or name
            self.search_in_data_base = self.data_base.db_search_item(id_name_input)

            item_encontrado = False

            for item in self.search_in_data_base:
                if item["id"] == id_name_input or item["name"].lower() == str(id_name_input).lower():

                    item_encontrado = True

                    self.removeui.confirm_remove_item_interface(item["name"], item["quantity"], item["id"])
                
                    confirm_input = self.confirm_remove_item_input()

                    validation_confirm_user_prompt = self.is_confirmed_removing_item(confirm_input)
                    
                    if validation_confirm_user_prompt:
                        self.data_base.db_remove_item(item["name"])
                        print(f"{self.removeui.GREEN}Item removed successfully!{self.removeui.RESET}")
                        return
                    else:
                        print(f"{self.removeui.RED}Removal cancelled. Returning to main menu...{self.removeui.RESET}")
                        time.sleep(2)
                        return

            if not item_encontrado:
                print(f"{self.removeui.RED}Error: Item not found. Please check the ID or name and try again.{self.removeui.RESET}")
                time.sleep(2)
                return

    def search_item_in_database(self, database, id_name_input):
        self.item_encontrado = False

        for item in database:
            if item["id"] == id_name_input or item["name"].lower() == str(id_name_input).lower():

                self.item_encontrado = True

                self.removeui.confirm_remove_item_interface(item["name"], item["quantity"], item["id"])
            
                confirm_input = self.confirm_remove_item_input()

                self.validation_confirm_user_prompt = self.is_confirmed_removing_item(confirm_input)

    def item_name_id_input(self) -> str | None:
        while True:
            item_name = input(
                f"\n{self.GREEN} > Enter Item ID or Name: _{self.RESET} "
            ).strip().lower()

            if self.exit_to_menu(item_name):
                return None

            try:
                return int(item_name)
            except ValueError:
                pass

            return item_name

    def is_confirmed_removing_item(self, input_value: str) -> bool:
        if input_value.lower() in ["s", "sim", "y", "yes"]:
            return True

        return False
    
    def confirm_remove_item_input(self) -> str:
        confirmation = input(
            f"{self.RED}⚠ Are you sure you want to remove this item? This action cannot be undone! (y/n): {self.RESET}"
        )
        return confirmation.strip().lower()

    def exit_to_menu(self, input_value: str) -> bool:

        if input_value.lower() in ["s", "sim", "y", "yes"]:
            print(
                f"\n{self.RED}Operation cancelled. Returning to main menu...{self.RESET}\n"
            )
            time.sleep(0.5)
            return True

        return False

if __name__ == "__main__":
    remove = RemoveItensEngine()