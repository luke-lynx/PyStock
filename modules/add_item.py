import sys
from pathlib import Path

# Add parent directory to path to allow imports from root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pystockui import AddItemUI

class AddItemEngine:
    def __init__(self, data_base):
        self.db = data_base

    def execute(self):
        self.ui = AddItemUI()
        
        self.bool, self._name, self._quantity, self._price = self.ui.welcome_to_add_item()

        self.db.db_insert_item(self._name, self._quantity, self._price)
        return None


if __name__ == "__main__":
    engine = AddItemEngine()