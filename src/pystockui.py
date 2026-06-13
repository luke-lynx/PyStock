import os
import time
#import json
#import sys

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
        time.sleep(0.9)


    def display_main_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{self.BLUE}{'=' * self.LARGURA}{self.RESET}")
        print(f"{self.BOLD}{'MAIN MENU'.center(self.LARGURA)}{self.RESET}")
        print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")

        print(f"  {self.BLUE}1.{self.RESET} Add Food Item")
        print(f"  {self.BLUE}2.{self.RESET} Remove Food Item")
        print(f"  {self.BLUE}3.{self.RESET} Update Food Item")
        print(f"  {self.BLUE}4.{self.RESET} List Inventory")

        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f"  {self.RED}0.{self.RESET} Exit")
        print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")

    
    def loading_animation(self, duration=2):
        animation = "|/-\\"
        idx = 0
        start_time = time.time()

        while (time.time() - start_time) < duration:
            print(f"\r{self.CIANO}Loading... {animation[idx % len(animation)]}{self.RESET}", end="")
            idx += 1
            time.sleep(0.1)

        print("\r" + " " * (len("Loading... ") + 1) + "\r", end="")

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
        self._quantity = 0
        self.LARGURA = 60

    def welcome_to_add_item(self):
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

    def waiting_for_confirmation(self):
        print(f"\n{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f"{self.CIANO} [ STATUS ] Waiting for confirmation... {self.RESET}")

    def confirmed_item_addition(self, item_name, quantity_item, price_item):
        print(
            f"{self.GREEN}✔ Item '{item_name}' with quantity {quantity_item} and price {price_item} has been confirmed for addition!{self.RESET}\n"
        )
        print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")
        time.sleep(1.5)

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

    def welcome_to_remove_item_interface(self):
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

    def confirm_remove_item_interface(self, nome, qtd, id):
        print(f"\n{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f"{self.BOLD} [ STATUS ] Searching database...{self.RESET}")
        print(f"{self.BLUE}{'=' * self.LARGURA}")
        print(f"\n{self.GREEN}Item found: {self.YELLOW}'{nome}'{self.RESET} with quantity {self.YELLOW}{qtd}{self.RESET} (ID: {self.YELLOW}{id}{self.RESET})")

class UpdateItemUI:
    def __init__(self):
        self.GREEN = "\033[92m"
        self.BLUE = "\033[94m"
        self.RED = "\033[91m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"
        self.CIANO = "\033[96m"
        self.MAGENTA = "\033[95m"
        self.YELLOW = "\033[33m"
        self.LARGURA = 70

    def top_update_interface(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")
        print(f"{self.BOLD}{self.YELLOW}{'UPDATE ENGINE SUBSYSTEM (v0.1.5)'.center(self.LARGURA)}{self.RESET}")
        print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")
        print(f"{self.GREEN}{' How would you like to locate the target record?'}{self.RESET}\n")
        print(f"{self.CIANO} [1]Search by ID (Exact Match){self.RESET}")
        print(f"{self.RED} [0]Cancel and Return to Main Menu{self.RESET}")
        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        option = input(f"{self.GREEN} Select option: _{self.RESET} ").strip()
        return option


    def search_by_id_interface(self):
        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f"{self.BOLD}{self.YELLOW}{' >>> IDENTIFIER QUERY (ID)'}{self.RESET}")
        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        try:
            id_ = int(input(f"{self.GREEN} Enter item numeric ID (e.g., 1, 42): _{self.RESET} ").strip())
        except ValueError:
            print(f"\n{self.RED}Invalid input! Please enter a valid integer for ID.{self.RESET}")
            time.sleep(1.5)
            return None
        return id_

    def located(self, id_, name, quantity):
        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f"{self.BOLD}{self.CIANO}{' [ ITEM RECORD FOUND ]'}{self.RESET}")
        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f"{self.CIANO}{' ID':<15} {self.YELLOW}:{id_}{self.RESET}")
        print(f"{self.CIANO}{' Name':<15} {self.YELLOW}:{name}{self.RESET}")
        print(f"{self.CIANO}{' Quantity':<15} {self.YELLOW}:{quantity}{self.RESET}")
        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        user_confirm = input(f"{self.GREEN} Is this the item you want to update? (Y/N): {self.RESET}").strip().lower()
        if user_confirm in ["s", "sim", "y", "yes"]:
            return True
        else:
            return False

    def edit_interface(self, actual_name, actual_quantity, actual_price):
        print(f"\n{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        print(f"{self.BOLD}{self.CIANO}{'      >>> DATA MODIFICATION'}{self.RESET}")
        print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
        change_name = input(f"{self.GREEN} Change name '{actual_name}'? (y/n): {self.RESET}").strip().lower()
        if change_name in ["s", "sim", "y", "yes"]:
            new_name = input(f"{self.GREEN} Enter new name: {self.RESET}").strip()
            confirm_name = input(f"{self.YELLOW} [CONFIRMATION] Save '{new_name}'? (y/n): {self.RESET}").strip().lower()
            if confirm_name in ["s", "sim", "y", "yes"]:
                actual_name = new_name
                print(f"{self.GREEN} Name updated successfully!{self.RESET}")
            else:
                actual_name = actual_name
        
        change_quantity = input(f"{self.GREEN} Change quantity '{actual_quantity}'? (y/n): {self.RESET}").strip().lower()
        if change_quantity in ["s", "sim", "y", "yes"]:
            try:
                new_quantity = int(input(f"{self.GREEN} Enter new quantity: {self.RESET}").strip())
                actual_quantity = new_quantity
                print(f"{self.GREEN} Quantity updated successfully!{self.RESET}")
            except ValueError:
                print(f"{self.RED} Invalid input! Quantity must be an integer. Quantity not changed.{self.RESET}")
        else:
            actual_quantity = actual_quantity

        change_price = input(f"{self.GREEN} Change price '{actual_price}'? (y/n): {self.RESET}").strip().lower()
        if change_price in ["s", "sim", "y", "yes"]:
            try:
                new_price = float(input(f"{self.GREEN} Enter new price: {self.RESET}").strip())
                actual_price = new_price
                print(f"{self.GREEN} Price updated successfully!{self.RESET}")
            except ValueError:
                print(f"{self.RED} Invalid input! Price must be a number. Price not changed.{self.RESET}")
        else:
            actual_price = actual_price


        return actual_name, actual_quantity, actual_price
    

    def final_confirmation(self, id_, name, quantity, price, new_name, new_quantity, new_price):
            print(f"\n{self.BLUE}{'=' * self.LARGURA}{self.RESET}")
            print(f"{self.BOLD}{self.GREEN}{'CHANGES SUMMARY'.center(self.LARGURA)}{self.RESET}")
            print(f"{self.BLUE}{'=' * self.LARGURA}{self.RESET}")  
            print(f" {self.GREEN}{'ID':<12}{self.YELLOW}: {self.RESET}{id_}")
            print(f" {self.GREEN}{'Name':<12}{self.YELLOW}: {self.RESET}{name:<20} -->  {self.CIANO}{new_name}{self.RESET}")
            print(f" {self.GREEN}{'Quantity':<12}{self.YELLOW}: {self.RESET}{str(quantity):<20} -->  {self.CIANO}{new_quantity}{self.RESET}")
            print(f" {self.GREEN}{'Price':<12}{self.YELLOW}: {self.RESET}{str(price):<20} -->  {self.CIANO}{new_price}{self.RESET}")
            print(f"{self.BLUE}{'-' * self.LARGURA}{self.RESET}")
            confirm = input(f" {self.YELLOW}Confirm changes? (y/n): {self.RESET}").strip().lower()
            
            if confirm in ["s", "sim", "y", "yes"]:
                return True
            else:
                return False

if __name__ == "__main__":
    ui = MainPyStockUI()