from file_manager import FileManager
from pystockui import AddItemUI
from pathlib import Path
import json
import os


class AddItemEngine:
    def __init__(self):

        self.file_manager = FileManager()

        self.user_file_path = self.file_manager.user_data

        self.ui = AddItemUI()

    def load_json(self, user_data):

        if os.path.exists(user_data):
            with open(user_data, "r", encoding="utf-8") as f:

                try:
                    data = json.load(f)
                    return data, None
                except json.JSONDecodeError as e:

                    return (
                        None,
                        f"{self.ui.RED}Error: Failed to parse user data file: {self.ui.GREEN} {e.msg} in line {e.lineno} column {e.colno}{self.ui.RESET}",
                    )
        else:
            raise FileNotFoundError(
                f"\n{self.ui.YELLOW}User data file not found.{self.ui.RESET}\n"
            )

    def write_json(self, user_data, name, quantity):

        with open(user_data, "w", encoding="utf-8") as f:
            json.dump(..., f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    engine = AddItemEngine()
