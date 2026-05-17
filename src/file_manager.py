from pathlib import Path


class FileManager:
    def __init__(self):
        
        self.base_path = Path(__file__).resolve().parent.parent / "data"
        
        self.base_path.mkdir(exist_ok=True)

    def get_path(self, filename):
        
        return self.base_path / filename

    @property
    def user_data(self):
        return self.get_path("user_data.json")

    @property
    def initial_data(self):
        return self.get_path("initial_data.json")
    
