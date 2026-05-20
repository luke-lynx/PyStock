from modules import add_item, remove_item, list_item, update_item
from file_manager import FileManager
from pystockui import MainPyStockUI
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

        self.file_manager = FileManager()
        self.user_file_path = self.file_manager.user_data
        self.itens_file_path = self.file_manager.initial_data

    def main(self):
        self.menu.welcome_to_program()
        self.menu.setup_data_persistence()
        self.menu.initialize_data_file(self.user_file_path)
        self.menu.populate_initial_data(self.itens_file_path, self.user_file_path)
        self.interface()

    def interface(self):
        acoes = {
            "1": add_item.AddItemEngine,
            "2": remove_item.RemoveItensEngine,
            "3": update_item.update_item,
            "4": list_item.list_all,
        }

        while True:
            self.menu.display_main_menu()

            opcao = input(f"{self.BOLD}Select an option: {self.RESET}").strip()

            if opcao == "0":
                print(f"\n{self.RED}Exiting system...{self.RESET}\n")
                sys.exit()

            acao_escolhida = acoes.get(opcao)

            if acao_escolhida:
                acao_escolhida()
            else:
                print(f"\n{self.RED}✖ Invalid option! Please try again.{self.RESET}")
                time.sleep(1.5)


if __name__ == "__main__":
    system = MainSystem()
    system.main()