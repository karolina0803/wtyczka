### PROJEKT 2: WTYCZKA DO QGIS

Wtyczka służy do obliczania przewyższenia i pola powierzchni.

#Spis treści
...
costam

#### Wymagania
```
Python 3.11
Biblioteka numpy
System operacyjny Windows 10 lub 11
program QGIS wersja 3.34.4
biblioteka qgis.PyQt
biblioteka qgis.core
biblioteka PyQt5
```
#### Funkcje wtyczki
 ```
 1. Obliczanie przewyższenia pomiędzy dwoma punktami
 2. Obliczanie pola powierzchni pomiędzy punktami
 ```
#### Ogólny sposób użycia wtyczki

1. Na samym początku należy pobrać wtyczkę i umieścić ją w katalogu z wtyczkami dla programu QGIS. Następnie należy otworzyć program QGIS, przejść do zakładki Wtyczki>Zarządzanie wtyczkami i na samej górze w pasku wyszukiwania wpisać "Wtyczka". 
Po lewej stronie od jej nazwy pojawi się checkbox, który należy zaznaczyć.
2. Do nowego projektu należy dodać warstwy z atrybutami geometrii (SHP lub SHX).
3. Aby włączyć ID punktów należy kliknąć prawym przyciskiem myszy na warstwę, wejść we właściwości>etykiety>rozwinąć pasek na samej górze okna i wybrać proste etykiety>w pasku niżej wybrać wartość 'id'
4. Należy zaznaczyć wybrane punkty za pomocą narzędzia "Zaznacz obiekty" i uruchomić wtyczkę. (Warstwa z wybranymi punktami musi być aktywna i jednocześnie wybrana w oknie wtyczki)
5. Aby wykonać kolejną operację z użyciem wtyczki należy kliknąć Wyczyść lub Zamknij. Wyczyść - czyści zaznaczenie punktów i dane z okna wtyczki, Zamknij - czyści dane i zamyka okno. 
Zalecane jest czyszczenie za każdym razem przed użyciem.

#### Obliczanie przewyższenia

W celu obliczenia przewyższenia należy zaznaczyć dokładnie dwa punkty, których elementy posiadają atrybut "wysokość", uruchomić wtyczkę, wybrać warstwę, na której znajdują się punkty 
i kliknąć przycisk "oblicz przewyższenie". W oknie wtyczki wyświetlą się numery zaznaczonych punktów oraz policzone przewyższenie między nimi. UWAGA: występują błędy. Patrz: sekcja Znane błędy.
Wynik otrzymujemy z dokładnością 0.001m


#### Obliczanie pola powierzchni

W celu obliczenia pola powierzchni należy zaznaczyć na jednej aktywnej warstwie przynajmniej 3 punkty, a następnie uruchomić wtyczkę, kliknąć przycisk "oblicz pole powierzchni" 
i wybrać sposób wyświetlania wyniku (metry kwadratowe, ary, hektary). Każdy wynik otrzymujemy z dokładnością do 3 miejsc po przecinku. Funkcja działa niezależnie od nazw atrybutów dla co najmniej
3 wybranych punktów. W oknie wtyczki wyświetlą się wybrane punkty o rosnących numerach ID.


#### Znane błędy

1. Przy obliczaniu przewyższenia wynik podawany jest tylko w jedną stronę nieależnie od kolejności wybrania punktów. Przykładowo jeśli jeden punkt ma ID = 4, a drugi ID = 5, to przewyższenie
będzie liczone w kierunku 4->5 (zgodnie z rosnącym ID punktu). Nie jest możliwa operacja odwrotna.
