Aplikacja pozwala na prowadzenie rejestru domowych wydatków oraz ich zapis do pliku "finance.json".
Dane są rejestrowane według schematu:
{
    "id": "[liczba_porządkowa]",
    "date": "[data_w_formacie_YYYY-MM-DD]",
    "category": "[kategoria]",
    "description": "[opis]",
    "amount": "[kwota]"
}

Aplikacja obsługuje następujące metody:

Metoda HTTP 	URI 	Akcja
GET 	http://[hostname]/finance/ 	Pobranie listy wydatków
GET 	http://[hostname]/finance/[id] 	Pobranie konkretnej pozycji
GET 	http://[hostname]/finance/total/  Zwraca sumę wydatków
POST 	http://[hostname]/finance/ 	Utworzenie nowej pozycji
PUT 	http://[hostname]/finance/[id] 	Update istniejącego wpisu
DELETE 	http://[hostname]/finance/[id] 	Usunięcie pozycji

UWAGA!
Przed uruchomieniem należy skonfigurować klucz CRSF w pliku "app.py" w linijce:
app.config["SECRET_KEY"] = "your_key"