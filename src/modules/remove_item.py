from file_manager import FileManager
from pystockui import RemoveItemUI
import json
import os

class RemoveItensEngine:
    def __init__(self):

        self.file_manager = FileManager()

        self.user_file_path = self.file_manager.user_data

        self.removeui = RemoveItemUI()

        self.remove_itens()

    def remove_itens(self):
    
        id_name = self.removeui.welcome_to_remove_item()  # Part 1°

        if os.path.exists(self.user_file_path):
            with open(self.file_manager.user_data, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    print(
                        f"{self.removeui.RED}Error: Failed to parse user data file: {self.removeui.GREEN} {e.msg} in line {e.lineno} column {e.colno}{self.removeui.RESET}"
                    )
                    return
            for item in data:
                if int(item.get("id")) == int(id_name) or item.get("name").lower() == str(id_name).lower():
                    
                    data["itens"].remove(item)
                    
                    with open(self.file_manager.user_data, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                    print(f"{self.removeui.GREEN}Item removed successfully!{self.removeui.RESET}")
                    return

        
        else:
            print(f"{self.removeui.RED}Error: User data file not found.{self.removeui.RESET}")
            return


if __name__ == "__main__":
    remove = RemoveItensEngine()