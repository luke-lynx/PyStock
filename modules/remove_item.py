import sys
from pathlib import Path

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
            id_name = self.removeui.welcome_to_remove_item() 

            # Search for the item by ID or name
            search = self.data_base.db_search_item(id_name)

            item_encontrado = False

            for item in search:
                if item["id"] == id_name or item["name"].lower() == id_name.lower():
                    item_encontrado = True
                    confirm = self.removeui.confirm_remove_item(item["name"], item["quantity"], item["price"])
                    validation_confirm_user_prompt = self.confirm_remove_item(confirm)
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
            
    def confirm_remove_item(self, input_value):
        if input_value.lower() in ["s", "sim", "y", "yes"]:
            return True

        return False


if __name__ == "__main__":
    remove = RemoveItensEngine()