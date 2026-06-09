import sys
from pathlib import Path

# Add parent directory to path to allow imports from root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from python_db_manager import OpenDatabase
import time
import os


class ListItem:
    def __init__(self, data_base: OpenDatabase):
        self.GREEN = "\033[92m"
        self.BLUE = "\033[94m"
        self.RED = "\033[91m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"
        self.CYAN = "\033[96m"
        self.MAGENTA = "\033[95m"
        self.YELLOW = "\033[33m"
        self.WIDTH = 75
        self.data_base = data_base
        self.sql_data_base_right = self.data_base.db_fetch_all()
            
    def execute(self):
        self.list_all()

    def list_all(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{self.BOLD}{self.BLUE}{'=' * self.WIDTH}{self.RESET}")
        print(f"{self.BOLD}{self.YELLOW}{'PYSTOCK - CURRENT INVENTORY'.center(self.WIDTH)}{self.RESET}")
        print(f"{self.BOLD}{self.BLUE}{'=' * self.WIDTH}{self.RESET}")
        print(f"{self.BOLD}{self.CYAN}{'ID':<4} | {'ITEM NAME':<30} | {'QTY':<6} | {'PRICE':<15} | {'STATUS'}{self.RESET}")
        print(f"{self.BLUE}{'-' * self.WIDTH}{self.RESET}")

        if not self.sql_data_base_right:
            print(f"{self.YELLOW}{'No items registered in stock.'.center(self.WIDTH)}{self.RESET}")
        else:
            for data in self.sql_data_base_right:
                qty = data["quantity"]
                
                if qty == 0:
                    status = "OUT OF STOCK"
                    status_color = self.RED
                elif qty <= 5:
                    status = "LOW"
                    status_color = self.YELLOW
                else:
                    status = "OK"
                    status_color = self.GREEN

                item_id = data["id"]
                name = data["name"][:30]
                price = data["price"]

                print(f"{item_id:<4} | {name:<30} | {qty:<6} | {price:<15} | {status_color}{self.BOLD}{status:<12}{self.RESET}")

        print(f"{self.BLUE}{'-' * self.WIDTH}{self.RESET}")
        print(f"{self.BOLD}Total items listed: {len(self.sql_data_base_right)}{self.RESET}")
        print(f"{self.BLUE}{'=' * self.WIDTH}{self.RESET}")
        input(f"\n{self.CYAN}Press Enter to return to the menu...{self.RESET}")
        time.sleep(3)

if __name__ == "__main__":
    db = OpenDatabase()
    ListItem(db)