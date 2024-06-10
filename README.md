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
2. Do nowego projektu należy dodać warstwy warstwy z atrybutami geometrii (SHP lub SHX).
3. Należy zaznaczyć wybrane punkty za pomocą narzędzia "Zaznacz obiekty" i uruchomić wtyczkę. (Warstwa z wybranymi punktami musi być aktywna i jednocześnie wybrana w oknie dialogowym wtyczki)

#### Obliczanie przewyższenia

W celu obliczenia przewyższenia należy zaznaczyć dokładnie dwa punkty, których elementy posiadają atrybut "wysokość", uruchomić wtyczkę, wybrać warstwę, na której znajdują się punkty 
i kliknąć przycisk "oblicz przewyższenie". W oknie wtyczki wyświetlą się numery zaznaczonych punktów oraz policzone przewyższenie między nimi. UWAGA: występują błędy. Patrz: sekcja Znane błędy.
Wynik otrzymujemy z dokładnością 0.001m


#### Obliczanie pola powierzchni

W celu obliczenia pola powierzchni należy zaznaczyć na jednej aktywnej warstwie przynajmniej 3 punkty, a następnie uruchomić wtyczkę poprzez kliknięcie przycisku "oblicz pole powierzchni" 
i wybrać sposób wyświetlania wyniku. Każdy wynik otrzymujemy z dokładnością do 3 miejsc po przecinku.


#### Znane błędy

1. Przy obliczaniu przewyższenia wynik podawany jest tylko w jedną stronę nieależnie od kolejności wybrania punktów. Przykładowo jeśli jeden punkt ma numer 4, a drugi numer 5, to przewyższenie
będzie liczone w kierunku 4->5 (zgodnie z rosnącym numerem punktu). Nie jest możliwa operacja odwrotna.