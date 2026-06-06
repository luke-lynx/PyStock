import sys
from pathlib import Path

# Add parent directory to path to allow imports from root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from file_manager import FileManager
import time
import os 
import json

class ListItem:
    def __init__(self):
        self.GREEN = "\033[92m"
        self.BLUE = "\033[94m"
        self.RED = "\033[91m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"
        self.CYAN = "\033[96m"
        self.MAGENTA = "\033[95m"
        self.YELLOW = "\033[33m"
        self.WIDTH = 75

        self.file_manager = FileManager()
        self.file_data = self.file_manager.user_data
        
        self.list_all()

    def list_all(self):
        if os.path.exists(self.file_data):
            try:
                with open(self.file_data, 'r', encoding='utf8') as f:
                    data_base_json = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                data_base_json = []

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{self.BOLD}{self.BLUE}{'=' * self.WIDTH}{self.RESET}")
            print(f"{self.BOLD}{self.YELLOW}{'PYSTOCK - CURRENT INVENTORY'.center(self.WIDTH)}{self.RESET}")
            print(f"{self.BOLD}{self.BLUE}{'=' * self.WIDTH}{self.RESET}")
            
            print(f"{self.BOLD}{self.CYAN}{'ID':<4} | {'ITEM NAME':<30} | {'QTY':<6} | {'CATEGORY':<15} | {'STATUS'}{self.RESET}")
            print(f"{self.BLUE}{'-' * self.WIDTH}{self.RESET}")

            if not data_base_json:
                print(f"{self.YELLOW}{'No items registered in stock.'.center(self.WIDTH)}{self.RESET}")
            else:
                for data in data_base_json:
                    qty = data.get('quantidade', 0)
                    
                    if qty == 0:
                        status = "OUT OF STOCK"
                        status_color = self.RED
                    elif qty <= 5:
                        status = "LOW"
                        status_color = self.YELLOW
                    else:
                        status = "OK"
                        status_color = self.GREEN

                    item_id = data.get('id', '??')
                    name = data.get('nome', 'No Name')[:30]
                    category = data.get('categoria', 'General')[:15]

                    print(f"{item_id:<4} | {name:<30} | {qty:<6} | {category:<15} | {status_color}{self.BOLD}{status:<12}{self.RESET}")

            print(f"{self.BLUE}{'-' * self.WIDTH}{self.RESET}")
            print(f"{self.BOLD}Total items listed: {len(data_base_json)}{self.RESET}")
            print(f"{self.BLUE}{'=' * self.WIDTH}{self.RESET}")
            input(f"\n{self.CYAN}Press Enter to return to the menu...{self.RESET}")

        else:
            print(f"\n{self.RED}[!] Error: Data file not found.{self.RESET}")
            time.sleep(2)
            return 1

if __name__ == "__main__":
    ListItem()