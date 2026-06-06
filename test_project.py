from project import validate_item_name, sanitize_sku, is_stock_low


def test_validate_item_name():
    assert validate_item_name("A") is False 
    assert validate_item_name("  ") is False
    assert validate_item_name("AB") is False
    assert validate_item_name("ABC") is True
    assert validate_item_name("A" * 41) is False
    assert validate_item_name("") is False
    assert validate_item_name("A" * 40) is True
    assert validate_item_name("  Valid Name  ") is True



def test_sanitize_sku():
    assert sanitize_sku(" abc-123 ") == "ABC123"
    assert sanitize_sku(" 123 456 ") == "123456"
    assert sanitize_sku("SKU-001") == "SKU001"
    assert sanitize_sku("   ") == ""
    assert sanitize_sku("- - -") == ""
    assert sanitize_sku("abc def-ghi") == "ABCDEFGHI"


def test_is_stock_low():
    assert is_stock_low(10, 5) is False
    assert is_stock_low("10", "5") is False
    assert is_stock_low("5", "10") is True
    assert is_stock_low(5, 10) is True
    assert is_stock_low(0, 0) is True
