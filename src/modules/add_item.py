import time
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pystockui import AddItemUI

class AddItemEngine:
    def __init__(self, sql_data_base):
        self.GREEN = "\033[92m"
        self.BLUE = "\033[94m"
        self.RED = "\033[91m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"
        self.CIANO = "\033[96m"
        self.MAGENTA = "\033[95m"
        self.YELLOW = "\033[33m"
        self.LARGURA = 60
        self.sql_data_base = sql_data_base

    def execute(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.ui = AddItemUI()

        while True:
            self.ui.welcome_to_add_item()

            name = self.item_name_input()
            if name is None:
                return

            quantity = self.quantity_item_input()
            if quantity is None:
                continue

            price = self.price_item_input()
            if price is None:
                continue

            self.ui.waiting_for_confirmation()

            if self.is_confirmed_adding_item(name, quantity, price):
                self.sql_data_base.db_insert_item(name, quantity, price)
                self.ui.confirmed_item_addition(name, quantity, price)
                return
            else:
                continue

    def item_name_input(self) -> str | None:
        item_name = input(
            f"{self.GREEN} > Item Name: _{self.RESET} ").strip()
        if self.exit_to_menu(item_name):
            return None
        return item_name

    def quantity_item_input(self) -> int | None:
        while True:
            quantity_item = input(
                f"{self.GREEN} > Initial Quantity: _{self.RESET} "
            ).strip()
            if self.exit_to_menu(quantity_item):
                return None

            try:
                quantity_item = int(quantity_item)
                if quantity_item < 0:
                    raise ValueError("✖ Invalid quantity! Please enter a non-negative integer.")
                return quantity_item
            except ValueError as e:
                print(f"{self.RED}{e}{self.RESET}\n")
                continue

    def price_item_input(self) -> float | None:
        while True:
            price_item = input(
                f"{self.GREEN} > Price per Unit: _{self.RESET} ").strip()
            if self.exit_to_menu(price_item):
                return None

            try:
                price_item = float(price_item)
                if price_item <= 0:
                    raise ValueError(
                        "✖ Invalid price! Please enter a positive number for price."
                    )
                return price_item
            except ValueError as e:
                print(f"{self.RED}{e}{self.RESET}\n")
                continue

    def is_confirmed_adding_item(self, name: str, quantity: int, price: float) -> bool:
        print(f"\n{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f"{self.BOLD}[ CONFIRMATION SUMMARY ]{self.RESET}")
        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f" {self.CIANO}Item Name{self.RESET}    : {name}")
        print(f" {self.CIANO}Quantity{self.RESET}      : {quantity} units")
        print(f" {self.CIANO}Price{self.RESET}         : ${price:.2f}")
        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")

        user_choice = (
            input(
                f"{self.YELLOW} > Confirm adding? ({self.GREEN}Y{self.RESET}{self.YELLOW}/{self.RESET}{self.RED}N{self.RESET}{self.YELLOW}): {self.RESET}"
            )
            .strip()
            .lower()
        )
        is_confirmed = user_choice in ["s", "sim", "y", "yes"]

        if not is_confirmed:
            print(f"\n{self.RED}Operation cancelled. Trying again...{self.RESET}\n")
            time.sleep(0.5)

        return is_confirmed

    def exit_to_menu(self, input_value) -> bool:
        if input_value.lower() in ["s", "sim", "y", "yes"]:
            print(
                f"\n{self.RED}Operation cancelled. Returning to main menu...{self.RESET}\n"
            )
            time.sleep(0.5)
            return True
        return False

if __name__ == "__main__":
    engine = AddItemEngine(None)
