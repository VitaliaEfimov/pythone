import coverage
import pytest

def run_tests_with_coverage():
    # Инициализируем coverage
    cov = coverage.Coverage()
    cov.start()
    
    # Запускаем тесты
    pytest.main(["-v", "test_2.py"])
    
    # Останавливаем сбор данных
    cov.stop()
    cov.save()
    
    # Выводим отчет
    print("\n" + "="*50)
    print("ОТЧЕТ О ПОКРЫТИИ")
    print("="*50)
    cov.report()
    
    # Детальный отчет с пропущенными строками
    print("\n" + "="*50)
    print("ДЕТАЛЬНЫЙ ОТЧЕТ (пропущенные строки)")
    print("="*50)
    cov.report(show_missing=True)
    
    # Можно также сгенерировать HTML отчет
    cov.html_report(directory='htmlcov')

if __name__ == "__main__":
    run_tests_with_coverage()