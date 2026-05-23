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
        self.CIANO = "\033[96m"
        self.MAGENTA = "\033[95m"
        self.YELLOW = "\033[33m"
        self.LARGURA = 60

    def welcome_to_program(self):
        largura = 60
        print(f"{self.BLUE}{'-' * largura}{self.RESET}")
        print(f"{self.BOLD}{'PyStock - v0.1.5'.center(largura)}{self.RESET}")
        print(f"{self.BLUE}{'-' * largura}{self.RESET}")
        print("Welcome to the inventory management system.")
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
        print(
            f"{self.BOLD}IMPORTANT NOTICE{self.RESET if not hasattr(self, 'RESET') else self.RESET}"
        )
        print("A new database file must be created to continue.")

        confirm = input("Do you wish to proceed? (Y/N): ").strip().lower()

        if confirm not in ["s", "sim", "y", "yes"]:
            print(f"\n{self.RED}Operation cancelled. Exiting...{self.RESET}\n")
            sys.exit()

        try:
            with open(file_path, "w", encoding="utf8") as f:
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

                with open(source_path, "r", encoding="utf8") as f_source:
                    initial_items = json.load(f_source)

                with open(target_path, "w", encoding="utf8") as f_target:
                    json.dump(initial_items, f_target, indent=4, ensure_ascii=False)

                print(f"\n{self.GREEN}✔ 50 items added successfully!{self.RESET}\n")
                return initial_items

            except FileNotFoundError:
                print(
                    f"\n{self.RED}✖ Error: Initial data file not found.{self.RESET}\n"
                )
            except json.JSONDecodeError:
                print(
                    f"\n{self.RED}✖ Error: Failed to parse initial data.{self.RESET}\n"
                )

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


class AddItemUI:
    def __init__(self):
        self.GREEN = "\033[92m"
        self.BLUE = "\033[94m"
        self.RED = "\033[91m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"
        self.CIANO = "\033[96m"
        self.MAGENTA = "\033[95m"
        self.YELLOW = "\033[33m"
        self._name = None
        self._quantity = 0
        self.LARGURA = 60

    def welcome_to_add_item(self):
        while True:

            print("")
            print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")
            print(
                f"{self.BOLD}{'NEW ITEM REGISTRATION - PyStock'.center(self.LARGURA)}{self.RESET}"
            )
            print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
            print(f"{self.BOLD}{"Please provide the item details below"}{self.RESET}")
            print(
                f"{self.GREEN}{"Tip: Type "}{self.RESET}{self.RED}'S'{self.RESET} {self.GREEN}{"at any prompt to cancel and return to menu."}{self.RESET}"
            )
            print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}\n")

            item_name = input(f"{self.GREEN} > Item Name: _{self.RESET} ").strip()
            if self.exit_to_menu(item_name):
                return None

            quantity_item = input(
                f"{self.GREEN} > Initial Quantity: _{self.RESET} "
            ).strip()
            if self.exit_to_menu(quantity_item):
                return None

            try:
                quantity_item = int(quantity_item)
                if quantity_item < 0:
                    print(
                        f"\n{self.RED}✖ Invalid quantity! Please enter a non-negative integer.{self.RESET}\n"
                    )
                    continue

            except ValueError:
                print(
                    f"\n{self.RED}✖ Invalid input! Please enter a valid integer for quantity.{self.RESET}\n"
                )
                continue

            print(f"\n{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
            print(f"{self.CIANO} [ STATUS ] Wainting for confirmation... {self.RESET}")

            confirm = (
                input(
                    f"{self.YELLOW} > Confirm adding '{item_name}' with quantity {quantity_item}? ({self.GREEN}Y{self.RESET}{self.YELLOW}/{self.RESET}{self.RED}N{self.RESET}{self.YELLOW}): {self.RESET}"
                )
                .strip()
                .lower()
            )
            if self.reject_option(confirm):
                return None
            print(
                f"{self.GREEN}✔ Item '{item_name}' with quantity {quantity_item} confirmed for addition!{self.RESET}\n"
            )
            print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")

            self._name = item_name
            self._quantity = quantity_item
            return True, self._name, self._quantity

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    def reject_option(self, input_value):

        if input_value.lower() in ["n", "no", "nao", "não"]:
            print(
                f"\n{self.RED}Operation cancelled. Returning to main menu...{self.RESET}\n"
            )
            time.sleep(0.5)
            return True

    def exit_to_menu(self, input_value):

        if input_value.lower() in ["s", "sim", "y", "yes"]:
            print(
                f"\n{self.RED}Operation cancelled. Returning to main menu...{self.RESET}\n"
            )
            time.sleep(0.5)
            return True

        return False


class RemoveItemUI:
    def __init__(self):
        self.GREEN = "\033[92m"
        self.BLUE = "\033[94m"
        self.RED = "\033[91m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"
        self.CIANO = "\033[96m"
        self.MAGENTA = "\033[95m"
        self.YELLOW = "\033[33m"
        self.LARGURA = 60


    def welcome_to_remove_item(self):
        print(f"\n{self.BLUE}{'=' * self.LARGURA}{self.RESET}")
        print(
            f"{self.BOLD}{'REMOVE ITEM FROM INVENTORY'.center(self.LARGURA)}{self.RESET}"
        )
        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(
            f"{self.BOLD}{" CAUTION: This action will permanently delete the record."}{self.RESET}"
        )
        print(f"{self.GREEN}{' Type S to cancel and return to Main Menu.'}{self.RESET}")
        print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")

        while True:
            item_name = input(
                f"\n{self.GREEN} > Enter Item ID or Name: _{self.RESET} "
            ).strip().lower()

             
            if self.exit_to_menu(item_name):
                return None

             
            try:
                return int(item_name)
            except ValueError:
                 
                pass                

             
            return item_name


    def confirm_remove_item(self, nome, qtd, id):
        print(f"\n{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f"{self.BOLD} [ STATUS ] Searching database...{self.RESET}")
        print(f"{self.BLUE}{'=' * self.LARGURA}")
        print(f"\n{self.GREEN}Item found: {self.YELLOW}'{nome}'{self.RESET} with quantity {self.YELLOW}{qtd}{self.RESET} (ID: {self.YELLOW}{id}{self.RESET})")
        confirmation = input(
            f"{self.RED}⚠ Are you sure you want to remove this item? This action cannot be undone! (y/n): {self.RESET}"
        )
        return confirmation.strip().lower()


    def exit_to_menu(self, input_value):

        if input_value.lower() in ["s", "sim", "y", "yes"]:
            print(
                f"\n{self.RED}Operation cancelled. Returning to main menu...{self.RESET}\n"
            )
            time.sleep(0.5)
            return True

        return False
    

if __name__ == "__main__":
    menu = RemoveItemUI()
    menu.welcome_to_remove_item()