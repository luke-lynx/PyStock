from file_manager import FileManager
from pystockui import AddItemUI
import json
import os


class AddItemEngine:
    def __init__(self):
        
        self.file_manager = FileManager()
        
        self.user_file_path = self.file_manager.user_data

        self.ui = AddItemUI()

        self.menu = self.ui.welcome_to_add_item()

        if self.menu:
        
            self.data = self.load_json(self.user_file_path)

            self.write = self.write_json()

    def load_json(self, user_data):

        if os.path.exists(user_data):
            with open(user_data, "r", encoding="utf-8") as f:

                try:
                    data = json.load(f)
                    return data
                except json.JSONDecodeError as e:

                    return (
                        None,
                        f"{self.ui.RED}Error: Failed to parse user data file: {self.ui.GREEN} {e.msg} in line {e.lineno} column {e.colno}{self.ui.RESET}",
                    )
        else:
            raise FileNotFoundError(
                f"\n{self.ui.YELLOW}User data file not found.{self.ui.RESET}\n"
            )

    def write_json(self):

        name = self.ui._name
        quantity = self.ui._quantity

        new_data = {"id": len(self.data) + 1, "nome": name, "quantidade": quantity}

        self.data.append(new_data)

        with open(self.user_file_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())


if __name__ == "__main__":
    engine = AddItemEngine()