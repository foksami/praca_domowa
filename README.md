# Testy automatyczne GUI dla Mbanku

## Opis
Projekt ten zawiera zadanie domowe

## Struktura katalogów
- `pages/`: Klasy Page Object dla różnych stron aplikacji.
- `tests/`: Pliki testowe.
- `reports/`: Raporty z wynikami testów.
- `requirements.txt`: Zależności projektu.
- `README.md`: Dokumentacja projektu.

## Uruchomienie testów
1. Zainstaluj zależności:
    ```sh
    pip install -r requirements.txt
    ```
2. Uruchom testy:
    ```sh
    pytest --html=report.html

    ```
3. Raport z testów znajdziesz w `reports/test_report.html`.
