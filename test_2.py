import pytest
from forTest import add, subtract  # замените your_module на имя вашего файла

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-2, -3) == 1

def test_subtract_zero():
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5

if __name__ == "__main__":
    # Запускаем pytest программно
    pytest.main([__file__])