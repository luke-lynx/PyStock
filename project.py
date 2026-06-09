from modules import AddItemEngine, RemoveItensEngine, ListItem, UpdateItemEngine
from pystockui import MainPyStockUI
from python_db_manager import OpenDatabase
import time
import sys


class MainSystem:
    def __init__(self):
        self.GREEN = "\033[92m"
        self.BLUE = "\033[94m"
        self.RED = "\033[91m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"
        self.LARGURA = 60
        self.menu = MainPyStockUI()
        self.db = OpenDatabase()

    def start(self):
        self.menu.welcome_to_program()
        self.interface()

    def interface(self):
        acoes = {
            "1": AddItemEngine,
            "2": RemoveItensEngine,
            "3": UpdateItemEngine,
            "4": ListItem,
        }

        while True:
            self.menu.display_main_menu()

            option = input(f"{self.BOLD}Select an option: {self.RESET}").strip()

            if option == "0":
                print(f"\n{self.RED}Exiting system...{self.RESET}\n")
                sys.exit()


            class_choice = acoes.get(option)

            if class_choice :

                execute_class = class_choice(self.db)
                
                execute_class.execute()
            else:
                print(f"\n{self.RED}✖ Invalid option! Please try again.{self.RESET}")
                time.sleep(1)


def main():
    system = MainSystem()
    system.start()


if __name__ == "__main__":
    main()