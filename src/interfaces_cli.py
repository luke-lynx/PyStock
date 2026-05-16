import sys
import time


class PyStockUI:
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
        time.sleep(1)


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



menu = PyStockUI()

menu.welcome_to_program()

menu.setup_data_persistence()