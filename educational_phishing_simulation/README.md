# Symulacja Formularza Ogłoszenia OLX

**Cel projektu:** 

Ten projekt ma na celu edukację i praktykę w tworzeniu formularzy internetowych oraz obsługi danych za pomocą Flask w Pythonie. Projekt symuluje formularz dodawania ogłoszenia podobny do tego, który można znaleźć na OLX.

## Jak uruchomić projekt:

1. **Skopiuj repozytorium:**
    ```bash
    git clone <URL-repo>
    cd educational_phishing_simulation
    ```

2. **Utwórz i aktywuj wirtualne środowisko:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Na Windows: venv\Scripts\activate
    ```

3. **Zainstaluj wymagane biblioteki:**
    ```bash
    pip install flask
    ```

4. **Uruchom aplikację:**
    ```bash
    python app.py
    ```

5. **Otwórz przeglądarkę i przejdź do:**
    ```
    http://127.0.0.1:5000/
    ```

## Pliki:

- `app.py` - Główny skrypt aplikacji Flask.
- `templates/form.html` - Szablon HTML formularza.
- `static/style.css` - Stylizacja formularza.
