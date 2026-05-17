from file_manager import FileManager
from pathlib import Path
import time
import json
import sys



   

class MainPyStockUI:
    def __init__(self):
        self.GREEN = "\033[92m"
        self.BLUE = "\033[94m"
        self.RED = "\033[91m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"
        self.LARGURA = 60


    def welcome_to_program(self):
        largura = 60
        print(f"{self.BLUE}{'-' * largura}{self.RESET}")
        print(f"{self.BOLD}{'PyStock - v0.1.5'.center(largura)}{self.RESET}")
        print(f"{self.BLUE}{'-' * largura}{self.RESET}")
        print(f"Welcome to the inventory management system.")
        print(f"Status: {self.GREEN}● Online{self.RESET}")
        print(f"{self.BLUE}{'-' * largura}{self.RESET}\n")
        time.sleep(0.4)


    def setup_data_persistence(self):
        print(f"{self.RED}\nATTENTION:{self.RESET}")
        prompt = (
            "A new data file must be created even if one already exists.\n"
            "Do you wish to continue? (Y/N): "
        )
        
        confirm = input(prompt).strip().lower()

        if confirm not in ["s", "sim", "y", "yes"]:
            print(f"\n{self.RED}Exiting system...{self.RESET}\n")
            sys.exit()
        
        print(f"\n{self.GREEN}Initialization confirmed.{self.RESET}\n")


    def initialize_data_file(self, file_path):

        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f"{self.BOLD}IMPORTANT NOTICE{self.RESET if not hasattr(self, 'RESET') else self.RESET}")
        print("A new database file must be created to continue.")
        
        confirm = input("Do you wish to proceed? (Y/N): ").strip().lower()

        if confirm not in ["s", "sim", "y", "yes"]:
            print(f"\n{self.RED}Operation cancelled. Exiting...{self.RESET}\n")
            sys.exit()

        try:
            with open(file_path, 'w', encoding='utf8') as f:
                json.dump([], f, indent=4, ensure_ascii=False)
            
            print(f"\n{self.GREEN}✔ Database initialized successfully!{self.RESET}")
            return [] 
            
        except Exception as e:
            print(f"\n{self.RED}✖ Critical error creating file: {e}{self.RESET}")
            sys.exit()


    def populate_initial_data(self, source_path, target_path):
        
        print(f"{self.BOLD}QUICK START:{self.RESET}")
        prompt = "Would you like to add the 50 most common items? (Y/N): "
        
        choice = input(prompt).strip().lower()

        if choice in ["s", "sim", "y", "yes"]:
            try:
            
                with open(source_path, 'r', encoding='utf8') as f_source:
                    initial_items = json.load(f_source)

                with open(target_path, 'w', encoding='utf8') as f_target:
                    json.dump(initial_items, f_target, indent=4, ensure_ascii=False)

                print(f"\n{self.GREEN}✔ 50 items added successfully!{self.RESET}\n")
                return initial_items

            except FileNotFoundError:
                print(f"\n{self.RED}✖ Error: Initial data file not found.{self.RESET}\n")
            except json.JSONDecodeError:
                print(f"\n{self.RED}✖ Error: Failed to parse initial data.{self.RESET}\n")
        
        return None


    def display_main_menu(self):
            
            print(f"\n{self.BLUE}{'=' * self.LARGURA}{self.RESET}")
            print(f"{self.BOLD}{'MAIN MENU'.center(self.LARGURA)}{self.RESET}")
            print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")
            
            print(f"  {self.BLUE}1.{self.RESET} Add Food Item")
            print(f"  {self.BLUE}2.{self.RESET} Remove Food Item")
            print(f"  {self.BLUE}3.{self.RESET} Update Food Item")
            print(f"  {self.BLUE}4.{self.RESET} List Inventory")
            print(f"  {self.BLUE}5.{self.RESET} Manage Quantities")
            
            print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
            print(f"  {self.RED}0.{self.RESET} Exit")
            print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")


if __name__ == "__main__":
    menu = MainPyStockUI()