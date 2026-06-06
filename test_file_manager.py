import file_manager
from pathlib import Path

def test_file_manager_initialization():
    fm = file_manager.FileManager()


    assert fm.base_path.exists()
    assert fm.base_path.is_dir()
    assert fm.base_path.name == "data"
    
def test_file_manager_properties():
    fm = file_manager.FileManager()
    
    expected_user_data_path = fm.base_path / "user_data.json"
    assert fm.user_data == expected_user_data_path
    assert isinstance(fm.user_data, Path)
    
    expected_initial_data_path = fm.base_path / "initial_data.json"
    assert fm.initial_data == expected_initial_data_path
    assert isinstance(fm.initial_data, Path)

def test_file_manager_get_path():
    fm = file_manager.FileManager()
    test_filename = "test_file.json"
    expected_path = fm.base_path / test_filename
    assert fm.get_path(test_filename) == expected_path
    assert isinstance(fm.get_path(test_filename), Path)
